'''
docstring
'''
from datetime import datetime


class HelloPyLint:
    '''
    class docstring
    '''
    def __init__(self, data):
        '''
        module docstring
        :param data:
        '''
        self.__data = data

    def get_data(self):
        '''
        module docstring
        :return:
        '''
        return self.__data

    def set_data(self, data):
        '''
        module docstring
        :param data:
        :return:
        '''
        self.__data = data

    def len_data(self):
        '''
        module docstring
        :return:
        '''
        return len(self.__data)


def get_datetime_now():
    '''
    module docstring
    :return:
    '''
    return datetime.now()


if __name__ == '__main__':
    MYCLASS = HelloPyLint('HelloPyLint')

    print(MYCLASS.get_data())
