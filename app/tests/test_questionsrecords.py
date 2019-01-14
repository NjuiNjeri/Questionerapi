import os
from datetime import datetime
import pytest
import unittest
import json
# from app import create_app

from app import create_app


'''test question endpoints'''
class TestQuestions(unittest.TestCase):
    def setUp(self):
        
        self.app = create_app()
        self.client = self.app.test_client
        self.post_question = {
            "question": "question",
            "title": "title",
            "meetup_id": "meetup_id",
        }

    def test_get_all_meetups(self):
        '''tests all questions sent to meetups'''
        result = self.client().post('/api/v1/questions', content_type='application/json', data=json.dumps (self.post_question))
        print(result)
        self.assertEqual(result.status_code, 200)
        

    def test_create_endpoint(self):
        '''tests that the questions are actually seen at the endpoint'''
        result = self.client().get('/api/v1/questions', content_type='application/json')
        self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
    unittest.main()