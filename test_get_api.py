import pytest
import unittest
import requests
from assertions import  assert_valid_schema


@pytest.mark.usefixtures("api_setup")
class TestGetApi(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, api_setup):
        self.base_url = api_setup

    def test_getapi_validating_status_code(self):
        page = 1
        print(self.base_url)
        headers = {'Content-Type': 'text/html',
                   'User-Agent': '	Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}
        response = requests.get('{}/api/users?page={}'.format(self.base_url, page), headers=headers)
        assert response.status_code == 200

    def test_getapi_validating_contenttype(self):
        page = 1
        print(self.base_url)
        headers = {'Content-Type': 'text/html',
                   'User-Agent': '	Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}
        response = requests.get('{}/api/users?page={}'.format(self.base_url, page), headers=headers)
        assert response.headers['Content-Type'] == "application/json; charset=utf-8"

    def test_getapi_validating_page_in_reponse(self):
        page = 1
        print(self.base_url)
        headers = {'Content-Type': 'text/html',
                   'User-Agent': '	Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}
        response = requests.get('{}/api/users?page={}'.format(self.base_url, page), headers=headers)
        response_body = response.json()
        assert response_body["page"] == 1

    def test_getapi_validating_json_schema(self):
        page = 1
        print(self.base_url)
        headers = {'Content-Type': 'text/html',
                   'User-Agent': '	Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}
        response = requests.get('{}/api/users?page={}'.format(self.base_url, page), headers=headers)
        json_data = response.json()
        assert_valid_schema(json_data, 'schemas/user.json')

    def test_getapi_negative_passing_page_1000(self):
        page = 1000
        print(self.base_url)
        headers = {'Content-Type': 'text/html',
                   'User-Agent': '	Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}
        response = requests.get('{}/api/users?page={}'.format(self.base_url, page), headers=headers)
        assert response.status_code == 200

    def test_getapi_negative_passing_page_0(self):
        page = 0
        print(self.base_url)
        headers = {'Content-Type': 'text/html',
                   'User-Agent': '	Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}
        response = requests.get('{}/api/users?page={}'.format(self.base_url, page), headers=headers)
        response_body = response.json()
        assert response_body["page"] == 0
