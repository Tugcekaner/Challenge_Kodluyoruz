
# ! Easy: Kullanıcıdan aldığınız bir sayının faktöriyelini hesaplayan kod parçacığını yazmanızı istiyorum.

sayi = int(input('Bir sayı giriniz : '))

def faktor(a):
    fak = 1
    for i in range(1,a+1):
        fak = i * fak
    print(f'Girilen {a} sayısının faktöriyeli {fak}')

faktor(sayi)

# ! Medium:  Bir dizi oluşturup bu sayıların ortalamasını hesaplayan bir kod parçacığı yazar mısın?

sayilar = {1,2,3,4,5,6,7,8,9,10}

def ortalama(a):
    toplam = sum(a)
    ort = toplam / len(a)
    print(ort)

ortalama(sayilar)

# ! Hard :  Bir sıralanmış dizide (örneğin, artan sırada) hedef bir sayının kaç kez tekrar ettiğini bulan bir kod parçacığı yazar mısın?

def count_occurrences(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
        elif num > target:
            break
    return count

# Örnek kullanım:
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
target_number = 3

occurrence_count = count_occurrences(numbers, target_number)
print("Hedef sayı {} dizide {} kez tekrar etmiştir.".format(target_number, occurrence_count))

