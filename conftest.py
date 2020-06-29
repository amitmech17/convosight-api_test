import requests
import pytest
import json


@pytest.fixture(scope='class')
def api_setup(baseurl):
    return baseurl


# def pytest_addoption(parser):
#     parser.addoption("--environment")
#
#
# @pytest.fixture(scope="session")
# def environment(request):
#     return request.config.getoption("--environment")


def pytest_addoption(parser):
    parser.addoption("--baseurl")


@pytest.fixture(scope="session")
def baseurl(request):
    return request.config.getoption("--baseurl")
