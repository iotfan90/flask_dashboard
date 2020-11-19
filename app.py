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

#Creating model table for our CRUD database
class dk_nfl_players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    position = db.Column(db.String(10))
    team = db.Column(db.String(10))
    salary = db.Column(db.Integer)
    avg_ppg = db.Column(db.Float)
  
    def __init__(self, name, position, team, salary, avg_ppg):
        self.name = name
        self.position = position
        self.team = team
        self.salary = salary
        self.avg_ppg = avg_ppg


#query on all our employee data
# @app.route('/')
# def Index():
#     all_data = dk_nfl_players.query.all()
#     return render_template("index.html", dk_nfl_players = all_data)
  
# #insert data to mysql database via html forms
# @app.route('/insert', methods = ['POST'])
# def insert():
#     if request.method == 'POST':
#         name = request.form['name']
#         position = request.form['position']
#         team = request.form['team']
#         salary = request.form['salary']
#         avg_ppg = request.form['avg_ppg']
  
#         my_data = dk_nfl_players(name, position, team, salary, avg_ppg)
#         db.session.add(my_data)
#         db.session.commit()
  
#         flash("Players Inserted Successfully")
#         return redirect(url_for('Index'))
  
# #update players
# @app.route('/update', methods = ['GET', 'POST'])
# def update():
#     if request.method == 'POST':
#         my_data = dk_nfl_players.query.get(request.form.get('id'))
  
#         my_data.name = request.form['name']
#         my_data.position = request.form['position']
#         my_data.team = request.form['team']
#         my_data.salary = request.form['salary']
#         my_data.avg_ppg = request.form['avg_ppg']
  
#         db.session.commit()
#         flash("Players Updated Successfully")
#         return redirect(url_for('Index'))
  
# #delete players
# @app.route('/delete/<id>/', methods = ['GET', 'POST'])
# def delete(id):
#     my_data = dk_nfl_players.query.get(id)
#     db.session.delete(my_data)
#     db.session.commit()
#     flash("Players Deleted Successfully")
#     return redirect(url_for('Index'))
  
if __name__ == "__main__":
    app.run(debug=True)
