import requests 
import pytest

def test_status_code():
    url = "https://swapi.dev/api/people/1"
    response = requests.get(url)
    assert response.status_code==200

def test_check_response():
    url = "https://swapi.dev/api/people/1"
    response = requests.get(url)
    response = response.json()
    assert response["name"] == "Luke Skywalker"

data = [("name","Luke Skywalker",1), ("height", "202",4), ("mass","49",5)]

@pytest.mark.parametrize("key,value,id",data)
def test_piece_of_body(key,value,id):
    url = f"https://swapi.dev/api/people/{id}"
    response = requests.get(url)
    response = response.json()
    assert response[key]==value