'''Getting into the application'''
from flask import Flask
import os
from app import create_app
app = create_app()

if __name__ == '__main__':
    app.run()