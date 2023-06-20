from flask import *

app = Flask(__name__,template_folder="template")

@app.route('/',methods=['GET', 'POST'])
def add():
    if(request.method == 'POST'):
        n1=request.form.get('no1')
        n2=request.form.get("no2")
        sum=n1+n2
        return render_template('index.html',sum=sum)
    return render_template('index.html',sum="not")
if (__name__ == '__main__'):
    app.run(debug=True)