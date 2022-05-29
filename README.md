# Test FastAPI

## Requirements
- docker
- docker-compose

## Run web service 
Execute command:
```
DB_USER=user DB_PASS=mysecretpassword DB_NAME=postgres docker-compose up web
```
Documentation and playground:

http://0.0.0.0:8000/redoc

## Run tests
Execute command:
```
docker-compose --env-file ./.env.test up test
```
