import logging

import flask
from flask import Response, request
from .interface import API
import json
app = flask.Flask("user_profiles_api")
logger = flask.logging.create_logger(app)
logger.setLevel(logging.INFO)


@app.route("/health-check", methods=["GET"])
def health_check():
    """
    Endpoint to health check API
    """
    app.logger.info("Health Check!")
    return Response("All Good!", status=200)


@app.route("/orgs", methods=["GET"])
def get_org():
    """
    Endpoint to health check API
    """
    response = {}
    try:
        org_name = request.args.get('org_name')
        api = API(org_name)
        gh_original, gh_forked = api.get_num_github_repos()
        gh_languages, gh_num_languages = api.get_github_languages()
        gh_topics, gh_num_topics = api.get_github_topics()
        bb_original, bb_forked, languages, num_languages, watchers = api.get_bitbucket_repos()

        response['github_org'] = {
            'number_followers': api.get_github_num_followers(),
            'number_original_repos': gh_original,
            'number_forked_repos': gh_forked,
            'languages': gh_languages,
            'number_languages': gh_num_languages,
            'topics': gh_topics,
            'number_topics': gh_num_topics
            }
        response['bitbucket_org'] = {
            'num_followers': watchers,
            'number_original_repos': bb_original,
            'number_forked_repos': bb_forked,
            'languages': languages,
            'num_languages': num_languages
            }

    except Exception as e:
        return Response("Error", status=404)
    
    return Response(response=json.dumps(response, indent=2), status=200)
