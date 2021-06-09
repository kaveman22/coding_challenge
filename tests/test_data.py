import unittest
from app.processor import Data

data = Data()
class test_data(unittest.TestCase):
    def test_get_github_num_followers(self):
        payload = {'followers': 10}
        assert data.get_github_num_followers(payload) == 10

    def test_get_github_num_followers_exception(self):
        payload = {'follower': 10}
        assert data.get_github_num_followers(payload) == 0
        self.assertRaises(LookupError)

    def test_get_giithub_num_original_forked_repos(self):
        payload = [{'private': False, 'fork': False},\
                    {'private': False, 'fork': False},\
                    {'private': False, 'fork': True}]
        assert 2, 1 == data.get_github_num_original_forked_repos(payload)

    def test_get_giithub_num_original_forked_repos_exception(self):
        payload = [{'priv': False, 'fork': False},\
                    {'private': False, 'fork': False},\
                    {'private': False, 'fork': True}]
        assert (0, 0) == data.get_github_num_original_forked_repos(payload)
        self.assertRaises(Exception)

    def test_get_bitbucket_num_repos(self):
        org = 'mailchimp'
        payload = [{'owner': {'username': 'mailchimp'}},\
                    {'owner': {'username': 'chimp'}}]
        assert 1, 1 == data.get_bitbucket_num_repos(payload, org)

    def test_get_bitbucket_num_repos_execption(self):
        org = 'mailchimp'
        payload = [{'own': {'username': 'mailchimp'}},\
                    {'owner': {'username': 'chimp'}}]
        self.assertRaises(Exception)
        assert (0,0) == data.get_bitbucket_num_repos(payload, org)

    def test_get_bitbucket_languages(self):
        payload= [{'language': 'python'},\
                    {'language': 'java'},\
                    {'language': 'go'},\
                    {'language': 'python'}]
        assert ['java', 'python', 'go'], 3 == data.get_bitbucket_languages(payload)

    def test_get_bitbucket_languages_exception(self):
        payload= [{'lang': 'python'},\
                    {'language': 'java'},\
                    {'language': 'go'},\
                    {'language': 'python'}]
        assert (0, 0)== data.get_bitbucket_languages(payload)
        self.assertRaises(Exception)