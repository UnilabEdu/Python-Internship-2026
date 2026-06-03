from os import path

class Config:
    SECRET_KEY = "ALFJDSLFJO@##@!AFLJKDSFL"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(path.dirname(__file__), "test.db")
    UPLOAD_PATH = path.join(path.dirname(__file__), 'static')