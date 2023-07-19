
# !Easy: 
# *Kullanıcının doğum tarihini alarak kaç yaşında olduğunu bulan bir algoritma yazmanızı istiyorum.


import datetime

today = datetime.datetime.now()
year = today.year

birthyear = int(input("Doğum tarihinizi giriniz :"))
age = year - birthyear
print(f"Yaşınız : {age}")


# !Medium: 
# *Kullanıcıdan bir metin almanızı istiyorum. Bu metnin içindeki en çok tekrar eden harfi bulmalı ve 
# *kaç kere tekrar ettiğini göstermeli.


text = input("Bir metin giriniz :")

letterNumbers = {}
for letter in text:
    letterNumbers[letter] = text.count(letter)

mostManyRepeatedLetter = max(letterNumbers, key=letterNumbers.get)
mostManyRepeats = letterNumbers[mostManyRepeatedLetter]

print(f"Girilen {text} metninde en çok tekrar edilen harf : {mostManyRepeatedLetter}\nTekrar sayısı: {mostManyRepeats}")


# !Hard: 
# *Bir tam sayı dizisi oluşturmanı istiyorum. Kullanıcıdan aldığın hedef sayı doğrultusunda sayı dizisinin 
# *içinden sayılar seçip toplayarak hedef sayıya ulaşmasını sağlamalısın. Farklı farklı kombinasyonlar ile 
# *hedef sayıya ulaşıyor olman burada çok önemli!


def hedefSayiyaUlas(sayilar, index, hedef, secilmis):
    if hedef == 0:
        kombinasyon = " + ".join(map(str, secilmis))
        print("Hedef sayıya ulaşan kombinasyon: {} = {}".format(kombinasyon, hedefSayi))
        return

    if index >= len(sayilar) or hedef < 0:
        return

    hedefSayiyaUlas(sayilar, index + 1, hedef, secilmis)

    secilmis.append(sayilar[index])
    hedefSayiyaUlas(sayilar, index + 1, hedef - sayilar[index], secilmis)
    secilmis.pop()

sayilar = list(range(1, 101))

hedefSayi = int(input("Hedef sayıyı giriniz: "))

if hedefSayi <= 0:
    print("Girilen sayı 0'dan büyük olmalı.")
else:
    hedefSayiyaUlas(sayilar, 0, hedefSayi, [])
