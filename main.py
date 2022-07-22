# from scrapy.crawler import CrawlerProcess
from spiders.sjc_gold_spider import SjcGoldSpider
from spiders.pnj_gold_spider import PnjGoldSpider
from spiders.doji_gold_spider import DojiGoldSpider
from scrapy.utils.log import configure_logging
#
# import sys
#
# process = CrawlerProcess(settings={
#     "ITEM_PIPELINES": {
#         'pipelines.pipelines.MongoDBPipeline': 600
#     }
# })
# process.crawl(SjcGoldSpider)
# if "twisted.internet.reactor" in sys.modules:
#     del sys.modules["twisted.internet.reactor"]
# process.crawl(PnjGoldSpider)
# if "twisted.internet.reactor" in sys.modules:
#     del sys.modules["twisted.internet.reactor"]
# process.crawl(DojiGoldSpider)
# if "twisted.internet.reactor" in sys.modules:
#     del sys.modules["twisted.internet.reactor"]
#     reactor.start()
# process.start()

from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor

# runner = CrawlerRunner(settings={
#     "ITEM_PIPELINES": {
#         'pipelines.pipelines.MongoDBPipeline': 600
#     }
# })

def run_spider():
    configure_logging()

    runner = CrawlerRunner()
    runner.crawl(PnjGoldSpider)
    runner.crawl(SjcGoldSpider)
    runner.crawl(DojiGoldSpider)
    d = runner.join()
    d.addBoth(lambda _: reactor.stop())
    reactor.run()


if __name__ == "__main__":
    run_spider()