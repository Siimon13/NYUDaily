from pymongo import MongoClient

client = MongoClient()
db = client.pcparts
	
# def register(username, password):
# 	conn = Dconn('users.db')
#         c = conn.cursor()
# 	c.execute('Select * from users where username= ? ',(username,))
#         check = c.fetchone();
# 	if check is not None:
# 		return "User already exists"
# 	else:
# 		c.execute('INSERT into users VALUES (?,?)', (username,password))
#                 conn.commit
#                 return True
	
# def login(username,password):
# 	c = conn('users.db')
# 	c[1].execute('Select * from users where username=? where password=?',(username,password))
# 	if c[1].rowcount > 0:
# 		return "Incorrect Info."
# 	else:
# 		return True

def register(username,password):
        if(db.users.find({"username":username}).count()) != 0:
                return "There is a account with that username"
        elif(chkpw != password):
                return "Passwords aren't the same"
        else:
                db.users.insert({'username':username, 'password' : password})
                return True

def login(user,password):
        check=db.users.find_one({'username':user,'password':password}, fields={'_id':False})
        if (db.users.find({"username":user}).count()) == 0:
                return "No account with that username"
        elif check == None:
                return "Username or password is invalid"
        else:
                return True

def add(username,school,classes,time):
        user = db.users.update({'username':username},{$addToSet: {tags: {$each ["schools","class","time"]}}
                             }
        
        
        
	
	
