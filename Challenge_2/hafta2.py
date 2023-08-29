
# !Easy: 
# *Kullanıcıdan bir sayı almanızı ve bu sayının asal olup olmadığını kullanıcıya söylemenizi istiyorum. 


say = int(input("Lütfen bir sayı giriniz : "))

bolenSayisi = 0

for i in range(1,say):
    if say%i==0:
        bolenSayisi += 1 

if bolenSayisi!=1:
    print(f'Girilen {say} sayısı asal değildir.')
else:
    print(f'Girilen {say} sayısı asaldır.')
    

# !Medium: 
# *Kullanıcıdan bir kelime almanız gerekiyor. Bu kelimenin harflerini büyük harflere 
# *dönüştüren bir program yazmanızı istiyorum. 


text = input("Bir metin giriniz : ")

def upper(a):
    b = a.upper()
    print(b)

upper(text)


# !Hard: 
# *Bir şirket, bir ürünü üretmek ve satmak için belirli bir maliyet ve satış fiyatı hesaplamaktadır. 
# *Şirketin bir ürün için birim maliyeti ve birim satış fiyatı verildiğinde, kaç adet ürünün satılması durumunda 
# *şirketin kar edeceğini bulmanı istiyorum. 


def kar():
    fark = fiyat - urunMaliyet
    adet = (urunMaliyet/fark)+1
    if adet>0:
        print(f'Kar elde edebilmek için en az {int(adet)} ürün satışı yapmalısınız.')
    else:
        print("Bu şekilde kar elde edemezsiniz.")

urunMaliyet = 0
secim1 = int(input("Ürün maliyetini hesaplamak için 1, maliyeti kendiniz belirlemek için 2 yazınız : "))
if secim1 ==1:
    asgari = 11000
    a = int(input("Günde kaç adet ürün üretildiğini giriniz : "))
    b = int(input("Çalışan işçi sayısını giriniz : "))
    c = int(input("Günlük çalışma saatini giriniz : "))
    d = int(input("Ürün aylık hammadde alış fiyatını giriniz : "))
    e = int(input("Ayda çalışılan gün sayısını giriniz : ")) 
    aylikMaliyet = ((b*asgari)/(c*e))+(d/(a*e))
    gunlukMaliyet = aylikMaliyet/e
    urunMaliyet = round((gunlukMaliyet / a),2)
    print(f'Ürün maliyeti : {urunMaliyet}')
elif secim1 ==2:
    urunMaliyet = int(input("Ürün maliyetini giriniz : "))
else:
    print("Hatalı giriş yaptınız!")

if urunMaliyet != 0:
    secim2 = int(input("Ürün satış fiyatını hesaplamak için 1, fiyatı kendiniz belirlemek için 2 yazınız : "))
    if secim2 ==1:
        karOran = int(input("Elde etmek istediğiniz kar oranını giriniz : "))
        fiyat = urunMaliyet+((urunMaliyet/100)*karOran)
        print(f'Ürün satış fiyatı : {fiyat}')
        kar()
    elif secim2 ==2:
        fiyat = int(input("Ürün fiyatını giriniz : "))
        kar()
        if fiyat<urunMaliyet:
            print("Fiyat ürün maliyetinden düşük olamaz!")
    else:
        print("Hatalı giriş yaptınız!")


