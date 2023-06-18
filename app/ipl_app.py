from flask import *
from joblib import load
import numpy as np
import json
import sqlite3
from flask_mail import *

with open(r"D:\Ravikumar\Git\ravikumar\app_service\app\config.json",'r') as f:
   par = json.load(f)['params']
with open(r"D:\Ravikumar\Git\ravikumar\app_service\app\config.json",'r') as f:
   model=json.load(f)['models']
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
   return render_template("work.html",params=par,mod=list(model.keys()))
@app.route("/work/<string:model_slug>",methods=["GET"])
def work_slug(model_slug):
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
   return render_template("work.html",params=par,mod=model)



@app.route("/work/ipl_fsp",methods=[ "POST"])
def ipl_final_predict(model_slug):
   inning=[request.form.get("inning")]
   teams={0: 'Chennai Super Kings',1: 'Delhi Capitals',2: 'Delhi Daredevils',
         3: 'Gujarat Lions',4: 'Kings XI Punjab',5: 'Kolkata Knight Riders',
         6: 'Mumbai Indians',7: 'Pune Warriors',8: 'Rajasthan Royals',9: 'Rising Pune Supergiant',
         10: 'Rising Pune Supergiants',11: 'Royal Challengers Bangalore',12: 'Sunrisers Hyderabad'}
   
   stadiums={0: 'ACA-VDCA Stadium',1: 'Barabati Stadium',2: 'Brabourne Stadium',3: 'Buffalo Park',4: 'De Beers Diamond Oval',5: 'Dr DY Patil Sports Academy',6: 'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium',
      7: 'Dubai International Cricket Stadium',8: 'Eden Gardens',9: 'Feroz Shah Kotla',10: 'Feroz Shah Kotla Ground',11: 'Green Park',12: 'Himachal Pradesh Cricket Association Stadium',13: 'Holkar Cricket Stadium',14: 'IS Bindra Stadium',
      15: 'JSCA International Stadium Complex',16: 'Kingsmead',17: 'M Chinnaswamy Stadium',18: 'M. A. Chidambaram Stadium',19: 'M. Chinnaswamy Stadium',20: 'MA Chidambaram Stadium, Chepauk',
      21: 'Maharashtra Cricket Association Stadium',22: 'New Wanderers Stadium',23: 'Newlands',24: 'OUTsurance Oval',25: 'Punjab Cricket Association IS Bindra Stadium, Mohali',26: 'Punjab Cricket Association Stadium, Mohali',
      27: 'Rajiv Gandhi International Stadium, Uppal',28: 'Rajiv Gandhi Intl. Cricket Stadium',29: 'Sardar Patel Stadium, Motera',30: 'Saurashtra Cricket Association Stadium',31: 'Sawai Mansingh Stadium',
      32: 'Shaheed Veer Narayan Singh International Stadium',33: 'Sharjah Cricket Stadium',34: 'Sheikh Zayed Stadium',35: "St George's Park",36: "Subrata Roy Sahara Stadium",37: 'SuperSport Park', 38: "Wankhede Stadium"}
   stadium=request.form.get('stadium')
   venue=[key for key,value in stadiums.items() if value==stadium ]
   batting_teams=['Chennai Super Kings batting team', 'Delhi Capitals batting team','Gujarat Lions batting team', 'Kings XI Punjab batting team',
       'Kolkata Knight Riders batting team','Mumbai Indians batting team', 'Pune Warriors batting team','Rajasthan Royals batting team',
       'Royal Challengers Bangalore batting team','Sunrisers Hyderabad batting team']
   
   bowling_teams=['Chennai Super Kings bowling  team', 'Delhi Capitals bowling team','Gujarat Lions bowling team', 'Kings XI Punjab bowling team',
       'Kolkata Knight Riders bowling team','Mumbai Indians bowling team', 'Pune Warriors bowling team','Rajasthan Royals bowling team',
       'Royal Challengers Bangalore bowling team','Sunrisers Hyderabad bowling team']
   team1=request.form.get('team1')
   team2=request.form.get('team2')
   if(team1==team2):
      print ("invalid team")
      return render_template("model.html",params=par)
   else:  
      bat=request.form.get('batting_team') 
      bowl=request.form.get('bowling_team')
      if(bat==bowl):
         print("invalid selection")
         return render_template("work.html",params=par)
      else:
         ba_t=[1 if x==bat else 0 for x in batting_teams ]
         bo_t=[1 if x==bowl else 0 for x in bowling_teams ]
         team_A=[key for key,value in teams.items() if value==team1]
         team_B=[key for key,value in teams.items() if value==team2]
         toss_winners=[teams[team_A[0]],teams[team_B[0]]]
         toss=request.form.get('toss_win')
         if toss==toss_winners[0]:
            toss_winner=[key for key,value in teams.items() if value==toss]
         else:
            toss_winner=[key for key,value in teams.items() if value==toss_winners[1]]
         toss_decisions=["feild","bat"]
         toss_taken=request.form.get('toss_decision')
         if toss_taken==toss_decisions[0]:
            toss_decision=[1]
         else:
            toss_decision=[0]
         powerplay_runs=[request.form.get("powerplay_runs")]
         powerplay_wickets=[request.form.get("powerplay_wickets")]
         powerplay_run_rate=[powerplay_runs[0]/6]
         input_list=inning+venue+ba_t+bo_t+team1+team2+toss_winner+toss_decision+powerplay_runs+powerplay_wickets+powerplay_run_rate
         m=load(model['ipl_model_2'])
         return render_template("model.html",params=par,model=m)

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























   
