from mylib.logistic import CITIES, distance_between_two_points, cities_list
from fastapi.testclient import TestClient
from main import app
import pytest



def test_dist():
    assert distance_between_two_points(CITIES[0][1], CITIES[1][1]) == 2450.9503446683375

def test_city_list():
    assert "Dallas" in cities_list()

#### Web Application Testing
@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

def test_read_main(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Logistics INC"}

# build a test for the cities endpoint
def test_cities(client):
    response = client.get("/cities")
    assert response.status_code == 200
    assert "cities" in response.json()
    assert "Dallas" in response.json()["cities"]
    assert "Houston" in response.json()["cities"]
    assert "New York" in response.json()["cities"]
    assert "Los Angeles" in response.json()["cities"]
    assert "Chicago" in response.json()["cities"]


# build a test for the distance endpoint
def test_distance(client):
    response = client.post(
        "/distance",
        json={"city1": {"name": "New York"}, "city2": {"name": "Los Angeles"}},
    )
    assert response.status_code == 200
    assert "distance" in response.json()


# build a test the travel time between two cities by car
def test_travel_time(client):
    response = client.post(
        "/travel",
        json={"city1": {"name": "New York"}, "city2": {"name": "Los Angeles"}},
    )
    assert response.status_code == 200
    assert response.json() == {"travel_time": "41 hours"}