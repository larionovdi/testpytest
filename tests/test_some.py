
import requests
#from jsonschema import validate
from configuration import SERVICE_URL
from pprint import pprint
from src.base_classes.response import Response
from src.schemas.user import User

#from src.schemas.post import POST_SCHEMA
#from src.pydantic_schemas.post import Post


"""     responses = Response(response)
    responses.asert_status_code(200).validate(Post) """

#   received_posts = response.json()

def test_getting_users_list():
    response = requests.get(SERVICE_URL)
    test_object = Response(response)
    test_object.asert_status_code(300).validate(User)
    


   


