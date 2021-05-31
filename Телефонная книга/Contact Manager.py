import Contact
import pickle


# Глобальные константы
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Глобальная константа для имени файла
FILENAME = 'contacts.dat'

# Главная функция


def main():
    #  Загрузить имеющийся список контактов
    mycontacts = load_contacts()
    # Переменная выбора пользователя
    choice = 0
    while choice != QUIT:
        choice = get_menu()
        if choice == LOOK_UP:
            look_up(mycontacts)
        elif choice == ADD:
            add(mycontacts)
        elif choice == CHANGE:
            change(mycontacts)
        elif choice == DELETE:
            delete(mycontacts)
    save_contacts(mycontacts)


def load_contacts():
    try:
        input_file = open(FILENAME, 'rb')
        contact_dct = pickle.load(input_file)
        input_file.close()
    except IOError:
        contact_dct = {}

    return contact_dct


def get_menu():
    print()
    print('Меню')
    print('--------------------')
    print('1. Найти контиктное лицо')
    print("2. Добавить новй контакт")
    print("3. Изменть существующий контакт")
    print("4. Удалить контакт")
    print("5. Выйти из программы")
    print()

    choice = int(input('Введите выбранный пункт: '))
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Введите выбранный пункт: '))

    return choice


def look_up(mycontacts):
    name = input('Введите имя: ')
    print(mycontacts.get(name, 'Это имя не найдено'))


def add(mycontacts):
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    email = input('Введите адрес элеткронной почты: ')

    entry = Contact.Contact(name, phone, email)

    if name not in mycontacts:
        mycontacts[name] = entry
    else:
        print('Это имя уже существует')


def change(mycontacts):
    name = input('Введите имя: ')
    if name in mycontacts:
        phone = input('Введите номер телефона: ')
        email = input('Введите адрес элеткронной почты: ')
        emtry = Contact.Contact(name, phone, email)
        mycontacts[name] = emtry
        print('Информация обновлена')
    else:
        print("Имя не найдено")


def delete(mycontacts):
    name = input('Введите имя: ')
    if name in mycontacts:
        del mycontacts[name]
        print('Запись удалена')
    else:
        print('Имя не найдено')


def save_contacts(mycontact):
    output = open(FILENAME, 'wb')
    pickle.dump(mycontact, output)
    output.close()


main()
