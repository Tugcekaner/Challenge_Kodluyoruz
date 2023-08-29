
# ! Easy: Bir dizi tanımladıktan sonra bu dizinin içinden en büyük sayıyı bulan kod parçacığını yazar mısın?

def find_max_number(arr):
    max_number = arr[0] 
    for num in arr:
        if num > max_number:
            max_number = num
    return max_number


numbers = [12, 45, 78, 34, 56, 23]

max_num = find_max_number(numbers)
print("Dizinin en büyük sayısı: ", max_num)

# ! Medium:  Bir dizi oluşturup içindeki sayıların en büyük ve en küçük değerlerini bulan ve ekrana yazdıran bir kod parçacığı yazar mısınız?

def find_min_and_max(arr):
    min_number = arr[0] 
    max_number = arr[0] 

    for num in arr:
        if num < min_number:
            min_number = num
        if num > max_number:
            max_number = num

    return min_number, max_number

numbers = [12, 45, 78, 34, 56, 23]

min_num, max_num = find_min_and_max(numbers)
print("Dizinin en küçük sayısı: ", min_num)
print("Dizinin en büyük sayısı: ", max_num)

# ! Hard: Kullanıcının girdiği bir sayının tam bölenlerinin toplamını hesaplayan bir kod parçacığı yazınız.

sayi = int(input("Bir sayı giriniz : "))

def bolen(a):
    toplam = 0
    for i in range(2,a):
        if a % i == 0:
            toplam += i
    print(f'Girilen {a} sayısının tam bölenlerinin toplamı : {toplam}')

bolen(sayi)
