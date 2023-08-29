
# ! Easy: Bir araba saatte 60 km hızla hareket ediyor. 
# ! Bu araba kaç saatte 240 km yol alır?

hiz = 60
uzaklik = 240 

def zaman(a,b):
    c = b/a
    print(f'{a} km hızla giden bir araç {b} km yolu {c} saatte alır.')

zaman(hiz,uzaklik)

# ! Medium:  Bir çiftlikte toplamda 36 baş tavuk ve koyun bulunmaktadır. Bu hayvanlardan toplamda 100 bacak çıkmaktadır.
# ! Çiftlikte kaçar tane tavuk ve koyun olduğunu bulan kod parçacığını yazar mısın?

def find_animals():
    for num_chickens in range(0, 37):
        num_legs_chickens = num_chickens * 2
        num_sheep = 36 - num_chickens
        num_legs_sheep = num_sheep * 4
        if num_legs_chickens + num_legs_sheep == 100: 
            return num_chickens, num_sheep 
    return None 

result = find_animals()
if result is not None:
    num_chickens, num_sheep = result
    print("Tavuk sayısı:", num_chickens)
    print("Koyun sayısı:", num_sheep)
else:
    print("Bu koşulları sağlayan bir kombinasyon bulunamadı.")

# ! hard : Hard: Bir yüzme havuzunda 2 adet su girişi, 1 adet su çıkışı vardır. İlk su girişi havuzu 10 saatte doldururken,
# ! ikinci su girişi havuzu 15 saatte doldurmaktadır. Havuzun kendiliğinden boşalma hızı ise 30 saatte bir doludur. 
# ! Eğer havuz boşken, her iki su girişi de açılırsa havuz ne kadar sürede dolar?

def calculate_pool_fill_time():
    first_inlet_rate = 1/10 
    second_inlet_rate = 1/15 
    empty_rate = 1/30 
    
    fill_rate = first_inlet_rate + second_inlet_rate - empty_rate
    
    fill_time = 1 / fill_rate

    return fill_time

time_to_fill = calculate_pool_fill_time()
print("Havuzun dolması {} saat sürer.".format(time_to_fill))