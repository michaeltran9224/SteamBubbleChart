# Steam Bubble Chart

## Short Description
A web app that visualizes your Steam gaming history as a bubble chart. Enter your Steam ID, and the app will display a chart with bubbles sized according to the total hours played for each game. Ideal for seeing how much time you've invested in your favorite titles.
## Long Description
Our web application's main purpose is for users to effectively correlate and visualize their hours spent on a Steam video game. By using a bubble chart format users will be able to compare their times spent on one game to another game.
We built this application in order to improve our skillset and be able to provide our friends a way to visualize how many hours they spend on steam.
## Table of Contents
* [Short Description](#Short-Description)
* [Long Description](#Long-Description)
* [Install](#Install)
  * [Backend Setup](#Flask-Backend-Setup)
  * [Frontend Setup](#React-Frontend-Setup)
* [API](#API)
* [Usage](Usage)

## Install  
### Flask Backend Setup

#### Venv activation (Optional):

```venv\Scripts\activate```

#### Create .flaskenv file with the following variables:
```
FLASK_APP= exampleapp.py
FLASK_ENV= development/production
```
#### Create .env file with the following variables:
```
STEAM_API_KEY= mysteamapikey
SQL_USER= mysqluser
SQL_NAME= mysqldatabasename
SQL_ROOT_PASSWORD= mysqlpassword
```

##### You can receive your own Steam API key via https://steamcommunity.com/dev/apikey

#### Docker prerequisites:

Docker must be installed on your machine via https://www.docker.com/products/docker-desktop/

#### To build Docker image:

```docker-compose build --no-cache```

#### To run the Docker container:

```docker-compose up -d ``` 

(the -d is optional and makes the service run in the background so you can concurrently use your terminal)

#### To shut down the Docker container:

```docker-compose down```

##### You will be able to access the flask api via http://127.0.0.1:5000/

### React Frontend Setup

## API

## Usage
