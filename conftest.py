import pytest
import requests

from random import randrange

SERVICE_URL = "https://my-json-server.typicode.com/typicode/demo/posts"
SERVICE_URL_1 = "https://gorest.co.in/public/v1/users"


@pytest.fixture
def get_users():
    response = requests.get(SERVICE_URL_1)
    # print('hallo')
    return response


def _calculate(a, b):
    return a + b


@pytest.fixture
def calculate():
    return _calculate


@pytest.fixture
def make_number():
    print("I am getting number")
    number = randrange(1, 1000, 5)
    yield number
    print(f"Number at home {number}")

