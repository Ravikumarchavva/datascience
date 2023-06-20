from flask import *
from joblib import load
import numpy as np
import json
import sqlite3
from flask_mail import *

with open(r"D:\Ravikumar\Git\datascience\iPortfolio\config.json",'r') as f:
   par = json.load(f)['params']
with open(r"D:\Ravikumar\Git\datascience\iPortfolio\config.json",'r') as f:
   model=json.load(f)['models']
app = Flask(__name__,template_folder='templates',static_folder='static')
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = par['gmail-user']
app.config['MAIL_PASSWORD'] = par['gmail-pass']
app.config['MAIL_ASCII_ATTACHMENTS'] = True
app.config['DEBUG'] = True
mail = Mail(app)


# @app.route("/<string:model_slug>",methods=["GET"])
# def work_slug(model_slug):
#    model_db=sqlite3.connect(par['db_uri'])
#    model_cur=model_db.cursor()
#    slug_name="ipl_fsp"
#    model_cur.execute(f"SELECT * FROM ml_models WHERE slug='{slug_name}'")
#    mc=model_cur.fetchone()
#    model={
#       'name':mc[1],
#       'slug':mc[2],
#       'date':mc[3]
#    }
#    return render_template("work.html",params=par,mod=model)

@app.route("/",methods=['GET','POST'])
def index():
   return render_template("index.html",params=par,moel=list(model.keys()))
   
def contact_form():
   if(request.method == 'POST'):
      con=sqlite3.connect(par['db_uri'])
      cur=con.cursor()
      username= request.form.get("name")
      email= request.form.get("email")
      about= request.form.get("subject")
      msg= request.form.get("message")
      try:
         cur.execute(f"insert into Contact (name,mail,subject,message) \
                     values ('{username}', '{email}','{about}','{msg}')  " )
         con.commit()
         con.close()
      except Exception as e:
         print(e)
      send_mess = Message("you got a mail ",
                  sender=email,
                  recipients=[par['gmail-user']],
                  body=msg)
      try:
         print("hi")
         mail.send(send_mess)
         print("hi")
         return "sent message"
      except Exception as e:
         print(e)
         return  "message error"



if (__name__ == "__main__"):
   app.run(debug=True)
