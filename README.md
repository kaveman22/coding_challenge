# Coding Challenge App

A skeleton flask app to use for a coding challenge.

## Install:

create a virtual environment venv
```
python3 -m venv venv
source source venv/bin/activate
```
once the virtual environment is activavted install dependencies 
pip install from the requirements file
``` 
pip install -r requirements.txt
```
Depending on your version of python
 May have to update werkzeug 
 ```
 pip install --upgrade werkzeug
```

## Set the OAuth token for github
Depending on the organization that you choose to query you make exceed the rate limit for unauthorized github api calls in order to prevent any errors in the response you will need to create a person access token Information on how to do so can be found here.

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

```
curl -i "http://127.0.0.1:5000/orgs?org_name=mailchimp"
```


## What'd I'd like to improve on...


## Notes

 May have to update werkzeug pip install --upgrade werkzeug


