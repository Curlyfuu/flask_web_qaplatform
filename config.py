
import pymysql
import os

SECRET_KEY = os.urandom(24)

HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'wake_up'
USERNAME = 'root'
PASSWORD = '1606260309ww'
DB_URI   = 'mysql+pynysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI =DB_URI
