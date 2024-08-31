def add_everything_up(a,b):
    try:
         result = a + b
    except TypeError as exc:
        print(f'{str(a) + str(b)} - Разные типы! Причина ошибки: {exc}.')
    else:
        print(f'{str(a) + str(b)} - Одинаковые типы.')
    finally:
        print('Конец')



add_everything_up(123.456, 'строка')
add_everything_up('яблоко', 4215)
add_everything_up(123.456, 7)