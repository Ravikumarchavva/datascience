import sqlite3

con= sqlite3.connect('d:\\Ravikumar\\Git\\ravikumar\\db-testings\\contact.db')
cur=con.cursor()
try:
    res=cur.execute('select * from chec')
    print (res.fetchall())
    con.commit()
except Exception as e:
    print (e)
    
con.close()