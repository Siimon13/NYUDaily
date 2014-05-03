import sqlite3

def conn(db):
	conn = sqlite3.connect(db)
	c = conn.cursor()
	if db == 'users.db':
		c.execute(CREATE TABLE if not exists users (username text,password text))
		conn.commit
	return [conn,c]
	
def register(username, password):
	c = conn('users.db')
	c[1].execute('Select * from users where username=? ',(username,))
	if c[1].rowcount > 0:
		return "User already exists"
	else:
		c[1].execute('INSERT into users VALUES (?,?)', (username,password))
	
def login(username,password):
	c = conn('users.db')
	c[1].execute('Select * from users where username=? where password=?',(username,password))
	if c[1].rowcount > 0:
		return "Incorrect Info."
	else:
		return True;
	
	
