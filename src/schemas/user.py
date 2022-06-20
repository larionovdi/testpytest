
from pydantic import BaseModel, validator
from src.enums.user_enums import Genders, Statuses, UserErrors


class User(BaseModel):
    id: int
    name: int
    email: int
    gender: Genders
    status: Statuses

    @validator('email')
    def check_that_dog_presented_in_email_address(cls, email):
        if '@' in email:
            return email
        else:
            raise ValueError(UserErrors.WRONG_EMAIL.value)
        
        