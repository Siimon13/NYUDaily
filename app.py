from flask import Flask, render_template, redirect, session, request
import auth

app = Flask(__name__)
app.secret_key = 'aasdfastw'

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
                        return redirect('/profile');
		else:
			return redirect('/login', message = auth.login(username,password))

@app.route("/profile",methods=["GET","POST"])
def profile():
        if 'username' in session:
                return render_template('profile.html',user = session['username']);
        elif request.method  == "GET":
                return render_template('profile.html')
        else:
                school = request.form['school'].encode('ascii','ignore')
                select = request.form['select'].encode('ascii','ignore')
                time = request.form['time'].encode('ascii','ignore')
                auth.add(session['username'],school,select,time)
                
                
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
