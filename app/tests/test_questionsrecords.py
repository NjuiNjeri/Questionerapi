import os
from datetime import datetime
import pytest
import unittest
import json
# from app import create_app

from app.api.v1.models.createmeetup import createmeetup


'''test question endpoints'''
class Test_Questions(unittest.TestCase):
    def setUp(self):
        
        # self.app = create_app()
        self.client = self.app.test_client()
        self.post_question = {
            "question": "question",
            "title": "title",
            "meetup_id": "meetup_id",
            "user_id": "user_id"
        }

        def test_get_all_meetups(self):
            result = self.client.get('/api/v1/questions', content_type='application/json')
        self.assertEqual(result.status_code, 200)

    def test_create_endpoint(self):
        result = self.client.get('/api/v1/questions', content_type='application/json')
        self.assertEqual(result.status_code, 201)

if __name__ == '__main__':
    unittest.main()