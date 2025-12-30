import os
from dotenv import load_dotenv

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']
load_dotenv()
key = "MyJwtLovelyKey1234567890!!1234567890"#for simplicity its here but suppose to be in .env
class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SMS4FREE_KEY = os.environ.get('SMS4FREE_KEY')
    SMS4FREE_USER = os.environ.get('SMS4FREE_USER')
    SMS4FREE_PASSWORD = os.environ.get('SMS4FREE_PASSWORD')
    AWS_ACCESSKEY = os.environ.get('AWS_ACCESSKEY')
    AWS_SECRETKEY = os.environ.get('AWS_SECRETKEY')
    BUCKET_URL = os.environ.get('BUCKET_URL')
