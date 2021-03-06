import unittest
import json
from app.api.v1.views import rsvpviews
from app.api.v1.models.RSVPmeetup import RSVP

from app import create_app
app = create_app

class TestRSVP(unittest.TestCase):
    '''Will check the availble RSVPs'''
    def test_dict(self):
        doc = rsvp.RSVP("test name", "email", "1")
        with rsvp.app.test_request_context():
            assert doc.dict() == {
                "_id": "1",
                "name": "test name",
                "email": "email",
                "links": {
                    "self": ("/api/rsvps/1")
                }
            }

    def test_new(self):
        self.rsvp = RSVP
        doc = RSVP.new("test name", "test@example.com")
        assert doc.name == "test name"
        assert doc.email == "test@example.com"
        assert doc._id is not None

        assert RSVP.find_one(doc._id) is not None
        assert len(RSVP.find_all()) == 1

    