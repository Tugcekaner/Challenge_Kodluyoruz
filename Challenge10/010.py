
# ! Easy: Bir futbol maçında 3 puanlık atışlarda 5 kez isabet edildi, 
# ! 2 puanlık atışlarda ise 10 kez isabet edildi. Toplam kaç puan elde edildi?

def point(twoPoint,threePoint):
    total = (twoPoint * 2) + (threePoint * 3)
    print(f'Maç puanı : {total}')

point(10,5)

# ! Medium:  Bir mağazada bir kitap 80 TL, bir defter 20 TL ve bir kalem 5 TL. 
# ! Bir müşteri 2 kitap, 3 defter ve 4 kalem aldı. Müşteri ne kadar ödeme yapmalı?

def price(book,notebook,pen):
    total = (book * 80) + (notebook * 20) + (pen * 5)
    print(f'Toplam tutar : {total}')

price(2,3,4)

# ! Hard: Bir sınıfta 30 öğrenci bulunmaktadır. Öğrencilerden kaç farklı şekilde 4 kişi seçilebilir?

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

total_students = 30
group_size = 4

different_ways = factorial(total_students) / (factorial(group_size) * factorial(total_students - group_size))

print("30 öğrenci içinde 4 kişi seçilebilecek farklı şekillerin sayısı:", int(different_ways))


