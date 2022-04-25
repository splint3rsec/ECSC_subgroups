from re import template
from flask import Flask, request, render_template, render_template_string

app = Flask(__name__)
app.run(debug=True)

@app.route('/')
def first():
    return render_template('interface.html')

@app.route('/hidden')
def hidden():
    # if request.method == 'GET':
    #     name = request.args.get('query')
    return render_template('secret.html')

@app.errorhandler(404)
def notfound(dir):
    return render_template("notfound.html"), 404