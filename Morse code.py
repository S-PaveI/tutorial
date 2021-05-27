# Конвертирует слова в азбуку Морзе


def main():
    tt = ''
    text = input('Введите текст, который нужно перевести в азбуку морзе ')
    text = text.upper()
    for i in text:
        t = convert_text(i)
        tt += t
    print(tt)



def convert_text(i):
    if i == ' ':
        return 'пробел'
    elif i == ',':
        return '--..--'
    elif i == '.':
        return '.-.-.-'
    elif i == '?':
        return '..--..'
    elif i == '0':
        return '-----'
    elif i == '1':
        return '.----'
    elif i == '2':
        return '..---'
    elif i == '3':
        return '...--'
    elif i == '4':
        return '....-'
    elif i == '5':
        return '.....'
    elif i == '6':
        return '-....'
    elif i == '7':
        return '--...'
    elif i == '8':
        return '---..'
    elif i == '9':
        return '----.'
    elif i == 'A':
        return '.-'
    elif i == 'B':
        return '-...'
    elif i == 'C':
        return '-.-.'
    elif i == 'D':
        return '-..'
    elif i == 'E':
        return '.'
    elif i == 'F':
        return '..-.'
    elif i == 'G':
        return '--.'
    elif i == 'H':
        return '....'
    elif i == 'I':
        return '..'
    elif i == 'J':
        return '.---'
    elif i == 'K':
        return '-.-'
    elif i == 'L':
        return '.-..'
    elif i == 'M':
        return '--'
    elif i == 'N':
        return '-.'
    elif i == 'O':
        return '---'
    elif i == 'P':
        return '.--.'
    elif i == 'Q':
        return '--.-'
    elif i == 'R':
        return '.-.'
    elif i == 'S':
        return '...'
    elif i == 'T':
        return '-'
    elif i == 'U':
        return '..-'
    elif i == 'V':
        return '...-'
    elif i == 'W':
        return '.--'
    elif i == 'X':
        return '-..-'
    elif i == 'Y':
        return '-.-'
    elif i == 'Z':
        return '--..'
    elif i == 'А':
        return '.-'
    elif i == 'Б':
        return '-...'
    elif i == 'В':
        return '.--'
    elif i == 'Г':
        return '--.'
    elif i == 'Д':
        return '-..'
    elif i == 'Е' or i == 'Ё':
        return '.'
    elif i == 'Ж':
        return '...-'
    elif i == 'З':
        return '--..'
    elif i == 'И':
        return '..'
    elif i == 'Й':
        return '.---'
    elif i == 'К':
        return '-.-'
    elif i == 'Л':
        return '.-..'
    elif i == 'М':
        return '--'
    elif i == 'Н':
        return '-.'
    elif i == 'О':
        return '---'
    elif i == 'П':
        return '.--.'
    elif i == 'Р':
        return '.-.'
    elif i == 'С':
        return '...'
    elif i == 'Т':
        return '-'
    elif i == 'У':
        return '..-'
    elif i == 'Ф':
        return '..-.'
    elif i == 'Х':
        return '....'
    elif i == 'Ц':
        return '-.-.'
    elif i == 'Ч':
        return '---.'
    elif i == 'Ш':
        return '----'
    elif i == 'Щ':
        return '--.-'
    elif i == 'Ъ':
        return '.--.-.'
    elif i == 'Ы':
        return '-.--'
    elif i == 'Ь':
        return '-..-'
    elif i == 'Э':
        return '..-..'
    elif i == 'Ю':
        return '..--'
    elif i == 'Я':
        return '.-.-'


main()
