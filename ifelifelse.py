age_student = int(input('Ваш возраст: '))
if age_student < 18:
    print('Ждём тебя в школе!')
elif age_student >= 18 and age_student <= 30:
    print('Иди в универ!')
elif age_student > 30 and age_student < 40:
    print('Иди работать!')
else:
    print('Тебе больше 40 лет!')
print('Конец.')
