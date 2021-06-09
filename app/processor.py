"""
Data Class Created to provide utility functions for response data processing
"""
import logging
from .utils import Logger
from typing import Dict, Any, Tuple, List

class Data(Logger):

    def get_github_num_followers(self, github_payload: Dict[Any, Any]) -> int:
        """
        Get the numner of github followers from an organization
        Arguments: github_payload - The Response from the github api 
        which contains the number of followers
        Return: int -  The number of followers on the github organization
        """
        try:
            if 'followers' not in github_payload:  
                raise LookupError('Missing Followers index') # Raise execption if followers is not in the payload
            else:
                return github_payload['followers']
        except Exception as e:
            logging.info(" Error - {}".format(e))
            return 0


    def get_github_num_original_forked_repos(self, github_payload: List[Dict[Any, Any]]) -> Tuple:
        """
        Parses through github response object to count the number of owned vs. forked repos
        Arguments: github_payload - Dictionary of repos
        Return: Tuple (#original_repos, #forked_repos)
        """
        original, fork = 0, 0 
        try:
            for i in github_payload:
                if i['private'] == False:
                    if i['fork'] == False:
                        original += 1
                    else:
                        fork += 1
        except Exception as e:
            logging.info("Error getting the number of original repos - {}".format(e))
            return 0, 0
        return original, fork



    def get_bitbucket_num_repos(self, bitbucket_payload: List[Dict[Any, Any]], org: str) -> Tuple:
        ### Assuming the owner key and username match the team name then that is considered and original repo
        # otherwise it is considered a forked repo Need to Valdate logic  
        """
        Get all languages and remove the duplicates
        Params: bitbucket_payload (list) of repositories from bitbucket
        Params: org (string) the name of the organization 
        Return Tuple (number of original, number of forked)
        """
        original, forked = 0, 0
        try:
            for i in bitbucket_payload:
                if i['owner']['username'] != org:
                    forked += 1
                else:
                    original += 1
        except Exception as e:
            logging.info('There was an error getting bitbucket num Repos - {}'.format(e))

        return original, forked

    def get_bitbucket_languages(self, bitbucket_payload):
        """
        Get all languages and remove the duplicates
        Params: bitbucket_payload list of repositories from bitbucket
        Return Tuple (languages set, number of languages)
        """
        languages = []
        try:
            for i in bitbucket_payload:
                languages.append(i['language'])
            languages = list(set(languages))
        except Exception as e:
            logging.info('There was an error getting bitbucket languages {}'.format(e))
            return 0 , 0
        return languages, len(languages)
