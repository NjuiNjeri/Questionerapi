import unittest
from flask import json
from app import create_app

from app.api.v1.models.createmeetup import CreateMeetups



app = create_app()

class TestMeetups(unittest.TestCase):
    """ tests admin creates meetup """
    
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

        # payload = {
        #     'username': username
        #     'email': email
        #     'password': password
        # }


    def test_get_all_meetups(self):
        result = self.client.get('/api/v1/meetups', content_type='application/json')
        self.assertEqual(result.status_code, 200)

    def test_create_endpoint(self):
        result = self.client.get('/api/v1/meetups', content_type='application/json')
        self.assertEqual(result.status_code, 201)

if __name__ == '__main__':
    unittest.main()