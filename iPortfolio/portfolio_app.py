from flask import *
from joblib import load
import numpy as np
import json
import sqlite3
from flask_mail import *

with open(r"D:\Ravikumar\Git\ravikumar\web_app\iPortfolio\config.json",'r') as f:
   par = json.load(f)['params']
with open(r"D:\Ravikumar\Git\ravikumar\web_app\iPortfolio\config.json",'r') as f:
   model=json.load(f)['models']
app = Flask(__name__,template_folder='templates',static_folder='static')
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = par['gmail-user']
app.config['MAIL_PASSWORD'] = par['gmail-pass']
app.config['MAIL_ASCII_ATTACHMENTS'] = True
app.config['DEBUG'] = True
mail = Mail(app)
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html',params=par)

if (__name__ == "__main__"):
   app.run(debug=True)
