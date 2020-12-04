from datetime import datetime

from click import command, echo
from flask_sqlalchemy import SQLAlchemy
from flask.cli import with_appcontext

#initialize SQLAlchemy with no seetings
db = SQLAlchemy()

class InterviewProcess(db.Model):
    """model for an interview process"""
    __tablename__ = 'interview_processes'

    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.Text, nullable=False)
    role = db.Column(db.Text, nullable=False)
    stages = db.Column(db.Text, nullable=False)
    
class Interview(db.Model):
    """model for a particular interview"""
    __tablename__ = 'interviews'

    id = db.Column(db.Integer, primary_key=True)
    interview_process = db.relationship('InterviewProcess', backref='interview')
    date = db.Column(db.DateTime, nullable=False)
    stageId = db.Column(db.Integer, nullable=False)
    stage = db.Column(db.Text, nullable=False)


class Offer(db.Model):
    """model for an offer"""
    __tablename__ = 'offers'

    id = db.Column(db.Integer, primary_key=True)
    interview_process = db.relationship('InterviewProcess', backref='interview')
    salary = db.Column(db.Integer, nullable=False)
    equity = db.Column(db.Integer, default=0)


@command("init-db")
@with_appcontext
def init_db_command():
    """Initialize the database"""
    db.create_all()
    echo("Initialize the database.")

def init_app(app):
    """Initialize the Flask app for database usage"""
    db.init_app(app)
    app.cli.add_command(init_db_command)
