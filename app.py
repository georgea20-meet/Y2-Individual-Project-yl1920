from databases import *
from flask import Flask, render_template, url_for, request,redirect
app = Flask(__name__)

@app.route('/signup', methods=['GET' , 'POST'])
def signup():
	if request.method == 'POST':
		add_participant(request.form['name'],
			request.form['psw'],
			request.form['image'],
			request.form['Nationality'],
			request.form['Instrument'].lower(),
			request.form['How_long'],
			request.form['Type'],
			request.form['email'],
			request.form['ph_n'])
		return redirect(url_for('homepage'))

	else:

		return render_template("signup.html") 

@app.route('/')
def homepage():

	return render_template("homepage.html")

@app.route('/Participants/<string:Instrument>')
def categories(Instrument):
	profiles = query_by_instrument(Instrument)

	return render_template("profiles.html", profiles = profiles )

if __name__ == '__main__':
	app.run(debug=True)