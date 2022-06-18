from pydantic import BaseModel, validator

class Post(BaseModel):
    id: int
    title: str
    
"""     @validator('id')
    def check_that_id_less2(cls, v):
        if v > 2:
            raise ValueError("Id is not less than 2")
        else:
            return v
 """
