# For flask object and routs
from flask import Flask, render_template, url_for, redirect, request, redirect, flash

# for sqlalchemy ORM
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from wtforms_sqlalchemy.fields import QuerySelectField
from pprint import pprint
# Flask object
app = Flask(__name__)

# Configs
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
app.config["SQLALCHEMY_TRACK-MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "mysecretkey"
