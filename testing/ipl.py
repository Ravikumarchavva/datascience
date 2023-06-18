from flask import *
from joblib import load
import numpy as np
import json
import sqlite3
from flask_mail import *
import numpy as np
with open(r"D:\Ravikumar\Git\ravikumar\app_service\app\config.json",'r') as f:
   par = json.load(f)['params']
with open(r"D:\Ravikumar\Git\ravikumar\app_service\app\config.json",'r') as f:
   model=json.load(f)['models']
app=Flask(__name__)
with app.app_context():
   inning=[1]
   teams={0: 'Chennai Super Kings',1: 'Delhi Capitals',2: 'Gujarat Lions',3: 'Kings XI Punjab',4: 'Kolkata Knight Riders',
         5: 'Mumbai Indians',6: 'Pune Warriors',7: 'Rajasthan Royals',8: 'Royal Challengers Bangalore',9: 'Sunrisers Hyderabad'}

   batting_teams=['Chennai Super Kings batting team', 'Delhi Capitals batting team','Gujarat Lions batting team', 'Kings XI Punjab batting team',
       'Kolkata Knight Riders batting team','Mumbai Indians batting team', 'Pune Warriors batting team','Rajasthan Royals batting team',
       'Royal Challengers Bangalore batting team','Sunrisers Hyderabad batting team']
   
   bowling_teams=['Chennai Super Kings bowling  team', 'Delhi Capitals bowling team','Gujarat Lions bowling team', 'Kings XI Punjab bowling team',
       'Kolkata Knight Riders bowling team','Mumbai Indians bowling team', 'Pune Warriors bowling team','Rajasthan Royals bowling team',
       'Royal Challengers Bangalore bowling team','Sunrisers Hyderabad bowling team']
   
   ba_t=[1 if x=="Chennai Super Kings batting team" else 0 for x in batting_teams ]
   bo_t=[1 if x=="Sunrisers Hyderabad bowling team" else 0 for x in bowling_teams ]
   team1=[key for key,value in teams.items() if value=='Chennai Super Kings']
   team2=[key for key,value in teams.items() if value=='Sunrisers Hyderabad']
   toss_winners=[teams[team1[0]],teams[team2[0]]]
   
   x="Sunrisers Hyderabad"
   if x==toss_winners[0]:
      toss_winner=[key for key,value in teams.items() if value==x]
   else:
      toss_winner=[key for key,value in teams.items() if value==toss_winners[1]]
   toss_decisions=["feild","bat"]
   x="feild"
   if x==toss_decisions[0]:
      toss_decision=[1]
   else:
      toss_decision=[0]
   powerplay_runs=[70]
   powerplay_wickets=[2]
   powerplay_run_rate=[powerplay_runs[0]/6]
   input_list=inning+ba_t+bo_t+team1+team2+toss_winner+toss_decision+powerplay_runs+powerplay_wickets+powerplay_run_rate
   m=load(model['ipl_model_2'])
   print(input_list)
   print(teams.keys())
   print(m.predict([input_list]))