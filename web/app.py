from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def first():
    return render_template('interface.html')

@app.route('/hidden')
def hidden():
    return render_template('secret.html')