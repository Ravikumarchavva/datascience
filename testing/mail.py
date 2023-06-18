import json
from flask import Flask,render_template
from flask_mail import *
with open(r"D:\Ravikumar\Git\ravikumar\app_service\app\config.json",'r') as f:
   par= json.load(f)['params']
app=Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = par['gmail-user']
app.config['MAIL_PASSWORD'] = par['gmail-pass']
mail = Mail(app)
with app.app_context():
   print("hi")
   try:
      print(par['gmail-user'])
      msg=Message("you got a mail from ",
                  sender="chavvanageswarareddy0007@gmail.com",
                  recipients=[par['gmail-user']],body="test")
      print("1")
      mail.send(msg)
      print("sent message")
   except Exception as e:
      print(e)