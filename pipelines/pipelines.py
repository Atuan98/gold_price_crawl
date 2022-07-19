
class JsonWriterPipeline(object):
   def __init__(self):
      self.file = open('items.json', 'w+', encoding='utf-8')

   def process_item(self, item, spider):
      line = json.dumps(dict(item), ensure_ascii=False) + "\n"
      self.file.write(line)
      return item# ITEM_PIPELINES = {
#     'myproject.pipelines.PricePipeline': 300,
#     'myproject.pipelines.JsonWriterPipeline': 800,
# }

from itemadapter import ItemAdapter
import sqlite3


class ScrapyTutorialPipeline(object):
 
# init method to initialize the database
# and create connection and tables
    def __init__(self):
        self.create_conn()
        self.create_table()
     
    # create connection method to create
    # database or use database to store scraped data
    def create_conn(self):
        self.conn = sqlite3.connect("mydata.db")
        self.curr = self.conn.cursor()
 
    # Create table method
    # using SQL commands to create table
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS prices""")
        self.curr.execute("""create table prices(
                        City TEXT, Type TEXT, Buy_Price INTEGER, Sell_Price INTEGER
                        )""")
         
# store items to databases.
    def process_item(self, item, spider):
        print(item)
        # self.putitemsintable(item)
        return item
     
    def putitemsintable(self,item):
        self.curr.execute("""insert into prices values (?)""",(
            item['Quote'][0],  # extracting item.
        ))
        self.conn.commit()