from flask import Blueprint, render_template, request
import db

register_bp = Blueprint("register", __name__)
db.init_db()

@register_bp.route("/register", methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        candidate_name = request.form.get("full_name")
        candidate_email = request.form.get("email")

        if candidate_name and candidate_email:
            db.add_candidate(None, candidate_name, candidate_email, 0)
            return render_template("register.html", register_message="Candidate registered successfully!")
        else:
            return render_template("register.html", register_message="All fields are required.")
    
    return render_template("register.html")