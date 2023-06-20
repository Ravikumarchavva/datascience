from flask import *
from joblib import load
import numpy as np
import json
import sqlite3
from flask_mail import *

with open(r"D:\Ravikumar\Git\datascience\app\config.json",'r') as f:
   par = json.load(f)['params']
with open(r"D:\Ravikumar\Git\datascience\app\config.json",'r') as f:
   model_names=json.load(f)['models']
app = Flask(__name__,template_folder='template',static_folder='static')
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = par['gmail-user']
app.config['MAIL_PASSWORD'] = par['gmail-pass']
app.config['MAIL_ASCII_ATTACHMENTS'] = True
app.config['DEBUG'] = True
mail = Mail(app)

@app.route("/")
def home():
   return render_template("index.html",params=par)
@app.route("/about")
def about():
   return render_template("about.html",params=par)
@app.route("/work")
def work():
   model_db=sqlite3.connect(par['db_uri'])
   model_cur=model_db.cursor()
   slug_name="ipl_fsp"
   model_cur.execute(f"SELECT * FROM ml_models WHERE slug='{slug_name}'")
   mc=model_cur.fetchone()
   m={
      'name':mc[1],
      'slug':mc[2],
      'date':mc[3]
   }
   return render_template("work.html",params=par,mod=list(model_names.keys()),model_n=m)



@app.route("/ipl_fsp",methods=["GET","POST"])
def get_ipl_fsp():
   model_db=sqlite3.connect(par['db_uri'])
   model_cur=model_db.cursor()
   slug_name="ipl_fsp"
   model_cur.execute(f"SELECT * FROM ml_models WHERE slug='{slug_name}'")
   mc=model_cur.fetchone()
   model={
      'name':mc[1],
      'slug':mc[2],
      'date':mc[3]
   }
   m=load(open(model_names['ipl_model_2'],"rb"))
   if(request.method == 'POST'):
      inning=request.form.get("inning")
      teams={  0: 'Chennai Super Kings',1: 'Delhi Capitals',2: 'Gujarat Lions',3: 'Kings XI Punjab',4: 'Kolkata Knight Riders',
            5: 'Mumbai Indians',6: 'Pune Warriors',7: 'Rajasthan Royals',8: 'Royal Challengers Bangalore',9: 'Sunrisers Hyderabad'}

      batting_teams=['Chennai Super Kings batting team', 'Delhi Capitals batting team','Gujarat Lions batting team', 'Kings XI Punjab batting team',
         'Kolkata Knight Riders batting team','Mumbai Indians batting team', 'Pune Warriors batting team','Rajasthan Royals batting team',
         'Royal Challengers Bangalore batting team','Sunrisers Hyderabad batting team']
      
      bowling_teams=['Chennai Super Kings bowling team', 'Delhi Capitals bowling team','Gujarat Lions bowling team', 'Kings XI Punjab bowling team',
         'Kolkata Knight Riders bowling team','Mumbai Indians bowling team', 'Pune Warriors bowling team','Rajasthan Royals bowling team',
         'Royal Challengers Bangalore bowling team','Sunrisers Hyderabad bowling team']
      team1=request.form['team1']
      team2=request.form['team2']
      if(team1==team2):
         return render_template("model.html",params=par,mod=model,score="invalid_team",t=teams,ba_t=batting_teams,bo_t=bowling_teams)
      bat=request.form.get('batting_team')
      bowl=request.form.get('bowling_team')
      if(bat==bowl):
         return render_template("model.html",params=par,mod=model,score="invalid_selection",t=teams,ba_t=batting_teams,bo_t=bowling_teams)
      ba_t=[1 if x==bat else 0 for x in batting_teams ]
      bo_t=[1 if x==bowl else 0 for x in bowling_teams ]
      toss=request.form['toss_win']
      if toss==team1:
         toss_winner=team1
      else:
         toss_winner=team2
      toss_decisions=["feild","bat"]
      toss_taken=request.form.get('toss_decision')
      if toss_taken==toss_decisions[0]:
         toss_decision=1
      else:
         toss_decision=0
      powerplay_runs=request.form.get("powerplay_runs")
      powerplay_wickets=request.form.get("powerplay_wickets")
      powerplay_run_rate=int(powerplay_runs)/6
      print(inning,ba_t,bo_t,team1,team2,toss_winner,toss_decision,powerplay_run_rate,powerplay_wickets,powerplay_runs)
      input_list=[[int(inning)]+ba_t+bo_t+[int(team1),int(team2)]+[int(toss_winner)]+[toss_decision,int(powerplay_runs),int(powerplay_wickets),powerplay_run_rate]]
      print(input_list)
      s=m.predict(input_list)
      return render_template("model.html",params=par,mod=model,score=s,t=teams,ba_t=batting_teams,bo_t=bowling_teams)
   return render_template("model.html",params=par,mod=model,score="calculate",t=teams,ba_t=batting_teams,bo_t=bowling_teams)

@app.route("/services")
def services():
   return render_template("services.html",params=par)
@app.route("/blog")
def blog():
   return render_template("blog.html",params=par)
@app.route("/contact",methods=['GET','POST'])
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
      send_mess = Message("you got a mail from "+ username,
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
   return render_template("contact.html",params=par)



if (__name__ == "__main__"):
   app.run(debug=True)