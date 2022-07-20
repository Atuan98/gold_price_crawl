from scrapy import Spider
from scrapy.selector import Selector
from spiders.mapping_data import get_area_name_code, get_type_gold_code
from datetime import datetime

class PnjGoldSpider(Spider):
    FEED_EXPORT_ENCODING = 'utf-8'
    name = "pnj-gold-spider"
    allowed_domains = ["pnj.com.vn"]
    start_urls = [
            "https://giavang.pnj.com.vn",
        ]
    def parse(self, response):
        portlet = Selector(response).xpath("//*[starts-with(@id, 'portlet_com_pnj_gold_price_web_ViewGoldPricePortlet_INSTANCE')]")
        rows = portlet.xpath('.//table/tbody/tr')

        area = ""
        for row in rows:
            cells = row.xpath(".//td/text()").getall()
            start_col = 0
            if len(cells) == 5:
                area = get_area_name_code(cells[start_col])
                next_area = area
                start_col = 1
            elif len(cells) == 4:
                area = next_area

            type = get_type_gold_code(cells[start_col])

            start_col += 1
            buy_price = cells[start_col]

            start_col += 1
            sell_price = cells[start_col]

            start_col += 1
            update_time = cells[start_col]
            update_time = datetime.strptime(update_time.strip(), '%d/%m/%Y %H:%M:%S')
            update_time = datetime.strftime(update_time, '%Y-%m-%dT%H:%M:%S.%f%z')
            record = {
                'area': area,
                'type': type,
                'buyPrice': buy_price,
                'sellPrice': sell_price,
                'date_time': update_time
            }
            yield record