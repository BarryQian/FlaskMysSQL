from flask import Flask
from flask_bootstrap import Bootstrap
from flaskapp import views


app = Flask(__name__)
Bootstrap(app)
