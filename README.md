# Test FastAPI

## Requirements
- docker
- docker-compose

## Run web service 
Execute command:
```
DB_USER=user DB_PASS=mysecretpassword DB_NAME=postgres docker-compose up web

```
## Run tests
Execute command:
```
docker-compose --env-file ./.env.test up test
```
