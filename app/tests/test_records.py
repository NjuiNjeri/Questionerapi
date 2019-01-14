import os
from datetime import datetime
import pytest
import unittest
import json
from app import create_app
from app.api.v1.views.recordviews import meetup

class TestMeetupRecords(unittest.TestCase):
    '''Test user can access all meetup records'''
    def setUp(self):

        self.app = create_app
        self.client = self.app.test_client
        self.createMeetup={}

    def test_get_all_meetups(self):
        result = self.client.get('/api/v1/Meetups', content_type='application/json')
        self.assertEqual(result.status_code, 200)

    def test_create_endpoint(self):
        result = self.client.post('/api/v1/Meetups', content_type='application/json')
        self.assertEqual(result.status_code, 201)

if __name__ == '__main__':
    unittest.main()