import os

MONGO_DB_HOST = os.getenv("MONGO_DB_HOST", "localhost")
LOOP_TIMEOUT = int(os.getenv("LOOP_TIMEOUT", "30"))
