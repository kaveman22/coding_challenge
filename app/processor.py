
import logging
from .utils import Logger

class Data(Logger):

    def get_github_num_followers(self, github_payload):
        try:
            if 'followers' not in github_payload:
                raise LookupError('Missing Followers index')
            else:
                return github_payload['followers']
        except Exception as e:
            logging.info(" Error - {}".format(e))
            return 0


    def get_github_num_original_forked_repos(self, github_payload):
        original, fork = 0, 0 
        for i in github_payload:
            if i['private'] == False:
                if i['fork'] == False:
                    original += 1
                else:
                    fork += 1
        return original, fork



    def get_bitbucket_num_repos(self, bitbucket_payload, org):
        ### Assuming the owner key and username match the team name then that is considered and original repo
        # otherwise it is considered a forked repo Need to Valdate logic  
        """
        Get all languages and remove the duplicates
        Params: bitbucket_payload list of repositories from bitbucket
        Params: org the name of the organization 
        Return Tuple (number of original, number of forked)
        """
        original, forked = 0, 0
        for i in bitbucket_payload:
            if i['owner']['username'] != org:
                forked += 1
            else:
                original += 1

        return original, forked

    def get_bitbucket_languages(self, bitbucket_payload):
        """
        Get all languages and remove the duplicates
        Params: bitbucket_payload list of repositories from bitbucket
        Return Tuple (languages set, number of languages)
        """
        languages = []
        
        for i in bitbucket_payload:
            languages += i['language']

        languages = list(set(languages))

        return languages, len(languages)
