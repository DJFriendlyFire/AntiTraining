def check_age(age):
    if age < 18:
        raise ValueError('Вы должны быть старше 18 лет')
    print('Вы можете участвовать в соревновании')


check_age(15)
