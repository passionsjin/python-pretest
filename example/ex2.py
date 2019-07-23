'''
ex2.
Whitespace
'''
MYSTRING = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

def get_str_size(data):
    '''
    string을 받아 size를 반환
    :param data: str
    :return: len(data)
    '''
    return len(data)

print("MYSTRING LENGTH : %d " % get_str_size(MYSTRING))
