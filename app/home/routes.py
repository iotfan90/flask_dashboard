
from app.home import blueprint
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app import login_manager, db
from jinja2 import TemplateNotFound
from app.base.models import Players


@blueprint.route('/index')
@login_required
def index():
    all_data = Players.query.all()
    return render_template("tables-tables.html", dk_nfl_players=all_data)
    # return render_template("index.html")


@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        return render_template(template)

    except TemplateNotFound:
        return render_template('page-404.html'), 404
    
    except:
        return render_template('page-500.html'), 500


#  query on all our employee data
# @blueprint.route('/')
# def Index():
#     all_data = Players.query.all()
#     return render_template("tables-tables.html", dk_nfl_players=all_data)


#  insert data to mysql database via html forms
@blueprint.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        position = request.form['position']
        team = request.form['team']
        salary = request.form['salary']
        avg_ppg = request.form['avg_ppg']
  
        my_data = Players(name, position, team, salary, avg_ppg)
        db.session.add(my_data)
        db.session.commit()
  
        flash("Players Inserted Successfully")
        return redirect(url_for('home_blueprint.index'))


#update players
@blueprint.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        avg_ppg = request.form['avg_ppg']
        my_data = Players.query.filter_by(avg_ppg=avg_ppg).first()
        # my_data.name = request.form['name']
        # my_data.position = request.form['position']
        # my_data.team = request.form['team']
        # my_data.salary = request.form['salary']
        my_data.avg_ppg = request.form['updatedAvg']
  
        db.session.commit()
        flash("Players Updated Successfully")
        return redirect(url_for('home_blueprint.index'))


#delete players
@blueprint.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    my_data = Players.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Players Deleted Successfully")
    return redirect(url_for('home_blueprint.index'))
