from jsonschema import validate
from src.schemas.post import POST_SCHEMA


class ResponseClass:
    def __init__(self, response):
        self.response = response

    def validate(self, schema):
        if isinstance(self.response, list):
            for item in self.response:
                validate(item, schema)
        else:
            validate(self.response, schema)


