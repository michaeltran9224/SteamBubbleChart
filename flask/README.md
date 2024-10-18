# Flask Backend Setup

## Venv activation:

venv\Scripts\activate

## Create .env file with the following variables:

STEAM_API_KEY={insert your Steam API key here}
FLASK_APP=hello.py
FLASK_ENV=development (if you are developing) or FLASK_ENV=production (if your product is finished)

### You can receive your own Steam API key via https://steamcommunity.com/dev/apikey

## Docker prerequisites:

Docker must be installed on your machine via https://www.docker.com/products/docker-desktop/

## To build Docker image:

docker-compose build --no-cache

## To run the Docker container:

docker-compose up -d (the -d is optional and makes the service run in the background so you can concurrently use your terminal)

## To shut down the Docker container:

docker-compose down

### You will be able to access the flask api via http://127.0.0.1:5000/
