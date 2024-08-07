import os
from dotenv import load_dotenv

load_dotenv()

RESTAPI_URL=os.getenv('RESTAPI_URL')
DB_NAME=os.getenv('DB_NAME')