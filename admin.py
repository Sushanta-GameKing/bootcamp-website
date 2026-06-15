from flask import Blueprint, render_template, request, redirect
import db

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/admin", methods=["GET", "POST"])
def admin_login():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "admin123":
            return redirect("/admin/dashboard")
        else:
            return render_template("admin.html", admin_message="Invalid credentials. Please try again.")

    return render_template("admin.html")

@admin_bp.route("/admin/dashboard")
def admin_dashboard():
    candidates = db.get_all_candidates()
    pending_candidates = [c for c in candidates if c[4] == 0]
    approved_candidates = [c for c in candidates if c[4] == 1]
    total_candidates = len(candidates)
    avg_score = round(sum(candidate[3] for candidate in candidates) / total_candidates, 1) if total_candidates else 0
    return render_template(
        "admin_home.html",
        candidates=candidates,
        approved_count=len(approved_candidates),
        pending_count=len(pending_candidates),
        avg_score=avg_score
    )


@admin_bp.route("/approve")
def approve_candidates():
    candidates = db.get_all_candidates()
    pending_candidates = [c for c in candidates if c[4] == 0]
    approved_candidates = [c for c in candidates if c[4] == 1]
    total_candidates = len(candidates)
    avg_score = round(sum(candidate[3] for candidate in candidates) / total_candidates, 1) if total_candidates else 0
    return render_template(
        "admin_approve.html",
        pending_candidates=pending_candidates,
        avg_score=avg_score,
        total_candidates=total_candidates,
        approved_count=len(approved_candidates)
    )


@admin_bp.route("/managepoint")
def manage_point():
    candidates = db.get_all_candidates()
    approved_candidates = [c for c in candidates if c[4] == 1]
    total_candidates = len(candidates)
    avg_score = round(sum(candidate[3] for candidate in candidates) / total_candidates, 1) if total_candidates else 0
    return render_template(
        "admin_managepoint.html",
        approved_candidates=approved_candidates,
        avg_score=avg_score,
        total_candidates=total_candidates,
        pending_count=sum(1 for candidate in candidates if candidate[4] == 0)
    )