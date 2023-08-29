
# ! Easy : Kullanıcıdan aldığın sayının karesini hesaplayarak ekrana yazdıran kod parçacığını yazar mısın?

# sayi = int(input('Bir sayı giriniz : '))

# sonuc = sayi**2
# print(f"Girilen {sayi} sayısının karesi : {sonuc}")

# ! Medium:  Oluşturduğunuz bir dizinin medyanını hesaplayan bir kod parçacığı yazar mısınız?

# def median(nums):
#     sorted_nums = sorted(nums)
#     n = len(sorted_nums)
    
#     if n % 2 == 0:
#         middle_right = n // 2
#         middle_left = middle_right - 1
#         result = (sorted_nums[middle_left] + sorted_nums[middle_right]) / 2
#     else:
#         middle = n // 2
#         result = sorted_nums[middle]
#     return result

# array = [1, 3, 5, 7, 9, 2, 4, 6, 8]
# array_median = median(array)
# print("Dizi medyanı:", array_median)

# ! hard :  Kullanıcıdan aldığınız bir sayının Armstrong sayısı olup olmadığını kontrol eden bir kod parçacığı yazar mısınız?

# def is_armstrong_number(num):
#     num_str = str(num)
#     num_digits = len(num_str)
    
#     armstrong_sum = 0
#     for digit in num_str:
#         armstrong_sum += int(digit) ** num_digits
    
#     if armstrong_sum == num:
#         return True
#     else:
#         return False

# num = int(input("Bir sayı girin: "))
# if is_armstrong_number(num):
#     print(num, "bir Armstrong sayısıdır.")
# else:
#     print(num, "bir Armstrong sayısı değildir.")