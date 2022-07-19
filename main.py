from scrapy.crawler import CrawlerProcess
from spiders.sjc_gold_spider import SjcGoldSpider
from spiders.pnj_gold_spider import PnjGoldSpider


# process = CrawlerProcess(settings={
#     "ITEM_PIPELINES": {
#         'pipelines.json_pipeline.JsonWriterPipeline': 600
#     }
# })
process = CrawlerProcess()
process.crawl(SjcGoldSpider)
# process.crawl(PnjGoldSpider)
process.start()

