
from datetime import datetime

class HelloPyLint:
    def __init__(self, data, nothing):

        self.__data = data

    def get_data(self):

        return self.__data

    def set_data(self, data):

        self.__data = data

    def len_data(self):

        return len(self.__data)

    def unused(self, data):
        return "Nothing"


def get_datetime_now():
    '''
    Unused Function
    :return:
    '''
    return datetime.now()



if __name__ == '__main__':
    my_class = HelloPyLint('HelloPyLint')

    print(my_class.get_data())
