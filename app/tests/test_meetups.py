import os
import pytest
import unittest
from flask import json, jsonify
from app import create_app
from app.api.v1.views.meetviews import meetup
from app.api.v1.models.createmeetup import CreateMeetups



app = create_app()

class TestMeetups(unittest.TestCase):
    """ tests admin creates meetup """
    
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.post_meetups = {
            "meetupId": "meetupId",
            "title": "title",
            "venue": " venue"
        }
    
    def test_get_single_meetup(self):
        result = self.client().get('/api/v1/meetups', content_type='application/json')
        self.assertEqual(result.status_code, 200)

    def test_createmeetup_endpoint(self):
        '''tests that the admin can effectively create a meetup'''
        result = self.client().post('/api/v1/meetups', data=json.dumps(self.post_meetups), content_type='application/json')
        self.assertEqual(result.status_code, 201)

    def test_api_can_delete_record(self):
        res = self.client().post('/api/v1/meetups', data=json.dumps(self.post_meetups), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        response = self.client().delete('/api/v1/meetups', content_type='application/json')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()