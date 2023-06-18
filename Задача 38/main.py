def print_records(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            print(*line.split(';'), end='')


def input_records(file_name: str):
    with open(file_name, 'r+', encoding='utf-8') as data:
        record_id = 0
        for line in data:
            if line != '':
                record_id = line.split(';', 1)[0]
        print('Введите ФИО и телефон через пробел')
        line = f'{int(record_id) + 1};' + ';'.join(input().split()[:4]) + ';\n'
        confirm = confirmation('добавление записи')
        if confirm == 'y':
            data.write(line)


def find_char():
    print('Выберите параметр:')
    print('0 - № п/п, 1 - фамилия, 2 - имя, 3 - отчество, 4 - телефон, e - выйти')
    char = input()
    while char not in ('0', '1', '2', '3', '4', 'e'):
        print('Введены неверные данные')
        print('Выберите параметр:')
        print("0 - № п/п, 1 - фамилия, 2 - имя, 3 - отчество, 4 - телефон, e - выйти")
        char = input()
    if char != 'e':
        inp = input('Введите значение\n')
        return char, inp
    else:
        return 'e', 'e'


def find_records(file_name: str, char, condition):
    if condition != 'e':
        printed = False
        with open(file_name, 'r', encoding='utf-8') as data:
            for line in data:
                if condition == line.split(';')[int(char)]:
                    print(*line.split(';'))
                    printed = True
        if not printed:
            print("Не найдено")
        return printed


def check_id_record(file_name: str, text: str):
    decision = input(
        f'Вы знаете № п/п записи которую хотите {text}? 1 - да, 2 - нет, e - выйти\n')
    while decision not in ('1', 'e'):
        if decision != '2':
            print('Введены неверные данные')
        else:
            find_records(path, *find_char())
        decision = input(
            f'Вы знаете № п/п записи которую хотите {text}? 1 - да, 2 - нет, e - выйти\n')
    if decision == '1':
        record_id = input('Введите № п/п, e - выйти\n')
        while not find_records(file_name, '0', record_id) and record_id != 'e':
            record_id = input('Введите № п/п, e - выйти\n')
        return record_id
    return decision


def confirmation(text: str):
    confirm = input(
        f"Подтвердите ввод {text} записи: y - да, n - нет\n")
    while confirm not in ('y', 'n'):
        print('Введены неверные данные')
        confirm = input(
            f"Подтвердите ввод {text} записи: y - да, n - нет\n")
    return confirm


def replace_record_line(file_name: str, record_id, replaced_line: str):
    replaced = ''
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            replaced += line
            if record_id == line.split(';', 1)[0]:
                replaced = replaced.replace(line, replaced_line)
    with open(file_name, 'w', encoding='utf-8') as data:
        data.write(replaced)


def change_records(file_name: str):
    record_id = check_id_record(file_name, 'изменить')
    if record_id != 'e':
        replaced_line = f'{int(record_id)};' + ';'.join(
            input('Введите ФИО и телефон через пробел\n').split()[:4]) + ';\n'
        confirm = confirmation('изменение')
        if confirm == 'y':
            replace_record_line(file_name, record_id, replaced_line)


def delete_records(file_name: str):
    record_id = check_id_record(file_name, 'удалить')
    if record_id != 'e':
        confirm = confirmation('удаление')
        if confirm == 'y':
            replace_record_line(file_name, record_id, '')

path = 'directory.txt'
try:                        
    file = open(path, 'r')  
except IOError:             
    print('Создан новый справочник -> directory.txt ')
    file = open(path, 'w')
finally:
    file.close()

actions = {'1': 'показать весь список',
           '2': 'добавить новую запись',
           '3': 'поиск по справочнику',
           '4': 'изменение данных',
           '5': 'удаление данных',
           'e': 'выход'}

action = None
while action != 'e':
    print('Выберете действие',
          *[f'{i} - {actions[i]}' for i in actions])
    action = input()
    while action not in actions:
        print('Выберете действие',
              *[f'{i} - {actions[i]}' for i in actions])
        action = input()
        if action not in actions:
            print('Введены неверные данные')
    if action != 'e':
        if action == '1':
            print_records(path)
        elif action == '2':
            input_records(path)
        elif action == '3':
            find_records(path, *find_char())
        elif action == '4':
            change_records(path)
        elif action == '5':
            delete_records(path)