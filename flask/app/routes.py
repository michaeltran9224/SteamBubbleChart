from flask import render_template, request, jsonify, Flask
from app import app
from app.database import Post, db
import os
from dotenv import load_dotenv
import requests
from datetime import datetime,timezone

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
    print(f"Incoming request for Steam ID: {steamId}")

    url = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={STEAM_API_KEY}&steamid={steamId}&include_appinfo=true&include_played_free_games=true&include_free_sub=true&include_extended_appinfo=false&format=json"
    print(f"Requesting URL: {url}")

    try:
        response = requests.get(url)
        print(f"Steam API response status: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            print(f"Steam API response JSON: {data}")

            games = data.get('response', {}).get('games', [])
            if not games:
                print("No games found in Steam API response.")
                return jsonify({'games': []}), 200  

            game_list = []
            for game in games:
                try:
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
                except Exception as e:
                    print(f"Error processing a game: {e}")

            return jsonify({'games': game_list})
        else:
            print(f"Steam API failed: {response.status_code}, {response.text}")
            return jsonify({'error': 'Failed to fetch data from Steam API'}), 500

    except Exception as e:
        print(f"Exception in getSteamUserGames: {e}")
        return jsonify({'error': 'Internal server error'}), 500

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
            player = players[0]  # get the first (and only) player
            
            # set api gathered info to variables
            steamId = player.get('steamid')
            personaName = player.get('personaname')
            profileUrl = player.get('profileurl')
            avatar = player.get('avatar')
            realName = player.get('realname')
            lastLogoff = player.get('lastlogoff')

            # optional variables, will return none if not set by user
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

            # conditional dictionary addition since these are not always input from steam user

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

    
@app.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()  # Retrieve all posts from the database
    post_list = [
        {
            'postID': post.postID,
            'username': post.username,
            'body': post.body,
            'date': post.date.isoformat(),  # Format the datetime for JSON
            'profileID' : post.profileID
        }
        for post in posts
    ]
    return jsonify(post_list)

# Route to create a new post
@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()  # Get JSON data from request
    username = data.get('username')
    body = data.get('body')
    profileID = data.get('profileID')

    if not username or not body:
        return jsonify({'error': 'Username and body are required'}), 400

    # Create a new post
    new_post = Post(
        username=username,
        body=body,
        date=datetime.now(timezone.utc),  # Use timezone-aware datetime
        profileID=profileID
    )
    db.session.add(new_post)  # Add the new post to the session
    db.session.commit()  # Commit to save changes in the database

    return jsonify({'message': 'Post created successfully'}), 201


@app.route('/posts/<int:profileID>', methods=['GET'])
def get_posts_by_profile(profileID):
    # Query the Post model for all posts with the given profileID
    posts = Post.query.filter_by(profileID=profileID).all()

    if posts:
        # Convert posts to a list of dictionaries to jsonify
        post_list = [
            {
                'postID': post.postID,
                'username': post.username,
                'body': post.body,
                'date': post.date,
                'profileID': post.profileID
            }
            for post in posts
        ]
        return jsonify({'posts': post_list})
    else:
        # Return a 404 if no posts are found for the profileID
        return jsonify({'error': 'No posts found for this profile ID'}), 404
        



