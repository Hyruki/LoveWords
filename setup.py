from flask import Flask, render_template, request, session, redirect
from utils import *
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mysqldb import MySQL


app = Flask(__name__)

"""# ONLINE MYSQL
app.config["MYSQL_HOST"] = "sql7.freesqldatabase.com"
app.config["MYSQL_USER"] = "sql7718001"
app.config["MYSQL_PASSWORD"] = "A5z86wrGha"
app.config["MYSQL_DB"] = "sql7718001"""

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "data"

app.secret_key = 'secret_key'

mysql = MySQL(app)


