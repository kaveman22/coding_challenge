import unittest
from app.interface import API

class test_interface(unittest.TestCase):
    ## Need to mock the requested payload in get_github_org
    def test_get_github_org(self):
        mock_payload = {'followers' : 5}
        data = API().get_github_org()
        assert data == 5