age_student = int(input('Ваш возраст: '))
if age_student < 18:
    print('Ждём тебя в школе!')
elif age_student >= 18 and age_student <= 30:
    print('Иди в универ!')
elif age_student > 30 and age_student < 40:
    print('Иди работать!')
    job_=input('Кем ты работаешь?')
    if job_ =='программист':
        print('Иди программировать!')
    else:
        print('Иди не знаю куда!')
else:
    print('Тебе больше 40 лет!')
print('Конец.')
