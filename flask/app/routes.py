from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'helen'}
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
    print("User is:", user['username'])  # Debug output
    return render_template('index.html', title='Home', user=user, posts=posts)

    #return jsonify({'title': 'Home', 'user': user}) for react
