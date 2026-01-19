# IP Lookup Pro

**IP Lookup Pro**, Python ve CustomTkinter ile oluşturulmuş modern, avangart bir IP adresi analiz aracıdır. Premium, ultra duyarlı bir kullanıcı arayüzü içinde ayrıntılı coğrafi konum verileri, İSS bilgileri ve etkileşimli harita görselleştirmesi sunar.

## Özellikler

- **Derin Analiz**: İSS, Şehir, Bölge, Posta Kodu, Saat Dilimi ve Koordinatlar dahil olmak üzere ayrıntılı bilgi edinin.
- **Etkileşimli Harita**: IP/Alan adının tam konumunu görselleştirmek için gömülü harita görünümü.
- **Avangart Tasarım**: "Kasıtlı Minimalizm" tasarım felsefesine sahip şık, modern bir arayüz.
- **Premium Temalar**: Okyanus Mavisi, Zümrüt, Gül Pembesi, Mor Yağmur ve Siberpunk gibi özenle hazırlanmış temalar arasında geçiş yapın.
- **Çoklu Dil Desteği**: Tam Türkçe ve İngilizce dil desteği.
- **Kopyala & Git**: Tüm veri alanları için tek tıkla kopyalama işlevi.

## Kurulum / Kaynaktan Çalıştırma

1.  **Depoyu klonlayın**:

    ```bash
    git clone https://github.com/Memati8383/ip_tracer.git
    cd ip_tracer
    ```

2.  **Bağımlılıkları yükleyin**:

    ```bash
    pip install -r requirements.txt
    ```

3.  **Uygulamayı çalıştırın**:
    ```bash
    python main.py
    ```

## Çalıştırılabilir Dosya Oluştur (Windows)

Bağımsız bir `.exe` dosyası oluşturmak için:

```bash
pyinstaller --noconfirm --onefile --windowed --clean --icon=icon.ico --name "IPLookupPro" main.py
```

Çalıştırılabilir dosya `dist/` klasöründe bulunacaktır.

## Teknolojiler

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- [TkinterMapView](https://github.com/TomSchimansky/TkinterMapView)
- Requests & IP-API
- Pillow (PIL)

## Lisans

MIT Lisansı.
