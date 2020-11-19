#app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import environ
from sys import exit
from decouple import config

from config import config_dict
from app import create_app, db


  
#app = Flask(__name__)
# app.secret_key = "S#cr#t_k#y"
  
# #SqlAlchemy Database Configuration With Mysql
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:kentland55@localhost/sports_data'
#                                         #mysql+pymysql://username:passwd@host/databasename 
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  
# db = SQLAlchemy(app)

# WARNING: Don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True)

# The configuration
get_config_mode = 'Debug' if DEBUG else 'Production'

try:
    
    # Load the configuration using the default values 
    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')

app = create_app(app_config)
Migrate(app, db)
  
if __name__ == "__main__":
    app.run(debug=True)
