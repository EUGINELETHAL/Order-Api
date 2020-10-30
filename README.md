[![Build Status](https://travis-ci.com/EUGINELETHAL/Backend-challenge.svg?branch=master)](https://travis-ci.com/EUGINELETHAL/Backend-challenge)
https://github.com/EUGINELETHAL/Backend-challenge/blob/master/coverage.svg
# ORDER-API
Order-Api is a simple REST  API used to upload customrs orders.
User Stories
Users authenticates via OAUTH2 and OpenidCOnnect(GOogleOAuth 2.0 )
Customer creates order 
Customers gets message after order created sucessfully(Asynchronous  Task)


# Tools and Technologies
Django 
DjangoRest
Travis(CI/CD)
Heroku-Deployment
AfricaisTalking-(SMSGATEWAY)
Coverage
Celery
Redis
## API ENDPOINTS

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/470df32a30646e961eb9)
#### Question Endpoints.
| API Endpoint  | Description | Methods |
| ------------- | ------------- | ------------- |
| /oidc/authenticate/  | Authentication | GET  |
| /api/v1/order  | Get all orders   | GET  |
 /api/v1/order | Customer posts order  | GET  |


## TODO
Improve on TestCoverage
Use pytest as the testing framework
Implement Containerization using Docker


## Getting Started
To get started:
 Git clone the repository using https://github.com/EUGINELETHAL/Backend-challenge
 For the API to run smoothly you will need the following:
```
1. Python 3.6 or higher installed.
2. Pip3
3. Pipenv or virtualenv installed.
```
### Installing
> __Local Development Guide.__

1. Git clone the repository using 
2. Through your terminal, navigate to the location with the cloned repository.
3. Open the cloned repo folder using your terminal.
4. You're currently on the `develop` branch.
5. Set up a virtual environment:
    > Using virtualenv: `virtualenv -p python3 env`
    > Using pipenv: `pipenv shell`
6. To activate the virtual environment:
    > Using virtualenv: `source env/bin/activate`
    > Using pipenv: `not necessary`(since it automatically activates itself after creation)
7. Install the packages:
    > Using virtualenv: `pip3 install -r requirements.txt`
    > Using pipenv: `pipenv install`
8. There is already a `sample.env` file containing all the necessary environment variables.


## Running the tests
 run python manage
### Style Guide.
PEP 8

## Deployment
Heroku


## Built With
* Django and Django Rest Framework

## Authors
* **Ochung Eugine.** 
