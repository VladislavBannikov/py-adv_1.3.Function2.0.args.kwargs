from pprint import pprint
import os
from phonebook import PhoneBook


def adv_print(*args, **kwargs):
    """ Advanced print
    :param string to print
    :param start - с чего начинается вывод. По умолчанию пустая строка;
    :param max_line - максимальная длин строки при выводе. Если строка превышает max_line, то вывод автоматически переносится на новую строку;
    :param in_file - аргумент, определяющий будет ли записан вывод ещё и в файл. (путь к файлу)
    """
    line = ' '.join(args)
    if kwargs.get('start'):
        line = kwargs.get('start') + line

    if kwargs.get('max_line'):
        maxx = int(kwargs.get('max_line'))
        if len(line) > maxx:
            tmp_line = line[:maxx] + os.linesep
            line = line[kwargs.get('max_line'):]
            while len(line) > int(kwargs.get('max_line')):
                tmp_line += line[:kwargs.get('max_line')] + os.linesep
                line = line[kwargs.get('max_line'):]
            line = tmp_line + line

    if kwargs.get('in_file'):
        try:
            with open(kwargs.get('in_file'),'w', encoding="utf-8",newline='') as f:
                f.write(line)
        except IOError as e:
            print(e)
    print(line)

info_message = '''p - Вывод контактов из телефонной книги;
a - Добавление нового контакта;
d - Удаление контакта по номеру телефона;
f - Поиск всех избранных номеров;
s - Поиск контакта по имени и фамилии.
q - for exit
'''
cmd_list = ["p", "s", "a", "q", "d", "f"]

if __name__ == "__main__":
    book = PhoneBook('personal book')

    # populate the book with test data
    for i in range(10):
        book.add_contact('Jhon'+str(i), 'Smith', '+71234567809'+str(i),favorite_contact=False, telegram='@jhony', email='jhony@smith.com')

    book.add_contact('Jhon_fav', 'Smith', '+712345678090', favorite_contact=book.find_contact('Jhon2', 'Smith'), telegram='@jhony',
                     email='jhony@smith.com')
    book.add_contact('Jhon_fav2', 'Smith', '+712345671090', favorite_contact=book.find_contact('Jhon3', 'Smith'),
                     telegram='@jhony',
                     email='jhony@smith.com')

    print(info_message)
    while True:
        cmd = input("Выберите действие:\n").lower()
        if cmd in cmd_list:
            if cmd == 'q':
                exit(0)
            elif cmd == 'p':
                book.print_contacts()
            elif cmd == 's':
                firstname = input("Введите имя:\n")
                lastname = input("Введите фамилию:\n")
                print(book.find_contact(firstname, lastname))
            elif cmd == 'a':
                firstname = input("Введите имя:\n")
                lastname = input("Введите фамилию:\n")
                phone_number = input("Введите номер:\n")
                fav_contact_id = input("Введите любимый контакт по номеру в списке или Enter для пропуска:\n")
                if fav_contact_id:
                    fav_contact = book.find_contact_by_id(fav_contact_id)
                    if not fav_contact:
                        print("Любимый контакт не найдет. Продолжение работы.")

                print('Введите дополнительную информацию в формате "key=value" или Enter для пропуска:\n')
                additional_info = dict()
                while True:
                    v = input("Введите дополнительную информацию :\n").strip()
                    if v == '':
                        break
                    else:
                        additional_info.update([tuple(v.split('='))])
                book.add_contact(firstname,lastname, phone_number, fav_contact,**additional_info)
            elif cmd == 'd':
                phone_number = input("Введите номер телефона:\n")
                print("Контакт(ы) удилен(ы)" if book.del_contact(phone_number) else "Контакт не найден")
            elif cmd == 'f':
                pprint(book.get_all_favorite_numbers())


    # adv_print('с чего начинается вывод. По умолчанию пустая строка;', "stroka2", start='--', max_line=20,in_file = "out_file.txt")