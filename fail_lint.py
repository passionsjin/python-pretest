import os

TESTPATH = os.path.join(os.path.dirname(__file__), 'test_text.txt')

def print_test(text):
    '''

    :param text:
    :return:
    '''
    print(text)

with open(TESTPATH, 'w') as writer:
    writer.write('asdjsdkf')
    writer.close()

print_test("func")
print('hello')

if True:
    print('true')