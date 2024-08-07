# REST API example application

This is a app for telus test.

The entire application is contained within the `app.py` file.

and file `conjob.py` for create task on the container

from file `.env.example` remove `.example`.

## Docker-compose build

    docker-compose build

## Docker-compose run

    docker-compose up

# REST API

The REST API to telus test.

## Get home

### Request

`GET /`

    curl -i -H 'Accept: application/json' http://localhost:5000/

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    []

## Get users

Execute function for get users data and create files

### Request

`GET /`

    curl -i -H 'Accept: application/json' http://localhost:5000/users

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    []

