
import requests
#from jsonschema import validate
from configuration import SERVICE_URL

from src.base_classes.response import Response
#from src.schemas.post import POST_SCHEMA
from src.pydantic_schemas.post import Post

def test_getting_posts():
    response = requests.get(url=SERVICE_URL)
#    print(response)
    responses = Response(response)
    responses.asert_status_code(200).validate(Post)

#   received_posts = response.json()

   


