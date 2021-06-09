"""
API class for making requests to github/bitbucket apis
"""

from typing import Tuple, List
from .processor import Data
from .utils import Logger
import json 
import logging 
import requests
from os import environ

class API(Logger):
    def __init__(self, org):
        self.org = org
        self.data = Data()
        self.header = {"Accept": "application/vnd.github.mercy-preview+json", "Authorization": "token {}".format(environ['gh_token'])}

    def get_github_num_followers(self) -> int:
        """
        Retrieves Number of followers for a github organization
        Return integer number of follwers
        """
        url = 'https://api.github.com/orgs/' + self.org
        res = requests.get(url, headers=self.header)
        res = json.loads(res.text)
        num_github_followers  = self.data.get_github_num_followers(res)
        return num_github_followers

    def get_num_github_repos(self) -> Tuple:
        """
        Retrieves all the repos in a github organization, queries all repos and passes
        the data payload to external function to count original vs. forked repos
        Return: Tuple (# of original Repos, # of forked repos)
        """

        url = 'https://api.github.com/orgs/' + self.org + '/repos'
        try:
            res = requests.get(url=url, headers=self.header)
        except Exception as e:
            logging.info('There was an error retrieving gitlab repos- {}'.format(e))
            return 0, 0 
        
        res = json.loads(res.text)
        num_original_repos, num_fork_repos = self.data.get_github_num_original_forked_repos(res)
 
        return num_original_repos, num_fork_repos

    def get_github_languages(self) -> Tuple:
        """
        Iteratively makes requests to github repos endpoint to collect the language info 
        Return: Tuple (list of deduplicate languages, Number of languages)
        """
        url = 'https://api.github.com/orgs/' + self.org + '/repos'
        res = requests.get(url, headers=self.header)
        res = json.loads(res.text)

        lang_urls = [i['languages_url'] for i in res]
        
        langs = []
        for i in lang_urls:
            try:
                langs += (json.loads(requests.get(url=i, headers=self.header).text).keys())
            except Exception as e:
                logging.info("Error Making call to github language endpoint- {}".format(e))
        langs = list(set(langs))

        return langs, len(langs)


    def get_github_topics(self) -> Tuple:
        """
        Iteratively makes requests to github topics endpoint to collect the language info 
        Return: Tuple of deduplicated languages, Number of languages)
        """
        url = 'https://api.github.com/orgs/' + self.org + '/repos'
        res = requests.get(url=url, headers=self.header)
        res = json.loads(res.text)
        topics_url = 'https://api.github.com/repos/' + self.org +'/'
        topic_urls = [topics_url + i['name'] + '/topics' for i in res]
        topics = []

        for i in topic_urls:
            try:
                res = json.loads(requests.get(url=i, headers=self.header).text)
                if 'names' in res:
                    topics += (res['names'])
            except Exception as e:
                logging.info("Error Making call to github topic endpoint - {}".format(e))
                return topics, len(topics)

        topics = list(set(topics))
        return topics, len(topics)


    def get_bitbucket_repos(self) -> Tuple:
        """
        Get all repositories for an organization on bitbucket and count the number of 
        forked repos vs. original repos 
        Return Tuple (number of original repos, number of forked repos)
        """
        repos = []
        try:
            url = 'https://api.bitbucket.org/2.0/repositories/' + self.org
            res = json.loads(requests.get(url=url, headers=self.header).text)
            repos = res['values']
            if 'next' in res:
                while res['next']:  ## get all repos if pagination exists
                    res = json.loads(requests.get(url=res['next'], headers=self.header).text)
                    repos += res['values']
        except Exception as e:
            logging.info('There was an error getting bitbucket repos - {}'.format(e))
        
        original, forked = self.data.get_bitbucket_num_repos(repos, self.org)  # Get number of repos
        languages, num_of_languages = self.data.get_bitbucket_languages(repos) # Get langauges
        
        watcher_urls = [i['links']['watchers']['href'] for i in repos]  # Get all the watcher urls 

        watchers = self.get_bitbucket_watchers(watcher_urls)

        return original, forked, languages, num_of_languages, watchers


    def get_bitbucket_watchers(self, watcher_urls: List) -> int:
        """
        Makes request to bitbucket api to get the watchers urls
        Argument: watcher_urls ( List ) list of url's to get the watchers
        Return: number of watchers (int)
        """
        watchers = 0 
        for i in watcher_urls:
            try:
                res = json.loads(requests.get(url=i, headers=self.header).text)
                watchers  += res['size']
            except Exception as e:
                logging.info('There was an error retrieving watchers -Error: {}'.format(e))
                return 0
        return watchers