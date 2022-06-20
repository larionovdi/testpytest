
import requests
#from jsonschema import validate
from configuration import SERVICE_URL
from pprint import pprint
from src.base_classes.response import Response
from src.schemas.user import User
import pytest

#from src.schemas.post import POST_SCHEMA
#from src.pydantic_schemas.post import Post


"""     responses = Response(response)
    responses.asert_status_code(200).validate(Post) """

#   received_posts = response.json()

def test_getting_users_list(get_users):
    
    Response(get_users).asert_status_code(200).validate(User)



@pytest.mark.development 
@pytest.mark.production
@pytest.mark.skip("For example issue with network")
def test_another():
    # I that test we try ... 
    assert 1 == 1



@pytest.mark.parametrize("first_value, second_value, result",[
    (1,2,3),
    (-1,-2,-3),
    (-1,2,1),
    ("b", -2, None),
    ("b","a", None)

])
def test_calculator_param(first_value, second_value, result, calculate):
    """      I this test we try to calculating numbers and str """
    assert calculate(first_value, second_value) == result
    