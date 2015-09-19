#coding=utf-8
from config import *
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

class Members(db.Model):
	name = db.Column(db.String(80), primary_key=True)
	email = db.Column(db.String(80), unique=True)
	qq = db.Column(db.String(80), unique=True)
	telephone = db.Column(db.String(80), unique=True)
	ideas = db.Column(db.String(600), unique=False)

	def __init__(self, name, email, qq, telephone, ideas):
		self.name = name
		self.email = email
		self.qq = qq
		self.telephone = telephone
		self.ideas = ideas

	def __repr__(self):
		return "<Members %r>" % self.name

