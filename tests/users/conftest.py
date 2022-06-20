from random import randrange
import pytest


def _calculate(a,b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return None
    

@pytest.fixture
def calculate():
    return _calculate

@pytest.fixture
def make_number():
#    print("I am getting number ")
    number = randrange(1, 1000, 5)
    yield number 
#    print(f"Number at home {number}")

