#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "21304205"))
API_HASH = environ.get("API_HASH", "f33a167f27ebf022b2c9dc876c11a642")
BOT_TOKEN = environ.get("BOT_TOKEN", "8478628373:AAEc6wmf0XhVt6jB4VWNZfmI_XqAmf8LNt8")

OWNER = int(environ.get("OWNER", "1444148191"))
CREDIT = environ.get("CREDIT", "Pramod026")

TOTAL_USER = os.environ.get('TOTAL_USERS', '1444148191').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '1444148191').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

