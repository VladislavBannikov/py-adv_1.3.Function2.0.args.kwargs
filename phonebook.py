'''
Методы:

Вывод контактов из телефонной книги;
Добавление нового контакта;
Удаление контакта по номеру телефона;
Поиск всех избранных номеров;
Поиск контакта по имени и фамилии.
'''
from contact import Contact


class PhoneBook:
    __contacts = []

    def __init__(self,name):
        self.__name = name

    def get_book_name(self):
        return self.__name

    def print_contacts(self):
        for i, c in enumerate(self.__contacts):
            print(str(i)+':')
            print(c)

    def add_contact(self,firstname, lastname, phone_number, favorite_contact=False, **kwargs):
        try:
            self.__contacts.append(Contact(firstname, lastname, phone_number, favorite_contact, **kwargs))
        except Exception as e:
            print(e)

    def del_contact(self,phone_number :str):
        success = False
        for contact in self.__contacts:
            if contact.get_phone_number() == phone_number.strip():
                self.__contacts.remove(contact)
                success = True
        return success

    def get_all_favorite_numbers(self):
        all_fav = set()
        for contact in self.__contacts:
            if contact.get_favorite_contact():
                all_fav.add(contact.get_favorite_contact().get_phone_number())
        return list(all_fav)

    def find_contact(self,firstname: str, lastname: str) -> Contact:
        full_name = f'{firstname} {lastname}'.lower()
        for contact in self.__contacts:
            if contact.get_name().lower() == full_name:
                return contact

    def find_contact_by_id(self, id):
        try:
            return self.__contacts[int(id)]
        except Exception:
            return False

