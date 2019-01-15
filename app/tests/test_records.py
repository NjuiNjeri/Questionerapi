
import os
from datetime import datetime
import pytest
import unittest
import json
from app.api.v1.views.recordviews import meetup
from app import create_app

'''Test user can access all meetup records'''
class TestMeetupRecords(unittest.TestCase):
    
    def setUp(self):

        self.app = create_app()
        self.client = self.app
        self.createMeetup={}

    def test_get_all_meetups(self):
        '''tests all meetups created '''
        result = self.client().get('/api/v1/allmeetups', content_type='application/json')
        self.assertEqual(result.status_code, 200)

    def test_create_endpoint(self):
        ''' tests whether the meetups created are availed to user'''
        result = self.client().post('/api/v1/allmeetups', data=json.dumps(self.createMeetup), content_type='application/json')
        self.assertEqual(result.status_code, 201)

if __name__ == '__main__':
    unittest.main()