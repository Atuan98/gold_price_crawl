from scrapy import Spider
from scrapy.selector import Selector
from spiders.mapping_data import get_area_name_code, get_type_gold_code
from datetime import datetime

class DojiGoldSpider(Spider):
    FEEDD_EXPORT_ENCODING = 'utf-8'
    name = "doji-gold-spider"
    allowed_domains = ["doji.vn"]
    start_urls = [
            "http://giavang.doji.vn/",
        ]

    def parse(self, response):
        ant_home = Selector(response).xpath("//*[@class = 'ant-home-price']")
        update_time = ant_home.xpath(".//p/span/text()").get().split(" ")[3:]
        update_time = ' '.join([elem for elem in update_time])
        update_time = datetime.strptime(update_time.strip(), '%H:%M %d/%m/%Y')
        update_time = datetime.strftime(update_time, '%Y-%m-%dT%H:%M:%S.%f%z')
        rows = ant_home.xpath(".//table/tbody/tr")
        for row in rows:
            start_col = 0
            cell = row.xpath(".//text()").getall()
            title = cell[start_col].split(" ")
            if len(title) == 2:
                type = title[0]
                area = title[1]
            elif len(title) == 5:
                type = cell[start_col].split("-")[0]
                area = cell[start_col].split("-")[1]
            elif len(title) == 3:
                type = title[0]
                area = title[1] + " " + title[2]

            start_col += 1
            area = get_area_name_code(area)
            type = get_type_gold_code(type)

            start_col += 1
            buy_price = cell[start_col]

            start_col += 1
            sell_price = cell[start_col]
            record = {
                'area': area,
                'type': type,
                'buyPrice': buy_price,
                'sellPrice': sell_price,
                'date_time': update_time
            }
            yield record
