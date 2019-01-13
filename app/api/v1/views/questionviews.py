from flask import jsonify, Blueprint, request, json
from ..models.questionrecords import All_Questions
from datetime import datetime
from uuid import uuid4

v1_all_questions_blueprint=('questions')