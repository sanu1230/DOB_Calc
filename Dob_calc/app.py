from flask import Flask, render_template, request
from main import age_cal

app = Flask(__name__)
pred = 0 

@app.route('/', methods = ['GET', 'POST'])
def age():
    global pred
    if request.method == 'POST':
        dob = request.form["dob"]
        pred = age_cal(dob)
    return render_template('index.html', d = pred)

if __name__ == '__main__':
    app.run(debug=True)