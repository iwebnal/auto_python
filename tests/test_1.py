import requests
import conftest

from src.baseclasses.response_classes import ResponseClass
from src.schemas.post import POST_SCHEMA


def test_getting_posts():
    res = requests.get(url=conftest.SERVICE_URL)
    response = ResponseClass(res)

    response.assert_status_code(200).validate(POST_SCHEMA)


