# Coding Challenge App

A skeleton flask app to use for a coding challenge.

## Install:

create a virtual environment venv
```
python3 -m venv venv
source venv/bin/activate
```
once the virtual environment is activavted install dependencies 
from the requirements file
``` 
pip install -r requirements.txt
```
Depending on your version of python
 May have to update werkzeug 
 ```
 pip install --upgrade werkzeug
```

## Set the OAuth token for github
Depending on the organization that you choose to query you may exceed the rate limit for unauthorized github api calls. In order to prevent any errors in the response you will need to create a personal access token. Information on how to do so can be found here.

https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token#using-a-token-on-the-command-line


When determining the scope of the access token you will want to check the following boxes.

![](/pat_scope.png)


Once you have your access token run an export command from your working directory in your virtual environment 

```
export gh_token={your_token_here}
```
## Running the code

### Spin up the service

```
# start up local server
python -m run 
```

### Making Requests
Ensure the server is running and make a request using the following url.
You can replace 'mailchimp' with some other valid github/bitbucket organization/team_name

```
curl -i "http://127.0.0.1:5000/orgs?org_name=mailchimp"
```


## What'd I'd like to improve on...

Testing -  Due to time constraints I did not have a lot of time to test all functions I would definitely want to write more tests for all functions

Error Handling - There are many situations where an external api can give unexpected responses , so ideally all requests should have adeqaute error handling to account for this.


Speed - Because there are many api calls happening to get the data, it takes a while for the final response to come back , I would implement threading to retrieve the data faster 

Organization - Due to time constraints I did not organize the code very well , some functions are larger than I would like them to be and in the wrong area. I would look at re-organizing the code quite a bit

More docstrings and comments - Because this was just an MVP I put docstrings can comments in various places but not everywhere. Ideally all functions would have a docstrings, and type hinting

## Notes

It was unclear how to retrieve the information on if a repo was forked from the bitbucket API. I made the assumption that if the owner of the repo was the same as the org/team name then it was an original , and if the owner name was different I assumed it was a forked repo.


Given a bit more time I am willing and able to do all of the above in the improve on section. This project was fun to do and I look forward to diving into the code for a review!


