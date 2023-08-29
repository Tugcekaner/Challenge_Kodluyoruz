
# ! Easy: Kullanıcıdan aldığınız sayının tek mi çift mi olduğunu ekrana yazdıran bir kod parçacığı yazar mısın?

say = int(input("Bir sayı giriniz :"))

if(say%2==0):
    print(f'Girilen {say} sayısı çift sayıdır.')
else:
    print(f'Girilen {say} sayısı tek sayıdır.')

# ! Medium: Bir dizi oluşturup içindeki çift sayıların toplamını hesaplayan bir kod parçacığı yazar mısınız?

nums = [1,84,57,62,15,34,92,51]

def toplam(a):
    sonuc = 0
    for i in range(0, len(a)):
        if a[i]%2==0:
            sonuc += a[i]
    print(sonuc)

toplam(nums)

# ! Hard: Kullanıcıdan bir cümle girmesini ve bu cümlenin içinde ikileme olup olmadığını bulan bir kod parçası yazmanızı istiyorum.
# ! (Not: burada ikilemeleri sadece arka arkaya yazılmış aynı kelimeler olarak düşünmenizi istiyorum.)

def check_for_repetition(sentence):
    words = sentence.lower().split()
    for i in range(len(words) - 1): 
        if words[i] == words[i + 1]: 
            return True
    return False

user_sentence = input("Bir cümle girin: ")

if check_for_repetition(user_sentence):
    print("Cümlede ikileme bulunuyor.")
else:
    print("Cümlede ikileme bulunmuyor.")