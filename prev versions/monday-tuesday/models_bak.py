

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User( DB.Model):
	""" Twitter users that we're pulling and analyzing tweets for """
	id = DB.Column( DB.BigInteger, primary_key= True)
	username = DB.Column( DB.String( 15), nullable= False)

class Tweet( DB.Model):
	""" Tweet tweet """
	id = DB.Column( DB.Integer, primary_key= True)
	text = DB.Column( DB.Unicode( 280))
	


