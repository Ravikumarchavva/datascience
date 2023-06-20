from flask import *

app = Flask(__name__,template_folder="template")

@app.route('/',methods=['GET', 'POST'])
def add():
    if(request.method == 'POST'):
        print(request.form['no1'])
        print(request.form["no2"])
        

    return render_template('index.html',sum="0")
if (__name__ == '__main__'):
    app.run(debug=True)