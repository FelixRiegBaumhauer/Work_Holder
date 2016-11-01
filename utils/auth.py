#everything concerning the verifying of logins is done here
import hashlib, sqlite3


#def check_if_exists(col, val):
    

#Return True if it works, false otherwise
def verify(username, password):

    f="data/data.db"
    db = sqlite3.connect(f);
    c = db.cursor()

    #=================================================

    c.execute("SELECT password FROM users WHERE username="+"'"+username+"'"+";")
    pass_hold = c.fetchall()

    #the for loops only fire if there is something in pass_hold,
    #thus, if there is no account for that user, then pass_hold is empty
    #and as a result the for never fires and False is retuned
    #False is also returned if the password doesn't match the one in the db
    
    for line in pass_hold:
        for entry in line:
            if(password == entry):
                return True
    return False
    #=================================================

    db.commit()
    db.close()
    
#print(verify('rabbit','33esss'))
#print(verify('erabbit','33fesss'))

