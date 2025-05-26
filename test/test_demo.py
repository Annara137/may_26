# import random
#
# my_list = ['one', 'two', 'three']
# print(random.choice(my_list))

import pytest

@pytest.fixture()
def before_after():
    print('Before test')
    yield None
    print('\nAfter test')

def test_demo_1():
    assert  1 == 1

def test_demo_2(before_after):
    assert  2 == 2