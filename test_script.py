import requests
import json

def test_get_all_merken():
    response = requests.get('http://127.0.0.1:8000/get/merken/')
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    for x in response_dictionary:
        assert type(x["merkId"]) == int
        assert type(x["merkNaam"]) == str
        assert type(x["smaakId"]) == int
        assert type(x["verpakkingId"]) == int

def test_get_merk():
    response = requests.get('http://127.0.0.1:8000/get/merk/1')
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert type(response_dictionary["merkId"]) == int
    assert type(response_dictionary["merkNaam"]) == str
    assert type(response_dictionary["smaakId"]) == int
    assert type(response_dictionary["verpakkingId"]) == int
    
def test_get_smaken():
    response = requests.get('http://127.0.0.1:8000/get/smaken')
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    for x in response_dictionary:
        assert type(x["smaakId"]) == int
        assert type(x["smaakNaam"]) == str

def test_get_verpakkingen():
    response = requests.get('http://127.0.0.1:8000/get/verpakkingen')
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    for x in response_dictionary:
        assert type(x["verpakkingId"]) == int
        assert type(x["Type"]) == str
        
def test_get_merk_non_existing():
    response = requests.get('http://127.0.0.1:8000/get/merk/1518')
    assert response.status_code == 404
    response_dictionary = json.loads(response.text)
    assert 'Merk niet gevonden!' in response_dictionary.values()
