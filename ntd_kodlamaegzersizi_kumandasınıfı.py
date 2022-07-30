import random
import time
import msvcrt

class Kumanda():

    def __init__(self,tv_durum="Kapalı",tv_ses=0,kanal_listesi=["TRT"],kanal="Trt"):
        print("Kumanda Oluşturuluyor...")
        self.tv_ses=tv_ses
        self.tv_durum=tv_durum
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal

    def sesi_azalt_artır(self):
        while True:
            karakter=input("Sesi Azaltmak için '<' Artırmak için '>' Çıkmak için 'q' ya basınız")
            if (karakter=="<"):
                if(self.tv_ses!=0):
                    self.tv_ses-=1
                    print("Ses:",self.tv_ses)
            elif(karakter==">"):
                if(self.tv_ses!=32):
                    self.tv_ses+=1
                    print("Ses:",self.tv_ses)
            else:
                print("Ses Güncellendi: ",self.tv_ses)
                break

    def tv_kapat(self):
        print("Tv kapatılıyor.")
        self.tv_durum="Kapalı"

    def tv_aç(self):
        print("Tv açılıyor.")
        self.tv_durum="Açık"

    def __str__(self):
        return "Tv durumu : {}\nSes: {} \nKanallar: {}\nMevcut kanal: {}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def rastgele_kanal(self):
        rastge=random.randint(0,len(self.kanal_listesi)-1)
        self.kanal=self.kanal_listesi[rastge]
        print("Şu anki kanal: ",self.kanal)

    def kanal_ekle(self,kanal):
        print("Kanal eklendi ",kanal)
        self.kanal_listesi.append(kanal)

kumanda=Kumanda()

print("""*******************

Kumanda Uygulması

İşlemler ;

1. Televizyonu Aç

2. Televizyonu Kapat

3. Televizyon Bilgileri

4. Kanal Sayısını Öğrenme

5. Kanal Ekle

6. Rastegele Kanal'a Geç

7.Sesi Artır/Azalt

8. Çıkış

*******************

""")

while True:
    işlem=input("İşlemi seçiniz:")
    if(işlem=="1"):
        kumanda.tv_aç()
    elif(işlem=="2"):
        kumanda.tv_kapat()
    elif(işlem=="3"):
        print(kumanda)
    elif(işlem=="4"):
        print("Kanal Sayısı: ",len(kumanda))
    elif(işlem=="5"):
        kanallar=input("Eklemek istediğiniz kanalları ',' ile ayırarak girin:")
        eklenecekler=kanallar.split(",")
        for i in eklenecekler:
            kumanda.kanal_ekle(i)
        print("Kanal listesi güncellendi..")

    elif(işlem=="6"):
        kumanda.rastgele_kanal()
    elif(işlem=="7"):
        kumanda.sesi_azalt_artır()
    else:
        print("Geçersiz işlem...")
        break






