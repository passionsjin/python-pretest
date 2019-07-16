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


TESTPATH = os.path.join(os.path.dirname(__file__), 'test_text.txt')

with open(TESTPATH, 'w') as writer:
    writer.write('asdjsdkf')
    writer.close()

print('hello')
