class Müşteri:
    def __init__(self,Ad,Soyad,kartşifre,Hesapbakiye,KrediKartıBorcu,Sonödeme):
        self.Ad=Ad
        self.Soyad=Soyad
        self.kartşifre=kartşifre
        self.Hesapbakiye=Hesapbakiye
        self.KrediKartıBorcu=KrediKartıBorcu
        self.Sonödeme=Sonödeme

AhmetHesap=Müşteri("Ahmet","Akar","1752",14200,7400,27/9/2023)
MehmetHesap=Müşteri("Mehmet","Sakar","1453",12796,4538,18/7/2023)
TakılanKart=AhmetHesap


class ATM:
    def __init__(self,ATMad):
        self.ATMad=ATMad
        self.girişkontrol()
        self.döngü=True

    def girişkontrol(self):
        Hak=2
        for i in range (0,3):
            şifre=input("Lütfen 4 HANELİ şifrenizi giriniz!:")
            if şifre==TakılanKart.kartşifre:
                self.program()
            elif şifre!=TakılanKart.kartşifre and Hak!=0:
                  print("Kalan Hakkınız {} ,Lütfen Tekrar Deneyiniz..".format(Hak))
                  Hak-=1
                   
            elif şifre!=TakılanKart.kartşifre and Hak==0:
                print("Şifreyi 3 DEFA yanlış girdiğinizden dolayı kartınız bloke olmuştur..Lütfen En Yakın Şubemize Giderek Başvuru Yapınız..")
                exit()

    def program(self):
        seçim=self.menu()
        if seçim==1:
            self.bakiye()
        if seçim==2:
            self.kredikartıborcu()
        if seçim==3:
            self.paraçek()   
        if seçim==4:
            self.parayatır()
        if seçim==5:
            self.çıkış()    

    def menu(self):
        seçim=int(input("****Merhabalar Hoşgeldiniz {}'a Sayın {} {}.\n[1] Bakiye Sorgulama\n[2] Kredi Kartı Borcu Sorgulama\n[3] Para Çekme\n[4] Para Yatırma\n[5] Kart İade\n\n Seçim:"
                        .format(self.ATMad,TakılanKart.Ad,TakılanKart.Soyad)))
        if seçim<1 or seçim>5:
            print("\n\nLütfen Geçerli Bir İşlem Seçiniz.\Ana Menüye Dönülüyor..")
            self.program()
        else:
            return seçim
            

    def bakiye(self):
      print("Hesap Bakiyeniz: {}TL'dir.".format(TakılanKart.Hesapbakiye))
      self.döngü=False
      self.menuyedon()

    def kredikartıborcu(self):
        print("Kredi Kartı Borcunuz {}TL'dir Son Ödeme Tarihi {}..".format(TakılanKart.KrediKartıBorcu,TakılanKart.Sonödeme))
        self.döngü=False
        self.menuyedon()    

    def paraçek(self):
        miktar=int(input("""Lütfen Çekeceğiniz Tutarı Giriniz.."""))
        if miktar>TakılanKart.Hesapbakiye:
            print("""YETERSİZ BAKİYE""")
            self.menuyedon
        else:
            YeniMiktar=TakılanKart.Hesapbakiye-miktar
            print("Lütfen Paranızı Kontrol Ederek Alınız.. Hesabınınızda Kalan Tutar {}TL'dir..".format(YeniMiktar))
            self.menuyedon()

    def parayatır(self):
        miktar2=int(input("Lütfen Yatırılacak Tutarı Giriniz..."))
        Yenimiktar2=TakılanKart.Hesapbakiye+miktar2
        print("İşleminiz Başarıyla Gerçekleştirilmiştir.. Hesap Bakiyeniz {}".format(Yenimiktar2))
        self.menuyedon()
    def çıkış(self):
        print("Bankamızı Tercih Ettiğiniz İçin Teşekkür Ederiz..")
        self.çıkış()
        exit()
    def menuyedon(self):
        x=int(input("""Ana Menüye Dönmek için 7 Tuşuna Basınız.Kart İade İçin 5'e Basınız"""))
        if x==7:
            self.program()
        elif x==5:
            print("Bizi Tercih Ettiğiniz İçin Teşekkür Ederiz...")
            self.çıkış()
            

Banka=ATM("AYDINBANK")
while Banka.döngü:
    Banka.program()