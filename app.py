from flask import Flask, render_template, request
from main import age_cal

app = Flask(__name__)
pred = 0
note = 0

@app.route('/', methods = ['GET', 'POST'])
def age():
    global pred, note
    if request.method == 'POST':
        dob = request.form["dob"]
        try:
            pred = age_cal(dob)
        except Exception as e:
            print(e)
            note = 'Please type DOB in given format dd-mm-yyyy'

    return render_template('index.html', d = pred, n = note)

if __name__ == '__main__':
    app.run(debug=True)