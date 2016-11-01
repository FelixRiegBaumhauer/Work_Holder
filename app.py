#Always in School Squad: Felix Rieg-Baumhauer, Asher Lasday, Sahron Lin, Sachal Malick
#Softdev pd8
#HW10 -- Da ARt of Storytellin'
#2016-11-01

#importing things, not to be touched
import utils.auth, utils.createAccount, hashlib, os

from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)    #crts Flask object

#Special things for special sessions
app.secret_key=os.urandom(32)
secret = "felixwebsite"#NOT THE REAL ONE, THAT ONE IS A SECRET,

#
#=============================Routage Starting==========================
#

@app.route("/")
def show_root():
    return render_template('auth.html')

@app.route("/home", methods=['POST'])
def authenticate():
    given_user = request.form["username"]
    given_pass = request.form["password"]

    session[secret]=given_user
    
    are_u_in = utils.auth.verify(given_user, given_pass)

    #return render_template('index.html', perm = are_u_in)

    if(are_u_in == True):
        return render_template('index.html', perm = are_u_in)
    else:
        return redirect(url_for('show_root'))

@app.route("/make_account")
def mk_one():
    return "lala"

     
@app.route("/logout")
def logger_outter():
    print session
    session.pop(secret)
    print session
    return redirect(url_for('show_root'))
            #render_template('auth.html')#"hlo"#redirect(url_for(show_root))



if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
