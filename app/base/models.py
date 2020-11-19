
from flask_login import UserMixin
from sqlalchemy import Binary, Column, Integer, String, Float
from app import db, login_manager
from app.base.util import hash_pass


class User(db.Model, UserMixin):

    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True)
    email = Column(String(100), unique=True)
    password = Column(Binary)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            if property == 'password':
                value = hash_pass(value)  # we need bytes here (not plain str)
                
            setattr(self, property, value)

    def __repr__(self):
        return str(self.username)


# Creating model table for our CRUD database
class Players(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    position = Column(String(10))
    team = Column(String(10))
    salary = Column(Integer)
    avg_ppg = Column(Float)

    def __init__(self, name, position, team, salary, avg_ppg):
        self.name = name
        self.position = position
        self.team = team
        self.salary = salary
        self.avg_ppg = avg_ppg


@login_manager.user_loader
def user_loader(id):
    return User.query.filter_by(id=id).first()


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = User.query.filter_by(username=username).first()
    return user if user else None
