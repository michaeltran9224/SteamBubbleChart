from flask import render_template, request, jsonify, Flask
from app import app
import os
from dotenv import load_dotenv
import requests

load_dotenv()
#api key from .env
STEAM_API_KEY = os.getenv('STEAM_API_KEY')

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'michael'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    print(f"Using Steam API Key: {STEAM_API_KEY}")  # Debug output
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/steam/user/<steamId>', methods=['GET'])
def getSteamUser(steamId):
    url = f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={STEAM_API_KEY}&steamids={steamId}&format=json"

    response = requests.get(url)

    if response.status_code == 200:  #checks if request was success
        data = response.json()
        players = data.get('response', {}).get('players', [])

        if players:
            player = players[0]  # Get the first (and only) player
            
            # set info to vars
            steamId = player.get('steamid')
            personaName = player.get('personaname')
            profileUrl = player.get('profileurl')
            avatar = player.get('avatar')
            realName = player.get('realname')
            lastLogoff = player.get('lastlogoff')

            # create dictionary
            player_info = {
                'steam_id': steamId,
                'persona_name': personaName,
                'profile_url': profileUrl,
                'avatar': avatar,
                'real_name': realName,
                'last_logoff': lastLogoff
            }
            return jsonify(player_info)  # return as JSON
        else:
            return jsonify({'error': 'No players found for provided Steam IDs'}), 404 
    else:
        print(f"Error response from Steam API: {response.status_code}, {response.text}")
        return jsonify({'error': 'Failed to fetch data from Steam API'}), 500



    #return jsonify({'title': 'Home', 'user': user}) for react
