import pytest
import requests

SERVICE_URL = "https://my-json-server.typicode.com/typicode/demo/posts"
SERVICE_URL_1 = "https://gorest.co.in/public/v1/users"


@pytest.fixture
def get_users():
    response = requests.get(SERVICE_URL_1)
    # print('hallo')
    return response
