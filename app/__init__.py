from flask import Flask
from app.api.v1.views.meetviews import v1_meetups as v1
from app.api.v1.views.questionviews import v1_all_questions_blueprint
from app.api.v1.views.recordviews import v1_meetup_blueprint

def  create_app():
    app = Flask(__name__)
    app.register_blueprint(v1)
    app.register_blueprint(v1_all_questions_blueprint)
    app.register_blueprint(v1_meetup_blueprint)
    return app