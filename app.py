from flask import Flask, render_template, redirect, session, request
import auth

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
	return render_template("index.html")
	
@app.route("/login",methods=["GET","POST"])
def login():
	if request.method = "GET":
		return render_template('login.html')
	else:
		username = request.form['username'].encode('ascii','ignore')
		password = request.form['password'].encode('ascii','ignore')	
		if auth.login(username,password):
			session['username'] = username
		else:
			return render_template('login.html', message = auth.login(username,password))
		
@app.route("/register",methods=["GET","POST"])
def register():
	if request.method = "GET":
		return render_template('register.html')
	else:
		username = request.form['username'].encode('ascii','ignore')
		password = request.form['password'].encode('ascii','ignore')	
		if auth.register(username,password) == 'True':
			return render_template('login.html',message="Account made")
		else:
			return render_template('register.html',message= auth.register(username,password))
			
if __name__ == "__main__":
	app.debug = True
	app.run()