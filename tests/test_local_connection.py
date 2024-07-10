import requests
import pytest


@pytest.mark.parametrize("uri", [
    "/",
    "/image/"
])
def test_local_connection(uri):
    response = requests.get(f"http://localhost{uri}")
    assert response.status_code == 200, f"Failed to connect to http://localhost{uri}. Status code = {response.status_code}"