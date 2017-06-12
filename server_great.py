import random
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "counterSecretKeyLlamas"

@app.route('/')
def index():
    try:
        session['number_answer']
    except KeyError:
        session['number_answer'] = random.randrange(0, 101)
        # print session['number_answer']
    try:
        session['result']
    except KeyError:
        session['result'] = None
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guessIt():
    guess = int(request.form['guess'])
    if guess == session['number_answer']:
        session['result'] = 'correct'
    elif guess > session['number_answer']:
        session['result'] = 'high'
    elif guess < session['number_answer']:
        session['result'] = 'low'
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('number_answer')
    session.pop('result')
    return redirect('/')

app.run(debug=True)
# Nothing after the debug line will be read.
