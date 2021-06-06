import unittest
from app.processor import Data

class test_processor(unittest.TestCase):
    
    def test_get_github_num_followers(self):
        mock_payload = {'followers' : 5}
        data = Data().get_github_num_followers(mock_payload)
        assert data == 5

    def test_get_github_num_followers_bad_payload(self):
        mock_payload = {'people' : 5}
        data = Data().get_github_num_followers(mock_payload)
        assert data == 0
        self.assertRaises(LookupError)
        