'''
ex 1.
잘못된 들여쓰기
'''
import os

print('hello pylint')

MYPATH = os.path.join(
os.path.dirname(__file__),
   "test_path")

print(MYPATH)
