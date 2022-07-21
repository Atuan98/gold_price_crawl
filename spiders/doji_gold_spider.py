from scrapy import Spider
from scrapy.selector import Selector
import re
from spiders.mapping_data import get_area_name_code, get_type_gold_code
from datetime import datetime


class DojiGoldSpider(Spider):
    FEEDD_EXPORT_ENCODING = 'utf-8'
    name = "doji-gold-spider"
    allowed_domains = ["doji.vn"]
    start_urls = [
            "http://giavang.doji.vn/",
        ]

    def number(self, txt):
        return int(txt.replace(',', ''))

    def parse(self, response):
        ant_home = Selector(response).xpath("//*[@class = 'ant-home-price']")
        update_time = ant_home.xpath("//p/span[contains(@class, 'update-time')]/text()").get()
        update_time = ' '.join(re.findall("(\d{2}:\d{2})\s(\d{2}\/\d{2}\/\d{4})", update_time)[0])
        update_time = datetime.strptime(update_time, '%H:%M %d/%m/%Y')
        rows = ant_home.xpath(".//table/tbody/tr")
        for row in rows:
            start_col = 0
            cell = row.xpath(".//text()").getall()
            split_symbol_hyphen = cell[start_col].split("-")
            split_symbol_whitespace = cell[start_col].split(" ")
            if len(split_symbol_hyphen) > 1 :
                area = split_symbol_hyphen[0]
                type = split_symbol_hyphen[1]
            elif len(split_symbol_whitespace) > 1:
                area = split_symbol_whitespace[0]
                type = split_symbol_whitespace[1]

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
                'buyPrice': self.number(buy_price),
                'sellPrice': self.number(sell_price),
                'date_time': update_time,
                'website': self.allowed_domains[0]
            }
            yield record
