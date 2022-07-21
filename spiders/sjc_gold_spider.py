from scrapy.crawler import CrawlerProcess
from scrapy.spiders import XMLFeedSpider
from spiders.mapping_data import get_area_name_code, get_type_gold_code
import time
from datetime import datetime


class SjcGoldSpider(XMLFeedSpider):
    FEED_EXPORT_ENCODING = 'utf-8'
    name = 'sjc-price-spider'
    allowed_domains = ['sjc.com.vn']
    itertag = 'ratelist'

    def __init__(self, *args):
        self.start_urls = [f"https://sjc.com.vn/xml/tygiavang.xml?t={int(time.time() * 1000)}"]
        super(SjcGoldSpider, *args)

    def number(self, txt):
        return int(txt.replace('.', ''))

    def parse_node(self, response, selector):
        update_time = selector.xpath("@updated").get()
        update_time = datetime.strptime(update_time.strip(), '%I:%M:%S %p %d/%m/%Y')
        print(update_time)
        tag_city = selector.xpath("//city")
        for city in tag_city:
            city_name = city.xpath('@name').get()
            items = city.xpath(".//item")
            for item in items:
                record = {
                    'area': get_area_name_code(city_name),
                    'type': get_type_gold_code(item.xpath('@type').get()),
                    'buyPrice': self.number(item.xpath('@buy').get()),
                    'sellPrice': self.number(item.xpath('@sell').get()),
                    'date_time': update_time,
                    'website': self.allowed_domains[0]
                }
                yield record