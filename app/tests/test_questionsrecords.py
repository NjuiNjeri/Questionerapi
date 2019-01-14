import os
from datetime import datetime
import pytest
import unittest
import json
# from app import create_app
from app.api.v1.views import questionviews


from app import create_app


'''test question endpoints'''
class TestQuestions(unittest.TestCase):
    def setUp(self):
        
        self.app = create_app()
        self.client = self.app.test_client
        self.post_question = {
            "meetupid": "meetup_id",
            "question": "question",
            "title": "title"
        }

    def test_get_all_meetups(self):
        '''tests all questions sent to meetups'''
        result = self.client().get('/api/v1/questions', content_type='application/json')
        self.assertEqual(result.status_code, 200)
        

    def test_create_endpoint(self):
        '''tests that the questions are actually seen at the endpoint'''
        result = self.client().post('/api/v1/questions', data=json.dumps(self.post_question), content_type='application/json')
        self.assertEqual(result.status_code, 201)

if __name__ == '__main__':
    unittest.main()