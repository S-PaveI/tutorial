# Программа определяет по номеру курса
# время аудиторию и преподавателя
# на конкретнм примере, можно переделать под свои данные


def main():
    number_aud = {'CS101': 3004, 'CS102': 4501, 'CS103': 6755,
                  'CS104': 1244, 'CS105': 1411}

    name_teacher = {'CS101': 'Haynes', 'CS102': 'Alvarado', 'CS103': 'Rich',
                  'CS104': 'Berg', 'CS105': 'Li'}

    time = {'CS101': '8:00', 'CS102': '9:00', 'CS103': '10:00',
                  'CS104': '11:00', 'CS105': '13:00'}

    number_cours = input('Press number course: ')
    print('Your audience:', number_aud[number_cours])
    print('Your time lesson:', time[number_cours])
    print('Your teacher:', name_teacher[number_cours])


main()
