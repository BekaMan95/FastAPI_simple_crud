import os


APP_NAME=os.getenv('APP_NAME', 'FastAPI')
APP_ENV=os.getenv('APP_ENV', 'local')

APP_DEBUG=os.getenv('APP_DEBUG', True)
APP_TIMEZONE=os.getenv('APP_TIMEZONE', 'UTC')
APP_URL=os.getenv('APP_URL', 'http://localhost')


LOG_CHANNEL=os.getenv('LOG_CHANNEL', 'stack')
LOG_STACK=os.getenv('LOG_STACK', 'single')
LOG_DEPRECATIONS_CHANNEL=os.getenv('APP_NAME', None)
LOG_LEVEL=os.getenv('LOG_LEVEL', 'debug')


DB_CONNECTION = 'mysql'
DB_CONNECTION_LIB = 'pymysql'
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_DATABASE = 'fastapi'
DB_USERNAME = 'username'
DB_PASSWORD = 'password'

DEBUG = os.getenv('DEBUG', True)
SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
DATABASE_URL = os.getenv('DATABASE_URL', f'{DB_CONNECTION}+{DB_CONNECTION_LIB}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}')

# DATABASE_URL like "sqlite+pysqlite://username:password@localhost:3306/db_name"
