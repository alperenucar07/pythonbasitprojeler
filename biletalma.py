print("Bilet alma servisimize hoşgeldiniz.")
gun=int(input("Hafta içi almak için 1, Hafta sonu almak için 2 tuşlayınız: "))
servisbedeli=10
ogrencisayisi=1
if (gun==1) :
    biletparasi=50
else: biletparasi=60
geneltoplam=ogrencisayisi*biletparasi+servisbedeli
print("Bilet : ",biletparasi)
print("Bilet alma servisi bedeli: ",servisbedeli)
print("Toplam :",str(geneltoplam))