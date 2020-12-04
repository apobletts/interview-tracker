from flask import Blueprint, abort, g, render_template, redirect, request, url_for

from .db import InterviewProcess, Interview, Offer, db

bp = Blueprint("interviewprocess", __name__, url_prefix="/")

def get_process_by_company(company):
    return InterviewProcess.query.filter_by(company=company)

@bp.route("/")
def index():
    processes = InterviewProcess.query()
    interviews = Interview.query().order_by(Interview.date.desc())
    return render_template("tracker/index.html", interviews=interviews, processes=processes)
    
@bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("tracker/create.html")

    process = get_process_by_company(request.form.get("company"))
    if not process:
        interviewprocess = InterviewProcess(
            company = request.form.get("company"),
            role = request.form.get("role")
        )

        db.session.add(interviewprocess)
        db.session.commit()
        process = interviewprocess
    
    interview = Interview(
        )
