
# !  Easy: Kullanıcıdan alınan bir kelimenin uzunluğunu hesaplayan bir kod parçacığı yazar mısın?

text = input('Bir metin giriniz :')

a = len(text)
print(f'Girilen {text} metninin uzunluğu : {a}')

# ! Medium:  Kullanıcıdan aldığınız bir sayının basamaklarının toplamını hesaplayan bir kod parçacığı yazar mısın?

say = input('Bir sayı giriniz :')

toplam = 0
for i in range(0, len(say)):
    a = int(say[i])
    toplam += a

print(toplam)

# ! Hard: Kullanıcıdan aldığınız bir metnin içindeki sesli harfleri sayan ve bunu kullanıcıya geri dönen bir kod parçacığı yazar mısın?
def count_vowels(text):
    vowels = 'aeiouAEIOU'
    vowel_count = 0

    for char in text:
        if char in vowels:
            vowel_count += 1

    return vowel_count

user_text = input("Metin girin: ")

vowel_count = count_vowels(user_text)
print("Metin içindeki sesli harf sayısı:", vowel_count)
