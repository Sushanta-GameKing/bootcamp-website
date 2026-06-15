from flask import Flask,render_template,request
from register import register_bp
import admin
import db

db.init_db()
app = Flask(__name__)
app.register_blueprint(register_bp)
app.register_blueprint(admin.admin_bp)

@app.route("/")
def homePage():
    return render_template("home.html")

@app.route("/candidates")
def candidates():
    return render_template("candidates.html", candidates=db.get_all_candidates())

if ( __name__ == "__main__"):
    app.run(debug=False)