from scrapy.crawler import CrawlerProcess
from spiders.sjc_gold_spider import SjcGoldSpider
from spiders.pnj_gold_spider import PnjGoldSpider
from spiders.doji_gold_spider import DojiGoldSpider


process = CrawlerProcess(settings={
    "ITEM_PIPELINES": {
        'pipelines.pipelines.MongoDBPipeline': 600
    }
})
# process = CrawlerProcess()
process.crawl(SjcGoldSpider)
process.crawl(PnjGoldSpider)
process.crawl(DojiGoldSpider)
process.start()

