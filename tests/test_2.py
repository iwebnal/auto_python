import requests

from conftest import SERVICE_URL_1
from src.baseclasses.response_classes import ResponseClass
from src.schemas.users import User

resp = requests.get(SERVICE_URL_1)


def test_getting_users_list():
    response = requests.get(SERVICE_URL_1)
    test_obj = ResponseClass(response)
    test_obj.assert_status_code(200).validate(User)

# print(resp.json())
