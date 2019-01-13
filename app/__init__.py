from flask import Flask
from app.api.v1.views.meetviews import v1_meetups as v1


def create_app():
    app = Flask(__name__)
    app.register_blueprint(v1)
    return app