from iperson import IPerson


class Student(IPerson):
    
    __mark: int

    def __init__(self, name, city, phone_num, mark):
        self.set_name(name)
        self.set_city(city)
        self.set_phone_num(phone_num)
        self.set_mark(mark)

    def set_mark(self, mark):
        self.__mark = mark

    def get_mark(self):
        return self.__mark

    # was used for debug
    def check_status(self):
        print('ima student')

    def show_info(self):
        print(f'Name: {self.get_name()}\nCity: {self.get_city()}\nPhone: {self.get_phone_num()}\nMark: {self.get_mark()}')
        print('---')
