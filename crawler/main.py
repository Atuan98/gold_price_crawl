# from scrapy.crawler import CrawlerProcess
from spiders.sjc_gold_spider import SjcGoldSpider
from spiders.pnj_gold_spider import PnjGoldSpider
from spiders.doji_gold_spider import DojiGoldSpider
from scrapy.utils.log import configure_logging
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor
from loguru import logger
runner = CrawlerRunner(settings={
    "ITEM_PIPELINES": {
        'pipelines.pipelines.MongoDBPipeline': 600
    }
})

def run_spider():
    try:
        configure_logging()
        print(configure_logging)
        runner.crawl(PnjGoldSpider)
        runner.crawl(SjcGoldSpider)
        runner.crawl(DojiGoldSpider)
        logger.info("Connected")
    except:
        logger.info("Failed")
    d = runner.join()
    d.addBoth(lambda _: reactor.stop())
    reactor.run()


if __name__ == "__main__":
    run_spider()