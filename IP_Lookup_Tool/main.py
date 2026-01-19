import json
import os
import webbrowser
import requests
import customtkinter as ctk
from PIL import Image
from datetime import datetime
import threading
import tkintermapview

# --- Avant-Garde Theme Engine ---
THEMES = {
    "Ocean Blue": {"main": "#3b82f6", "hover": "#2563eb", "text": "white"},
    "Emerald": {"main": "#10b981", "hover": "#059669", "text": "white"},
    "Rose Pink": {"main": "#f43f5e", "hover": "#e11d48", "text": "white"},
    "Purple Rain": {"main": "#8b5cf6", "hover": "#7c3aed", "text": "white"},
    "Amber Gold": {"main": "#f59e0b", "hover": "#d97706", "text": "white"},
    "Cyberpunk": {"main": "#ff00ff", "hover": "#d400d4", "text": "white"}
}

LANGUAGES = {
    "tr": {
        "title": "IP Bulucu Pro",
        "search_placeholder": "IP Adresi veya Alan Adı girin...",
        "check_my_ip": "Kendi IP'm",
        "search": "Analiz Et",
        "settings": "Ayarlar",
        "appearance": "Görünüm Modu",
        "language": "Uygulama Dili",
        "theme": "Vurgu Rengi",
        "results": "IP Analiz Raporu",
        "ip_address": "IP Adresi",
        "org": "Servis Sağlayıcı (ISP)",
        "city": "Şehir",
        "region": "Bölge / Eyalet",
        "country": "Ülke",
        "zip": "Posta Kodu",
        "timezone": "Saat Dilimi",
        "coords": "Koordinatlar",
        "open_maps": "Haritada Göster",
        "error_conn": "Hata: Bağlantı Yok!",
        "error_invalid": "Hata: Geçersiz IP!",
        "search_complete": "Analiz Tamamlandı.",
        "copy_success": "Kopyalandı!",
        "dark": "Koyu", "light": "Açık", "system": "Sistem"
    },
    "en": {
        "title": "IP Lookup Pro",
        "search_placeholder": "Enter IP or Domain...",
        "check_my_ip": "My IP",
        "search": "Analyze",
        "settings": "Settings",
        "appearance": "App Theme",
        "language": "App Language",
        "theme": "Accent Color",
        "results": "IP Analysis Report",
        "ip_address": "IP Address",
        "org": "Provider (ISP)",
        "city": "City",
        "region": "Region / State",
        "country": "Country",
        "zip": "Zip Code",
        "timezone": "Timezone",
        "coords": "Geo Coordinates",
        "open_maps": "Show on Map",
        "error_conn": "Error: No Connection!",
        "error_invalid": "Error: Invalid IP!",
        "search_complete": "Analysis Finished.",
        "copy_success": "Copied!",
        "dark": "Dark", "light": "Light", "system": "System"
    }
}

class IPLookupApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set initial appearance BEFORE any widgets are created
        ctk.set_appearance_mode("dark")
        
        self.current_lang = "tr"
        self.current_theme = "Ocean Blue"
        
        self.title("IP Bulucu Pro")
        self.geometry("1150x800")
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.setup_ui()
        self.update_translations()
        self.apply_premium_theme()

    def setup_ui(self):
        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=280, corner_radius=0, fg_color=("gray95", "#0d0d0d"))
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_rowconfigure(10, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar, text="IP PRO", font=ctk.CTkFont(family="Inter", size=32, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=30, pady=(50, 40))

        # Controls
        self.lbl_app = ctk.CTkLabel(self.sidebar, text="Görünüm Modu", font=ctk.CTkFont(size=12, weight="bold"), text_color=("#444444", "#bbbbbb"))
        self.lbl_app.grid(row=1, column=0, padx=30, pady=(10, 5), sticky="w")
        self.appearance_menu = ctk.CTkOptionMenu(self.sidebar, values=["Dark", "Light", "System"], command=self.change_appearance, height=35)
        self.appearance_menu.grid(row=2, column=0, padx=30, pady=(0, 15), sticky="ew")
        self.appearance_menu.set("Dark")

        self.lbl_accent = ctk.CTkLabel(self.sidebar, text="Vurgu Rengi", font=ctk.CTkFont(size=12, weight="bold"), text_color=("#444444", "#bbbbbb"))
        self.lbl_accent.grid(row=3, column=0, padx=30, pady=(5, 5), sticky="w")
        self.theme_menu = ctk.CTkOptionMenu(self.sidebar, values=list(THEMES.keys()), command=self.change_theme, height=35)
        self.theme_menu.grid(row=4, column=0, padx=30, pady=(0, 15), sticky="ew")
        self.theme_menu.set("Ocean Blue")

        self.lbl_lang = ctk.CTkLabel(self.sidebar, text="Uygulama Dili", font=ctk.CTkFont(size=12, weight="bold"), text_color=("#444444", "#bbbbbb"))
        self.lbl_lang.grid(row=5, column=0, padx=30, pady=(5, 5), sticky="w")
        self.lang_menu = ctk.CTkOptionMenu(self.sidebar, values=["Türkçe", "English"], command=self.change_lang, height=35)
        self.lang_menu.grid(row=6, column=0, padx=30, pady=(0, 20), sticky="ew")
        self.lang_menu.set("Türkçe")

        # Main content
        self.main_content = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.main_content.grid(row=0, column=1, sticky="nsew", padx=30, pady=30)
        self.main_content.grid_columnconfigure(0, weight=1)

        # Search box
        self.search_frame = ctk.CTkFrame(self.main_content, fg_color="transparent")
        self.search_frame.grid(row=0, column=0, sticky="ew", pady=(0, 20))
        self.search_frame.grid_columnconfigure(0, weight=1)

        self.entry = ctk.CTkEntry(self.main_content, height=50, corner_radius=12, border_width=2) # Temporarily place in main_content for grid control
        self.entry.grid(row=0, column=0, padx=(0, 10), in_=self.search_frame, sticky="ew")

        self.search_btn = ctk.CTkButton(self.search_frame, text="Analiz", height=50, width=120, corner_radius=12, command=self.perform_search)
        self.search_btn.grid(row=0, column=1, padx=5)
        
        self.my_ip_btn = ctk.CTkButton(self.search_frame, text="Kendi IP'm", height=50, width=120, corner_radius=12, fg_color="transparent", border_width=2, command=self.check_self_ip)
        self.my_ip_btn.grid(row=0, column=2, padx=5)

        # Result title
        self.results_title = ctk.CTkLabel(self.main_content, text="Analysis", font=ctk.CTkFont(size=24, weight="bold"))
        self.results_title.grid(row=1, column=0, sticky="w", pady=(0, 15))

        # Cards (Standard Frame instead of Scrollable to avoid scrollbar)
        self.cards_container = ctk.CTkFrame(self.main_content, fg_color="transparent")
        self.cards_container.grid(row=2, column=0, sticky="nsew", pady=(0, 10))
        self.cards_container.grid_columnconfigure((0, 1, 2), weight=1)

        # Map Panel (Fixed clipping issues with identical radius and no border)
        current_mode = ctk.get_appearance_mode().lower()
        map_bg = "#ffffff" if current_mode == "light" else "#1a1a1a"
        map_fg = "#ebebeb" if current_mode == "light" else "#242424" # Slightly different for contrast if needed
        
        self.map_frame = ctk.CTkFrame(
            self.main_content,
            height=300,
            corner_radius=15,
            fg_color=map_bg,
            border_width=0
        )
        self.map_frame.grid(row=3, column=0, sticky="nsew", pady=(10, 0))
        self.main_content.grid_rowconfigure(3, weight=1)
        
        self.map_widget = tkintermapview.TkinterMapView(
            self.map_frame,
            corner_radius=0,   # ✅ ÇOK ÖNEMLİ
            bg_color=map_bg
        )
        self.map_widget.pack(fill="both", expand=True) # Removed padding to prevent edge bleed
        self.map_widget.set_zoom(12)



        self.info_widgets = {}
        fields = [("ip_address", "🌐"), ("org", "🏢"), ("city", "🏙️"), ("region", "📍"), ("country", "🌍"), ("zip", "📮"), ("timezone", "⏰"), ("coords", "🎯")]
        
        for i, (field, icon) in enumerate(fields):
            r, c = i // 3, i % 3
            card = ctk.CTkFrame(self.cards_container, corner_radius=15, fg_color=("white", "#161616"), border_width=1, border_color=("gray90", "gray20"))
            card.grid(row=r, column=c, padx=8, pady=8, sticky="ew")
            card.grid_columnconfigure(1, weight=1)
            
            ctk.CTkLabel(card, text=icon, font=ctk.CTkFont(size=26)).grid(row=0, column=0, rowspan=2, padx=15, pady=20)
            
            n_lbl = ctk.CTkLabel(card, text=field, font=ctk.CTkFont(size=11, weight="bold"), text_color=("#555555", "#888888"), anchor="w")
            n_lbl.grid(row=0, column=1, padx=(0, 15), pady=(15, 0), sticky="ew")
            
            v_lbl = ctk.CTkLabel(card, text="---", font=ctk.CTkFont(family="Inter", size=15, weight="bold"), wraplength=200, anchor="w", cursor="hand2")
            v_lbl.grid(row=1, column=1, padx=(0, 15), pady=(0, 15), sticky="ew")
            v_lbl.bind("<Button-1>", lambda e, text_to_copy=v_lbl: self.copy_to_clipboard(text_to_copy))
            
            self.info_widgets[field] = (n_lbl, v_lbl)

        # Footer actions
        self.footer = ctk.CTkFrame(self.main_content, fg_color="transparent")
        self.footer.grid(row=4, column=0, sticky="ew", pady=(10, 10))
        self.footer.grid_columnconfigure(0, weight=1)

        self.status_label = ctk.CTkLabel(self.footer, text="", font=ctk.CTkFont(size=13, weight="normal"))
        self.status_label.grid(row=0, column=0, sticky="w")


    def apply_premium_theme(self):
        colors = THEMES[self.current_theme]
        # Update search button
        self.search_btn.configure(fg_color=colors["main"], hover_color=colors["hover"], text_color=colors["text"])
        
        # Update My IP button (outline style)
        current_mode = ctk.get_appearance_mode().lower()
        self.my_ip_btn.configure(border_color=colors["main"], text_color=colors["main"] if current_mode == "light" else "white")
        
        # Update map frame and widget background to fix corner issues
        map_bg = "#ffffff" if current_mode == "light" else "#1a1a1a"
        self.map_frame.configure(fg_color=map_bg)
        
        # Deep update for map colors (Using standard 'bg' for canvas to fix corners)
        if hasattr(self.map_widget, 'canvas'):
            self.map_widget.canvas.configure(bg=map_bg, highlightthickness=0)
            
        # Update option menu colors
        for menu in [self.appearance_menu, self.theme_menu, self.lang_menu]:
            menu.configure(button_color=colors["main"], button_hover_color=colors["hover"])

    def change_theme(self, theme_name):
        self.current_theme = theme_name
        self.apply_premium_theme()

    def change_appearance(self, mode):
        ctk.set_appearance_mode(mode)
        # Re-apply theme colors to handle mode-specific adjustments
        self.apply_premium_theme()
        
    def copy_to_clipboard(self, label_widget):
        text = label_widget.cget("text")
        if text and text != "---":
            self.clipboard_clear()
            self.clipboard_append(text)
            self.update() # Required for some systems to finalize clipboard
            
            original_color = label_widget.cget("text_color")
            label_widget.configure(text_color="#27ae60")
            
            success_msg = LANGUAGES[self.current_lang]["copy_success"]
            self.status_label.configure(text=f"📋 {success_msg} ({text})", text_color="#27ae60")
            
            # Reset color after 1 second
            self.after(1000, lambda: label_widget.configure(text_color=original_color))

    def change_lang(self, lang):
        self.current_lang = "tr" if lang == "Türkçe" else "en"
        self.update_translations()

    def update_translations(self):
        t = LANGUAGES[self.current_lang]
        self.title(t["title"])
        self.lbl_app.configure(text=t["appearance"])
        self.lbl_accent.configure(text=t["theme"])
        self.lbl_lang.configure(text=t["language"])
        
        self.entry.configure(placeholder_text=t["search_placeholder"])
        self.search_btn.configure(text=t["search"])
        self.my_ip_btn.configure(text=t["check_my_ip"])
        self.results_title.configure(text=t["results"])
        
        for k, (n, v) in self.info_widgets.items():
            n.configure(text=t[k])

    def perform_search(self, target=""):
        q = target if target else self.entry.get()
        # Status text based on language
        self.status_label.configure(text="⌛ Analiz ediliyor..." if self.current_lang=="tr" else "⌛ Analyzing...", text_color="gray")
        
        def _thread():
            try:
                headers = {'User-Agent': 'Mozilla/5.0'}
                r = requests.get(f'http://ip-api.com/json/{q}', headers=headers, timeout=10)
                data = r.json()
                
                if data.get('status') == 'success':
                    self.after(0, lambda d=data: self.display_data(d))
                    success_msg = LANGUAGES[self.current_lang]["search_complete"]
                    self.after(0, lambda: self.status_label.configure(text=f"✅ {success_msg}", text_color="#27ae60"))
                else:
                    invalid_msg = LANGUAGES[self.current_lang]["error_invalid"]
                    self.after(0, lambda: self.status_label.configure(text=f"❌ {invalid_msg}", text_color="#e74c3c"))
            except Exception:
                conn_msg = LANGUAGES[self.current_lang]["error_conn"]
                self.after(0, lambda: self.status_label.configure(text=f"📡 {conn_msg}", text_color="#e74c3c"))

        threading.Thread(target=_thread, daemon=True).start()

    def check_self_ip(self):
        self.perform_search(target="") 

    def display_data(self, d):
        mapping = {
            "ip_address": "query", "org": "org", "city": "city", 
            "region": "regionName", "country": "country", "zip": "zip", 
            "timezone": "timezone"
        }
        for field, key in mapping.items():
            self.info_widgets[field][1].configure(text=d.get(key, "N/A"))
        
        coords = f"{d.get('lat')}, {d.get('lon')}"
        self.info_widgets["coords"][1].configure(text=coords)
        
        self.lat, self.lon = d.get('lat'), d.get('lon')
        
        # Update Map
        if self.lat and self.lon:
            self.map_widget.set_position(self.lat, self.lon)
            # Use theme main color for the marker
            colors = THEMES[self.current_theme]
            self.map_widget.set_marker(self.lat, self.lon, text=f"IP: {d.get('query')}", marker_color_circle=colors["main"], marker_color_outside=colors["hover"])
            self.map_widget.set_zoom(13)

    def open_google_maps(self):
        if hasattr(self, 'lat'):
            webbrowser.open(f"https://www.google.com/maps/place/{self.lat}+{self.lon}")

if __name__ == "__main__":
    app = IPLookupApp()
    app.mainloop()
