from scrapy.crawler import CrawlerProcess
from scrapy.spiders import XMLFeedSpider
from spiders.mapping_data import get_area_name_code, get_type_gold_code
import time

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
        print(selector)
        for ratelist in selector:
            city = ratelist.xpath("@name").get()
            items = ratelist.xpath('//item')
            for item in items:
                record = {
                        'area': get_area_name_code(city),
                        'type': get_type_gold_code(item.xpath('@type').get()),
                        'buyPrice': self.number(item.xpath('@buy').get()),
                        'sellPrice': self.number(item.xpath('@sell').get()),
                        # 'date_time': update_time
                    }
                yield record