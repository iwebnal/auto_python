from jsonschema import validate
from src.schemas.post import POST_SCHEMA
from src.enums.global_enums import GlobalErrorMesages


class ResponseClass:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json().get('data')
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                # validate(item, schema)
                schema.parse_obj(item)
        else:
            # validate(self.response_json, schema)
            schema.parse_obj(self.response_json)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, GlobalErrorMesages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == status_code, GlobalErrorMesages.WRONG_STATUS_CODE.value
        return self
