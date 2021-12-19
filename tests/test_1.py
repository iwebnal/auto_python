import requests
import conftest

from src.enums.global_enums import GlobalErrorMesages
from src.schemas.post import POST_SCHEMA
from jsonschema import validate


# def test_equal():
#     assert 1 == 1, "Number is not equal to expected"


def test_getting_posts():
    response = requests.get(url=conftest.SERVICE_URL)
    received_posts = response.json()
    # print(received_posts)

    assert response.status_code == 200, GlobalErrorMesages.WRONG_STATUS_CODE.value
    assert len(received_posts) == 3, GlobalErrorMesages.WRONG_ELEMENT_COUNT.value
    """
    Moved to response_classes.py
    
    for item in received_posts:
        validate(item, POST_SCHEMA)
    
    """


