from os.path import dirname, join
from flask import Flask, render_template

from . import db, tracker

app = Flask(__name__)
app.config.from_mapping(
    SQLALCHEMY_DATABASE_URI="sqlite:///" + join(dirname(dirname(__file__)), "database.sqlite")
)

db.init_app(app)

app.register_blueprint(tracker.bp)

@app.errorhandler(404)

def page_not_found(e):
    return render_template("404.html"), 404

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
