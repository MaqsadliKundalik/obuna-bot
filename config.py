from dotenv import load_dotenv
import os   

load_dotenv()

TOKEN = os.getenv("TOKEN")
ADMINS = [123456789]

CARD_NUMBER = os.getenv("CARD_NUMBER")
CARD_NAME = os.getenv("CARD_NAME")
PRICE = 25_000
GROUP_ID = -1001234567890 
SUBSCRIBE_DAY = 30