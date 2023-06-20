import json
from flask_sqlalchemy import *
from flask import *
import sqlite3
from joblib import load
app=Flask(__name__)

with open(r"D:\Ravikumar\Git\datascience\iPortfolio\config.json",'r') as f:
   par = json.load(f)['params']
with open(r"D:\Ravikumar\Git\datascience\iPortfolio\config.json",'r') as f:
   model=json.load(f)['models']
con=sqlite3.connect(par['db_uri'])
cur=con.cursor()
print("1")

with app.app_context():
    a="ravi"
    b="rspure@gmail.com"
    c="hi"
    d="bye"
    cur.execute(f"insert into Contact (name,mail,subject,message) values ('{a}','{b}','{c}','{d}')")
    cur.execute("select * from Contact")
    res=cur.fetchall()
    con.commit()
    con.close()
    print(res)