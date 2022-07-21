import pymongo
from scrapy.exceptions import DropItem


class MongoDBPipeline(object):

    def __init__(self):
        client = pymongo.MongoClient('localhost', 27017)
        crawl_db = client['gold_price']
        self.collection_daily_price = crawl_db["daily_price"]
        self.collection_area = crawl_db["area"]
        self.collection_type_gold = crawl_db["type_gold"]
        self.collection_realtime_price = crawl_db["realtime_price"]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            record_realtime = item
            current_item_realtime = self.collection_realtime_price.find_one({"area": record_realtime["area"], "type": record_realtime["type"],
                                                                      "website": record_realtime["website"]},
                                                                     sort= [("date_time", pymongo.DESCENDING)], limit = 1)
            if current_item_realtime is not None:
                current_item_realtime.pop('_id')
                if record_realtime != current_item_realtime:
                    self.collection_realtime_price.insert_one(record_realtime)
            else:
                self.collection_realtime_price.insert_one(record_realtime)

            record_daily = item
            current_item_daily = self.collection_daily_price.find_one(
                {"area": record_daily["area"], "type": record_daily["type"],
                 "website": record_daily["website"]},
                sort=[("date_time", pymongo.DESCENDING)], limit=1)

            if current_item_daily is not None:
                last_item_daily = current_item_daily.copy()
                id = current_item_daily.pop('_id')
                if record_daily != current_item_daily:
                    self.collection_daily_price.update_one({"_id": id}, {"$set": record_daily})
            else:
                self.collection_daily_price.insert_one(record_daily)

            record_area = {
                "area": item["area"],
                "website": item["website"]
            }
            current_area = self.collection_area.find_one(record_area)
            if current_area is None:
                self.collection_area.insert_one(record_area)

            record_type_gold = {
                "area": item["area"],
                "type": item["type"],
                "website": item["website"]
            }
            current_type = self.collection_type_gold.find_one(record_type_gold)

            if current_type is None:
                self.collection_type_gold.insert_one(record_type_gold)
        return item