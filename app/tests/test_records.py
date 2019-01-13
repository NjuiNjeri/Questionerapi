import os
from datetime import datetime
import pytest
import unittest
import json
from app import create_app

from app.api.v1.models.meetuprecords import Meetup_records
from app.api.v1.views.recordviews import meetup

class TestMeetupRecords(unittest.TestCase):
    '''Test user can access all meetup records'''


    def test_get_all_meetups(self):
        result = self.client.get('/api/v1/Meetup_records', content_type='application/json')
        self.assertEqual(result.status_code, 200)

    def test_create_endpoint(self):
        result = self.client.get('/api/v1/Meetup_records', content_type='application/json')
        self.assertEqual(result.status_code, 201)

if __name__ == '__main__':
    unittest.main()