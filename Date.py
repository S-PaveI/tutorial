# Программа конвертирует дату из цифровой в словестную
def main():
    date = input('Введите дату в формате дд/мм/гггг ')
    re_date = date.replace('/', ' ')
    mouth = re_date[3:5]
    if mouth == '01':
        real_date = re_date.replace(re_date[3:5], 'январь')
    elif mouth == '02':
        real_date = re_date.replace(re_date[3:5], 'февраль')
    elif mouth == '03':
        real_date = re_date.replace(re_date[3:5], 'марта')
    elif mouth == '04':
        real_date = re_date.replace(re_date[3:5], 'апрель')
    elif mouth == '05':
        real_date = re_date.replace(re_date[3:5], 'май')
    elif mouth == '06':
        real_date = re_date.replace(re_date[3:5], 'июнь')
    elif mouth == '07':
        real_date = re_date.replace(re_date[3:5], 'июль')
    elif mouth == '08':
        real_date = re_date.replace(re_date[3:5], 'август')
    elif mouth == '09':
        real_date = re_date.replace(re_date[3:5], 'сентябрь')
    elif mouth == '10':
        real_date = re_date.replace(re_date[3:5], 'октябрь')
    elif mouth == '11':
        real_date = re_date.replace(re_date[3:5], 'ноябрь')
    elif mouth == '12':
        real_date = re_date.replace(re_date[3:5], 'декабрь')
    print(real_date + 'г.')


main()
