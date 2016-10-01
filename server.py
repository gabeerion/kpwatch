# server.py -- grabs user data and makes an entry in the emails database

from flask import Flask
app = Flask(__name__)

HOMEPAGE = "What is your email address?\n\nWhat city would you like alerts for?"

@app.route("/")
def homepage():
	return HOMEPAGE

@app.route("/<email>_<city>")
def cpage(email,city):
	return "You will be notified at %s when there is a Kp alert for %s." % (email,city)

app.run()