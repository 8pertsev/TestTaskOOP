from abc import ABC, abstractmethod


class IPerson(ABC):

    __name: str
    __city: str
    __phone_num: int

    @abstractmethod
    def show_info(self):
        pass

    @abstractmethod
    def check_status(self):
        pass

    def get_name(self):
        return self.__name

    def get_city(self):
        return self.__city

    def get_phone_num(self):
        return self.__phone_num

    def set_name(self, name):
        self.__name = name

    def set_city(self, city):
        self.__city = city

    def set_phone_num(self, phone_num):
        self.__phone_num = phone_num
