# Эта программа содержит данные (название производителя, номер
# модели, розничная стимость) о телефонах
# количество которых задает пользователь

import cellphone


def main():
    n = int(input('Введите кол-во телефонов, которое хотите ввести: '))
    phones = make_list(n)

    print('Вот введенные вами данные')
    print('_________________________')
    display_list(phones)


def make_list(n):
    phone_list = []
    for count in range(1, n+1):
        man = input('Введите производителя: ')
        mod = input('Введите номер модели: ')
        retail = float(input('Введите розничную цену: '))
        print()
        phone = cellphone.CellPhone(man, mod, retail)
        phone_list.append(phone)
    return phone_list


def display_list(phones):
    for item in phones:
        print('Производитель:', item.get_manufact())
        print('Номер модели:', item.get_model())
        print('Розничная цена:', format(item.get_retail_price(), ',.2f'), 'руб.', sep='')
        print()


main()
