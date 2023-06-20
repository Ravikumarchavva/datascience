from flask import *
from joblib import load
import numpy as np
import json
import sqlite3
from flask_mail import *
import numpy as np
import pickle
with open(r"D:\Ravikumar\Git\datascience\app\config.json",'r') as f:
   par = json.load(f)['params']
with open(r"D:\Ravikumar\Git\datascience\app\config.json",'r') as f:
   model_names=json.load(f)['models']
app=Flask(__name__)
with app.app_context():
   inning=int(1)
   teams={0: 'Chennai Super Kings',1: 'Delhi Capitals',2: 'Gujarat Lions',3: 'Kings XI Punjab',4: 'Kolkata Knight Riders',
          5: 'Mumbai Indians',6: 'Pune Warriors',7: 'Rajasthan Royals',8: 'Royal Challengers Bangalore',9: 'Sunrisers Hyderabad'}

   batting_teams=['Chennai Super Kings batting team', 'Delhi Capitals batting team','Gujarat Lions batting team', 'Kings XI Punjab batting team',
       'Kolkata Knight Riders batting team','Mumbai Indians batting team', 'Pune Warriors batting team','Rajasthan Royals batting team',
       'Royal Challengers Bangalore batting team','Sunrisers Hyderabad batting team']
   
   bowling_teams=['Chennai Super Kings bowling team', 'Delhi Capitals bowling team','Gujarat Lions bowling team', 'Kings XI Punjab bowling team',
       'Kolkata Knight Riders bowling team','Mumbai Indians bowling team', 'Pune Warriors bowling team','Rajasthan Royals bowling team',
       'Royal Challengers Bangalore bowling team','Sunrisers Hyderabad bowling team']
   team1="Chennai Super Kings"
   team2="Pune Warriors"
   if(team1==team2):
      print ("invalid team")
   else:  
      bat="Chennai Super Kings batting team"
      bowl="Pune Warriors bowling team"
      if(bat==bowl):
         print("invalid selection")
      else:
         ba_t=[1 if x==bat else 0 for x in batting_teams ]
         bo_t=[1 if x==bowl else 0 for x in bowling_teams ]
         team_A=[key for key,value in teams.items() if value==team1]
         team_B=[key for key,value in teams.items() if value==team2]
         print(team_B,team_A)
         toss_winners=[teams[team_A[0]],teams[team_B[0]]]
         toss="Pune Warriors"
         if toss==toss_winners[0]:
            toss_winner=[key for key,value in teams.items() if value==toss]
         else:
            toss_winner=[key for key,value in teams.items() if value==toss_winners[1]]
         toss_decisions=["feild","bat"]
         toss_taken="feild"
         if toss_taken==toss_decisions[0]:
            toss_decision=int(1)
         else:
            toss_decision=int(0)
         powerplay_runs=76
         powerplay_wickets=3
         powerplay_run_rate=float(powerplay_runs/6)
         input_list=[[inning]+ba_t+bo_t+team_A+team_B+toss_winner+[toss_decision,powerplay_runs,powerplay_wickets,powerplay_run_rate]]
         print (input_list)
         m=load(open(model_names['ipl_model_2'],"rb"))
         s=m.predict(input_list)
         print(m.predict(input_list))
         print(list(model_names.keys())[0])