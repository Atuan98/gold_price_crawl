from config import MONGO_DB_HOST, MONGO_DB_PORT, MONGO_DB_USERNAME, MONGO_DB_PASSWORD
from urllib.parse import quote_plus

uri = "mongodb://%s:%s@%s" % (
            quote_plus(MONGO_DB_USERNAME), quote_plus(MONGO_DB_PASSWORD), MONGO_DB_HOST)