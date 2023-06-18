import json
from flask_mail import *
from flask import *
with open("config.json",'r') as f:
   par = json.load(f)['params']
app=Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = par['gmail-user']
app.config['MAIL_PASSWORD'] = par['gmail-pass']
mail = Mail(app)
with app.app_context():
   send_mess = Message("you got a mail from ",
                  sender='test@gmail.com',
                  recipients=[par['gmail-user']])
   print("hi")
   mail.send(send_mess)
