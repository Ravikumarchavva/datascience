from flask import *
from joblib import load
import numpy as np
import json
import sqlite3
from flask_mail import *
app=Flask(__name__)
with open(r"D:\Ravikumar\Git\ravikumar\app_service\app\config.json",'r') as f:
   par = json.load(f)['params']
print(1)
with app.app_context():
    model_db=sqlite3.connect(par['db_uri'])
    print(2)
    model_cur=model_db.cursor()
    slug_name="ipl_fsp"
    print(3)
    model_cur.execute(f"SELECT * FROM ml_models WHERE slug='{slug_name}'")
    mc=model_cur.fetchone()
    print(mc)
    print(mc[1])
    print(10)
    model={
        'name':mc[1],
        'slug':mc[2],
        'date':mc[3]
    }
    print(model['name'])
