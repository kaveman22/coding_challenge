import unittest
from unittest import mock
from unittest.mock import patch
from app.interface import API
from app.processor import Data

api = API('mailchimp')

class test_interface(unittest.TestCase):

    @patch('app.interface.Data', return_value='data_obj')
    def test_init(self, mock_data):
        api = API('mailchimp')

        mock_data.assert_called_once()
        assert api.data == mock_data.return_value
        assert api.org == 'mailchimp'

    @patch('app.interface.requests.get')
    def test_github_num_followers(self, mock_request):
        mock_request.return_value.text = '{"followers": 200}'
        num_follwors = api.get_github_num_followers()
        
        mock_request.assert_called_once()
        assert num_follwors == 200

    @patch('app.interface.requests.get')
    def test_get_num_github_repos(self, mock_request):
        mock_request.return_value.text = '[{"private": false, "fork": false},\
                                            {"private": false, "fork": false}]'
        
        num_original, num_forked = api.get_num_github_repos()

        assert num_original == 2
        assert num_forked == 0
