import sqla_wrapper
import os


# SQLITE_FILE = ':memory:'
SQLITE_FILE = 'LOCALHOST.sqlite'

# db = sqla_wrapper.SQLAlchemy(os.getenv("DATABASE_URL", f"sqlite:///{SQLITE_FILE}"))
db = sqla_wrapper.SQLAlchemy("postgres://azwjhwhjyjkkli:bc0dda017d91dcf67793ac5c4cc7f23ba511e3555b684fb6dc786ffc482f6569@ec2-54-217-243-19.eu-west-1.compute.amazonaws.com:5432/d6km9nn8q8c19r")

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    session_token = db.Column(db.String, nullable=True)
    session_expiry_datetime = db.Column(db.DateTime, nullable=True)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    description = db.Column(db.String, unique=True)

class Receipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    description = db.Column(db.String, unique=True)




    # def __init__(self, name, description):
    #     self.name = name
    #     self.description = description
