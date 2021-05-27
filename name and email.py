# This program create name and email or change dictionary
import pickle


LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def main():



    try:
        input_file = open('name-mail.dat', 'rb')
        email = pickle.load(input_file)
        input_file.close()
    except FileNotFoundError:
        email = {}


    choice = 0
    while choice != QUIT:
            choice = get_menu_choice()
            if choice == LOOK_UP:
                look_up(email)
            elif choice == ADD:
                add_email(email)
            elif choice == CHANGE:
                change_mail(email)
            elif choice == DELETE:
                delete_mail(email)

    output_file = open('name-mail.dat', 'wb')
    pickle.dump(email, output_file)
    output_file.close()



def get_menu_choice():
    print( 'МЕНЮ' )
    print( '-----' )
    print( '1. Найти адрес электронной почты' )
    print( '2. Добавить новое имя и адрес электронной почты' )
    print( '3. Изменить существующий адрес' )
    print( '4. Удалить имя и адрес' )
    print('5. Выход')
    choice = int(input('Выберете нужный пункт: '))
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Выберите нужный пунктЖ '))
    return choice


def look_up(email):
    name = input('Введите имя: ')
    print(email.get(name, 'Не найдено'))


def add_email(email):
    name = input('Введите имя: ')
    mail = input('Введите электронную почту: ')
    if name not in email:
        email[name] = mail
    else:
        print('Имя уже есть в списке')


def change_mail(email):
    name = input('Введите имя, которое хотите изменить: ')
    if name in email:
        mail = input('Введите новый адрес электронной почты: ')
        email[name] = mail
    else:
        print('Имя не найдено')


def delete_mail(email):
    name = input('Введие имя которое хотите удалить: ')
    if name in email:
        del email[name]
    else:
        print('Имя не найдено')


main()
