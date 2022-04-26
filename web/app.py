from flask import Flask, request, render_template
from jinja2 import Environment


app = Flask(__name__)
Jinja2 = Environment()

@app.route('/')
def first():
    return render_template('interface.html')

@app.route('/robots.txt') 
def content(): 
	with open('robots.txt', 'r') as f: 
		return render_template('content.html', text=f.read()) 

@app.route('/hidden', methods=['GET'])
def hidden():
    input = request.args.get('input')
    output = Jinja2.from_string('Secret? Maybe: ' + str(input)).render()
    return render_template('secret.html', output=output)

@app.errorhandler(404)
def notfound(dir):
    return render_template("notfound.html"), 404

if __name__ == "__main__":
    app.run(debug=True)