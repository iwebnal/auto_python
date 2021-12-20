from pydantic import BaseModel, validator, ValidationError, Field


class Post(BaseModel):
    id: int
    title: str

    @validator('id')
    def check_id(cls, v):
        if v > 2:
            raise ValueError("ID is not less than two")
        return v
