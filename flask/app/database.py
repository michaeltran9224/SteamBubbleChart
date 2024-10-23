from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

db = SQLAlchemy()

class Post(db.Model):
    postID = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(16), nullable=False)
    body = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

def create_database(app):
    with app.app_context():
        db.create_all()  # Create the tables in the database

        # Create a post if none exist
        if not Post.query.first():  # Check if there are no posts
            new_post = Post(
                postID=1,  # Use an integer ID
                body="This is the content of my first post.",
                username="Michael",
                date=datetime.now(timezone.utc)  # Use timezone-aware datetime
            )
            db.session.add(new_post)  # Add the post to the session
            db.session.commit()  # Commit the session to save changes
            print("Created a new post.")  # Optional: Confirm the creation


# Fetch all posts
# posts = Post.query.all()

# Fetch a post by ID
# post = Post.query.get(1)  # Assuming ID = 1

# Fetch the post to update
# post = Post.query.get(1)
# post.title = "Updated Title"
# db.session.commit()  # Save changes

# Fetch the post to delete
# post = Post.query.get(1)
# db.session.delete(post)
# db.session.commit()  # Remove the post from the database