import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or ("KWame123$%^&Bryt)(86)")
    SQLALCHEMY_DATABASE_URI = "sqlite:///attendance.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False