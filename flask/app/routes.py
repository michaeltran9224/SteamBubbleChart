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
    user = {'username': 'sk'}
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

@app.route('/steam/user/games/<steamId>', methods=['GET'])
def getSteamUserGames(steamId):
    url = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={STEAM_API_KEY}&steamid={steamId}&include_appinfo=true&include_played_free_games=true&include_free_sub=true&include_extended_appinfo=false&format=json"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        games = data.get('response', {}).get('games', [])

        if games:
            game_list = []
            for game in games:
                app_id = game.get('appid')
                name = game.get('name')
                playtime_forever = game.get('playtime_forever', 0)
                img_icon_url = game.get('img_icon_url')
                image_url = f"http://media.steampowered.com/steamcommunity/public/images/apps/{app_id}/{img_icon_url}.jpg"

                game_info = {
                    'app_id': app_id,
                    'name': name,
                    'playtime_forever': playtime_forever,
                    'img_icon_url': image_url
                }

                game_list.append(game_info)

            return jsonify({'games': game_list})
        else:
            return jsonify({'error': 'No games found for this Steam ID'}), 404
    else:
        print(f"Error response from Steam API: {response.status_code}, {response.text}")
        return jsonify({'error': 'Failed to fetch data from Steam API'}), 500
        
# REACT: fetch(`/steam/user/games/${steamId}`)
    #games is a list btw

#getplayersummary steam api call
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

            #will return none if not set by user
            locCountryCode = player.get('loccountrycode')
            locStateCode = player.get('locstatecode')
            locCityId = player.get('loccityid')


            # create dictionary to assign information 
            player_info = {
                'steam_id': steamId,
                'persona_name': personaName,
                'profile_url': profileUrl,
                'avatar': avatar,
                'real_name': realName,
                'last_logoff': lastLogoff
            }

            #conditional dictionary addition

            if locCountryCode:
                player_info['country_code'] = locCountryCode
            if locStateCode:
                player_info['state_code'] = locStateCode
            if locCityId:
                player_info['city_id'] = locCityId



            return jsonify(player_info)  # return as JSON
        else:
            return jsonify({'error': 'No players found for provided Steam IDs'}), 404 
    else:
        print(f"Error response from Steam API: {response.status_code}, {response.text}")
        return jsonify({'error': 'Failed to fetch data from Steam API'}), 500



    #return jsonify({'title': 'Home', 'user': user}) for react
