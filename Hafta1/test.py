
# !Easy: 
# *Kullanıcının doğum tarihini alarak kaç yaşında olduğunu bulan bir algoritma yazmanızı istiyorum.

# import datetime

# today = datetime.datetime.now()
# year = today.year

# birthyear = int(input("Doğum tarihinizi giriniz :"))
# age = year - birthyear
# print(f"Yaşınız : {age}")



# !Medium: 
# *Kullanıcıdan bir metin almanızı istiyorum. Bu metnin içindeki en çok tekrar eden harfi bulmalı ve 
# *kaç kere tekrar ettiğini göstermeli.

# text = input("Bir metin giriniz :")

# letterNumbers = {}
# for letter in text:
#     letterNumbers[letter] = text.count(letter)

# mostManyRepeatedLetter = max(letterNumbers, key=letterNumbers.get)
# mostManyRepeats = letterNumbers[mostManyRepeatedLetter]

# print(f"Girilen {text} metninde en çok tekrar edilen harf : {mostManyRepeatedLetter}\nTekrar sayısı: {mostManyRepeats}")



# !Hard: 
# *Bir tam sayı dizisi oluşturmanı istiyorum. Kullanıcıdan aldığın hedef sayı doğrultusunda sayı dizisinin 
# *içinden sayılar seçip toplayarak hedef sayıya ulaşmasını sağlamalısın. Farklı farklı kombinasyonlar ile 
# *hedef sayıya ulaşıyor olman burada çok önemli!

# numbers = []
# for i in range(100):
#     numbers.append(i)

# say = int(input("Hedef sayıyı giriniz :"))
# if say<=0:
#     say = int(input("Yanlış bir sayı girdiniz.0'dan büyük bir sayı giriniz :"))
#     for i in numbers:
#         say2 = say-numbers[i]
#         if say2 in numbers:
#             print(f"{numbers[i]} + {say2} = {say} ")
