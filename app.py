from flask import Flask,render_template,request
import db

db.init_db()
app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template("home.html")

@app.route("/candidates")
def candidates():
    return render_template("candidates.html",candidates = db.get_all_candidates())

@app.route("/register",methods = ['GET','POST'])
def register():
    return render_template("register.html")
if ( __name__ == "__main__"):
    app.run(debug=False)