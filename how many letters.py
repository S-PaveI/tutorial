# Эта программа рассчитает сколько глассных и согласных в строковой последовательности


def main():
    text = input('Введите предложение: ')
    print('В этой строке', how_vowels(text), 'гласных')
    print('В этой строке', how_consonans(text), 'согласных')


def how_vowels(t):
    t = t.lower()
    total = 0
    for i in t:
        if i == 'а' or i == 'е' or i == 'и' or i== 'у' or i == 'ы':
            total += 1
        elif i == 'о' or i == 'э' or i == 'я' or i == 'ю' or i == 'й':
            total += 1
    return total


def how_consonans(t):
    t = t .lower()
    total = 0
    for i in t:
        if i == 'ц' or i == 'к' or i == 'н' or i == 'г' or i == 'ш' or i == 'щ':
            total += 1
        elif i == 'з' or i == 'х' or i == 'ф' or i == 'в' or i == 'п' or i == 'р' or i == 'б':
            total += 1
        elif i == 'л' or i == 'д' or i == 'ж' or i == 'ч' or i == 'с' or i == 'м' or i == 'т':
            total += 1
    return total


main()
