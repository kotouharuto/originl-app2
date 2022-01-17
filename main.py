from sqlite3.dbapi2 import connect
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def newac():
 dbname = ('db/user.db')
 conn = sqlite3.connect(dbname, isolation_level=None)

 return render_template('newac.html')

@app.route('/login')
def login():
 dbname = ('db/user.db')

 return render_template('login.html')

@app.route('/home')
def home_page():

 return render_template('home.html', title=title, msg=msg)



app.run(port=8000, debug=True)