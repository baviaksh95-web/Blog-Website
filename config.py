# Configuration Settings for storing DB url's  and secret key
import os

class Config:
    SECRET_KEY = 'secretkeyapi'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False