import pytest
import unittest
import requests
import json
from assertions import  assert_valid_schema


@pytest.mark.usefixtures("api_setup")
class TestPostApi(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, api_setup):
        self.base_url = api_setup

    def test_postapi_validating_status_code(self):
        headers = {'Content-Type': 'application/json',
                   'User-Agent': '	Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}
        response = requests.post('{}/api/users'.format(self.base_url), data=json.dumps({"name":"jitu kumar","job":"QA"}), headers=headers)
        assert response.status_code == 201

    def test_postapi_validating_contenttype(self):
        headers = {'Content-Type': 'application/json',
                   'User-Agent': '	Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}
        response = requests.post('{}/api/users'.format(self.base_url), data=json.dumps({"name":"rakesh","job":"QA 2"}), headers=headers)
        assert response.headers['Content-Type'] == "application/json; charset=utf-8"

    def test_postapi_validating_name_in_reponse(self):
        headers = {'Content-Type': 'application/json',
                   'User-Agent': '	Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}
        response = requests.post('{}/api/users'.format(self.base_url),
                                 data=json.dumps({"name": "madhur", "job": "QA 3"}), headers=headers)
        response_body = response.json()
        assert response_body["name"] == "madhur"

    def test_postapi_validating_json_schema(self):
        headers = {'Content-Type': 'application/json',
                   'User-Agent': '	Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}
        response = requests.post('{}/api/users'.format(self.base_url),
                                 data=json.dumps({"name": "kio", "job": "QA 8"}), headers=headers)
        json_data = response.json()
        assert_valid_schema(json_data, 'schemas/userpost.json')


    def test_postapi_negative_passing_number_in_name(self):
        headers = {'Content-Type': 'application/json',
                   'User-Agent': '	Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}
        response = requests.post('{}/api/users'.format(self.base_url),
                                 data=json.dumps({"name": "2", "job": "QA"}), headers=headers)
        assert response.status_code == 400
