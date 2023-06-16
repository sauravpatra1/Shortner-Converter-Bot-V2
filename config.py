# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "c3b9a964-4662-465c-a55c-593af0c45785"))
API_HASH = os.environ.get("API_HASH", "8b73b450e3ce082cdbd5234aab6fc0ec")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6282993512:AAHBrSzO8SM56IpqVp3_X8x_aeAxFD60c98")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("971097286")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "tpsarmy")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://BUBUBHAI:saurav@cluster0.yqc7q6r.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "Owner Id")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001763285096")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "urlspay") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
