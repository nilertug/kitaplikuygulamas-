class MenuSistemi:
    yeni_kitap = []

    @staticmethod
    def karsilama(program_adi):
        print(f"{program_adi} programına hoş geldiniz!\n")

    @staticmethod
    def kitap_ekle():
        k_adi = input("Kitabın ismini giriniz: ")
        k_yazar = input("Kitabın yazarını giriniz: ")
        k_tur = input("Kitabın türünü giriniz: ")
        kitap = f"{k_adi} - {k_yazar} - {k_tur}"
        MenuSistemi.yeni_kitap.append(kitap)
        print("Kitap eklendi:", kitap, "\n")

    @staticmethod
    def kitap_ara():
        arama = input("Kitap aramak için kelime girin: ")
        bulundu = False
        for satir in MenuSistemi.yeni_kitap:
            if arama.lower() in satir.lower():
                print("Kitap mevcut:", satir)
                bulundu = True
        if not bulundu:
            print("Aradığınız kitap yok.\n")

    @staticmethod
    def cikis_yap():
        print("Çıkış yapılıyor...")
        exit()

    @staticmethod
    def menu_calistir():
        menu = {
            "1": MenuSistemi.kitap_ekle,
            "2": MenuSistemi.kitap_ara,
            "3": MenuSistemi.cikis_yap
        }
        while True:
            print("Menü:")
            print("1 - Kitap ekle")
            print("2 - Kitap ara")
            print("3 - Çıkış\n")
            secim = input("Lütfen yapmak istediğiniz işlemin numarasını yazınız: ")
            if secim in menu:
                menu[secim]()
            else:
                print("Geçersiz seçim. Tekrar deneyin.\n")
if __name__ == "__main__":
    MenuSistemi.karsilama("KİTAPLIK UYGULAMASI")
    MenuSistemi.menu_calistir()