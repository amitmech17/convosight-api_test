import pytest
import unittest
import requests
from assertions import  assert_valid_schema


@pytest.mark.usefixtures("api_setup")
class TestDeleteApi(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, api_setup):
        self.base_url = api_setup

    def test_delete_api_validating_status_code(self):
        user = 1
        headers = {'Content-Type': 'text/html',
                   'User-Agent': '	Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}
        response = requests.delete('{}/api/users/{}'.format(self.base_url, user), headers=headers)
        assert response.status_code == 204