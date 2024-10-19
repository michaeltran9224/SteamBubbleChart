from flask import Flask
from flask_cors import CORS
from config import Config
import os
from dotenv import load_dotenv
from app.database import db, create_database  # Import the db and the single create_database function

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('SQL_USER')}:{os.getenv('MYSQL_ROOT_PASSWORD')}@mysql:3306/{os.getenv('SQL_NAME')}"


CORS(app)

db.init_app(app)

create_database(app)  # Create the database and initial post

from app import routes  # Import routes after initializing the app
