from flask import Flask, Blueprint, jsonify, render_template
from app.api.v1.models.RSVPmeetup import RSVP

v1_rsvp=Blueprint('RSVP', __name__, url_prefix='/api/v1/RSVP')


@app.route('/')
def rsvp():
    _items = db.rsvpdata.find()
    items = [item for item in _items]
    count = len(items)
    hostname = socket.gethostname()
    return render_template('profile.html', counter=count, hostname=hostname,\)