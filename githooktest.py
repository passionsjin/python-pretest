'''
Git precommit Test
1. check lint
2. coverage
'''
import os


def print_test(text):
    '''

    :param text:
    :return:
    '''
    print(text)


def print_test2(text):
    '''

    :param text:
    :return:
    '''
    print(text)


def print_test3(text):
    '''

    :param text:
    :return:
    '''
    print(text)


def print_test4(text):
    '''

    :param text:
    :return:
    '''
    print(text)


def print_test5(text):
    '''

    :param text:
    :return:
    '''
    print(text)


def print_tes6t(text):
    '''

    :param text:
    :return:
    '''
    print(text)


def print_test7(text):
    '''

    :param text:
    :return:
    '''
    print(text)


def print_test8(text):
    '''

    :param text:
    :return:
    '''
    print(text)


def print_test12(text):
    '''

    :param text:
    :return:
    '''
    print(text)


def print_test13(text):
    '''

    :param text:
    :return:
    '''
    print(text)


def print_test14(text):
    '''

    :param text:
    :return:
    '''
    print(text)


TESTPATH = os.path.join(os.path.dirname(__file__), 'test_text.txt')

with open(TESTPATH, 'w') as writer:
    writer.write('asdjsdkf')
    writer.close()

print_test("func")
print('hello')

if True:
    print('true')
