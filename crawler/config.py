import os

MONGO_DB_HOST = os.getenv("MONGO_DB_HOST", "localhost")
MONGO_DB_PORT = int(os.getenv("MONGO_DB_PORT", "27017"))
MONGO_DB_USERNAME = os.getenv("MONGO_DB_USERNAME","igold")
MONGO_DB_PASSWORD = os.getenv("MONGO_DB_PASSWORD","ZSE45rdx")
LOOP_TIMEOUT = int(os.getenv("LOOP_TIMEOUT", "60"))
