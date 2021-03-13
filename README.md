[![Build Status](https://travis-ci.com/EUGINELETHAL/Backend-challenge.svg?branch=main)](https://travis-ci.com/EUGINELETHAL/Backend-challenge)[![](https://github.com/EUGINELETHAL/Backend-challenge/blob/master/coverage.svg)
[![Coverage Status](https://coveralls.io/repos/github/EUGINELETHAL/Order-Api/badge.svg?branch=main)](https://coveralls.io/github/EUGINELETHAL/Order-Api?branch=main)
# ORDER-API
..Order-Api is a simple REST  API used to upload customers orders.
..User Stories
Users authenticates via OAUTH2 and OpenidCOnnect(GOogleOAuth 2.0 )
Customer creates order 
Customers gets message after order created sucessfully(Asynchronous  Task)


# Tools and Technologies
 Django 
2. DjangoRest
3. Travis(CI/CD)
4. Heroku-Deployment
5. AfricaisTalking-(SMSGATEWAY)
6. Coverage
7. Celery
8. Redis
9. Pytest
10. Docker
11. Docker-Compose
## API ENDPOINTS

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/470df32a30646e961eb9)
#### Question Endpoints.
| API Endpoint  | Description | Methods |
| ------------- | ------------- | ------------- |
| /oidc/authenticate/  | Authentication | GET  |
  /api/v1/customer  | create customer  | POST |
| /api/v1/order  | Get all orders   | GET  |
 /api/v1/order | Customer posts order  | POST  |




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
4. You're currently on the `main` branch.



## Running the tests
 python manage 
### Style Guide.
PEP 8

## Deployment
Heroku


## Built With
* Django and Django Rest Framework

## Authors
* **Ochung Eugine.** 
