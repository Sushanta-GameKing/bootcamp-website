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
    candidates = db.get_all_candidates()
    approved_candidates = [candidate for candidate in candidates if candidate[4] == 1]
    total_candidates = len(candidates)
    approved_count = len(approved_candidates)
    total_points = sum(candidate[3] for candidate in approved_candidates)
    avg_score = round(total_points / approved_count, 0) if approved_count else 0

    return render_template(
        "candidates.html",
        candidates=approved_candidates,
        total_candidates=total_candidates,
        approved_count=approved_count,
        avg_score=avg_score
    )

if ( __name__ == "__main__"):
    app.run(debug=False)