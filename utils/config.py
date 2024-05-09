from dotenv import load_dotenv
import os

load_dotenv()

prefix = os.environ.get("PREFIX_BOT")
token = os.environ.get("TOKEN")
token_seller = os.environ.get("TOKEN_SELLER")
fidea_api = os.environ.get("FIDEA_API")
