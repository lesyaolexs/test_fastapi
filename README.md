#Test FastAPI
To run fast API execute command:
```
DB_USER=user DB_PASS=mysecretpassword DB_NAME=postgres docker-compose up web
```
To run tests execute command:
```
docker-compose --env-file ./.env.test up test
```
