from collections import UserDict


class AddressBook(UserDict):
    # def __init__(self, name: str, phone: list = None):

    def add_record(self, name: Name, phone: list = None):
        new_contact = Record(name=Name, phone=Phone)
        self.data[name] = new_contact


class Record:
    def __init__(self, name: str, phone: list = None):
        self.name = Name
        if phone is not None:
            self.phone = [phone]
        else:
            self.phone = []

    def add_phone_field(self, phone_number: str):
        self.phone.append(phone_number)

    def change_phone_field(self, old_number: str, new_number: str):
        try:
            self.phone.remove(old_number)
            self.phone.append(new_number)
        except ValueError:
            return

    def delete_phone_field(self, phone: Phone = None):
        pass


class Field:
    pass


class Name(Field):
    pass


class Phone(Field):
    pass



