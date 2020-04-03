'''
Имя, фамилия, телефонный номер - обязательные поля;
Избранный контакт - необязательное поле. По умолчанию False;
Дополнительная информация(email, список дополнительных номеров, ссылки на соцсети) - необходимо использовать *args, **kwargs.
Переопределить "магический" метод str для красивого вывода контакта. Вывод контакта должен быть следующим

    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    print(jhon)

Имя: Jhon
Фамилия: Smith
Телефон: +71234567809
В избранных: нет
Дополнительная информация:
	 telegram : @jhony
	 email : jhony@smith.com

'''


import os


class Contact:
    def __init__(self, firstname, lastname, phone_number, favorite_contact=False, **kwargs):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__phone_number = phone_number
        self.__favorite_contact = favorite_contact
        self.__additional_info = kwargs

    def __str__(self):
        s = f"Имя: {self.__firstname}{os.linesep}"
        s += f"Фамилия: {self.__lastname}{os.linesep}"
        s += f"Телефон: {self.__phone_number}{os.linesep}"
        s += f"В избранных: {self.__favorite_contact.get_name() if self.__favorite_contact else 'нет'}{os.linesep}"
        if self.__additional_info:
            s += f"Дополнительная информация:{os.linesep}"
            for k,v in self.__additional_info.items():
                s += f"\t{k} : {v}{os.linesep}"
        return s

    def get_name(self)-> str:
        return f'{self.__firstname} {self.__lastname}'

    def get_phone_number(self):
        return self.__phone_number

    def get_favorite_contact(self):
        return self.__favorite_contact
