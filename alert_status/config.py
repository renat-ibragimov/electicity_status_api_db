import os

from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_LOCAL_PORT = os.getenv('DB_LOCAL_PORT')

TG_API_ID = os.getenv('TG_API_ID')
TG_API_HASH = os.getenv('TG_API_HASH')

PRIMORSKII_COURT_BOT_TOKEN = os.getenv('PRIMORSKII_COURT_BOT_TOKEN')
PRIMORSKII_COURT_CHANNEL_ID = os.getenv('PRIMORSKII_COURT_CHANNEL_ID')

SOURCE_CHANNEL_NAME = os.getenv('SOURCE_CHANNEL_NAME')

ALERT_ON = os.getenv('ALERT_ON')
ALERT_OFF = os.getenv('ALERT_OFF')
