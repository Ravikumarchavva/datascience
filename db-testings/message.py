import json
from flask_sqlalchemy import *
from flask import *
import sqlite3
app=Flask(__name__)
con=sqlite3.connect(r"D:\Ravikumar\Git\ravikumar\app_service\app\portfolio.db")
cur=con.cursor()

with app.app_context():
    cur.execute("select * from ml_models where model_name like 'ipl%'")
    res=cur.fetchone()
    res_dic={
        "id":res[0],
        "name":res[1],
    }
    print(res_dic['name'])
    con.commit()
    con.close()
    print(res)