import requests
import pytest

urls = ['http://cumshot.hopto.org/', 'http://cumshot.hopto.org/image/']

@pytest.mark.parametrize("url", urls)
def test_http_connection(url):
    response = requests.get(url)
    assert response.status_code == 200, f'Failed to connect to {url}. Status code = {response.status_code}'