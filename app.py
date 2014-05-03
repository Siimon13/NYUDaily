from flask import Flask, render_template, redirect, session, request
from pymongo import MongoClient
import auth

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
	return render_template("index.html")
	
@app.route("/login",methods=["GET","POST"])
def login():
	if request.method == "GET":
		return render_template('login.html')
	else:
		username = request.form['username'].encode('ascii','ignore')
		password = request.form['password'].encode('ascii','ignore')	
		if auth.login(username,password):
			session['username'] = username
		else:
			return redirect('/login', message = auth.login(username,password))
		
@app.route("/register",methods=["GET","POST"])
def register():
	if request.method == "GET":
		return render_template('register.html')
	else:
		username = request.form['username'].encode('ascii','ignore')
		password = request.form['password'].encode('ascii','ignore')
                print username
                print password
		if auth.register(username,password):
                        print "Auth.register worked!"
			return redirect('/login')
		else:
			return render_template('register.html',message= auth.register(username,password))
			
if __name__ == "__main__":
	app.debug = True
	app.run()
