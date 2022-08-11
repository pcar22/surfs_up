from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
# 	return 'Hello world'

coolapp = Flask(__name__)

@coolapp.route('/')
def cool_app():
	return 'This is really cool!'