from flask import Flask, make_response, url_for, redirect, render_template
import os
import json

app=Flask(__name__)





class RSVP(object):
    """Class for RSVP"""
    def __init__(self, name, email, _id=None):
        self.name = name
        self.email = email
        self._id = _id

    def dict(self):
        _id = str(self._id)
        return {
            "_id": _id,
            "name": self.name,
            "email": self.email,
            "links": {
                "self": "{}api/rsvps/{}".format('request.url_root, _id')
            }
        }

    