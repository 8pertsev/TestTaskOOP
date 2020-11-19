from iperson import IPerson


class Teacher(IPerson):

    __salary: float

    def __init__(self, name, city, phone_num, salary):
        self.set_name(name)
        self.set_city(city)
        self.set_phone_num(phone_num)
        self.set_salary(salary)

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    # was used for debug
    def check_status(self):
        print('ima teacher')

    def show_info(self):
        print(f'Name: {self.get_name()}\nCity: {self.get_city()}\nPhone: {self.get_phone_num()}\nSalary: {self.get_salary()}')
        print('---')


    @property
    def __calculate_yearly_income(self):
        return self.__salary * 12

    def show_yearly_income(self):
        return self.__calculate_yearly_income


