
# ! Easy: Bir kutuda 5 kırmızı, 4 yeşil ve 3 mavi top bulunuyor. 
# ! Kutudan rastgele çekilen 2 topun aynı renk olma olasılığı nedir?

def probability_same_color(total_red, total_green, total_blue, total_draws):
    total_balls = total_red + total_green + total_blue

    probability = (total_red / total_balls) * ((total_red - 1) / (total_balls - 1))
    probability += (total_green / total_balls) * ((total_green - 1) / (total_balls - 1))
    probability += (total_blue / total_balls) * ((total_blue - 1) / (total_balls - 1))

    return probability

total_red_balls = 5
total_green_balls = 4
total_blue_balls = 3

total_draws = 2

probability = probability_same_color(total_red_balls, total_green_balls, total_blue_balls, total_draws)

print("İki topun aynı renkte olma olasılığı:", probability)

# ! Medium:  Bir öğrenci kitap okuma hedefi olarak yılda 36 kitap okumayı belirledi. 
# ! Eğer her ay eşit sayıda kitap okursa kaç kitap okumuş olur?

def read(book):
    monthly_book = book / 12
    print(f'Her ay okuması gereken kitap : {monthly_book}')

read(36)

# ! Hard: Bir yarış pistinde iki yarışmacı aynı anda start alıyor. İlk yarışmacı saatte 15 km hızla, 
# ! ikinci yarışmacı ise saatte 20 km hızla koşuyor. İkinci yarışmacı kaç saat sonra ilk yarışmacıyı yakalar?


def catch_up_time(first_speed, second_speed):
    relative_speed = second_speed - first_speed
    time_to_catch = 0

    if relative_speed <= 0:
        return None 

    time_to_catch = 0
    while True:
        distance_covered_by_second = second_speed * time_to_catch
        distance_covered_by_first = first_speed * time_to_catch
        if distance_covered_by_second >= distance_covered_by_first:
            break
        time_to_catch += 1

    return time_to_catch

first_runner_speed = 15
second_runner_speed = 20 
time_to_catch = catch_up_time(first_runner_speed, second_runner_speed)

if time_to_catch is not None:
    print(f"Ikinci yarışmacı birinci yarışmacıyı {time_to_catch} saat sonra yakalar.")
else:
    print("İkinci yarışmacı birinci yarışmacıyı yakalayamaz.")