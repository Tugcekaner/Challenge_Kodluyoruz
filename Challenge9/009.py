
# ! Easy: Kullanıcıdan aldığın iki sayının toplamını ekrana yazdıran bir kod parçacığı yazar mısın?

say1 = int(input("1. sayıyı giriniz :"))
say2 = int(input("2. sayıyı giriniz :"))

def toplam(a,b):
    sonuc = a + b
    print(f'Girilen {a} ve {b} sayılarının toplamı : {sonuc}')

toplam(say1,say2)

# ! Medium:  Kullanıcıdan alınan bir metindeki kelime sayısını hesaplayan bir kod parçacığı yazar mısın?

text = input("Bir metin giriniz :")

count = 1
for i in range(0, len(text)):
    if text[i] == " ":
        count += 1

print(f'Girilen {text} metnindeki kelime sayısı {count}')

# ! Hard: Kullanıcının girdiği bir sayı karekökten çıkıyorsa çıktığı halini eğer çıkmıyorsa 
# ! karekökten tam olarak çıkmıyor hata mesajı veren kod parçacığını yazar mısın?

import math

say = int(input("Bir sayı giriniz : "))

def square(x):
    a = math.sqrt(x)
    if x == a*a:
        print(f'Girilen {x} sayısının karekökü : {a}')
    else:
        print(f'Girilen {x} sayısı karekökten tam olarak çıkmıyor.')

square(say)
