import scrapy
from scrapy.linkextractors import LinkExtractor
from spiders.items import TestItem


class ExampleSpider1(scrapy.Spider):
    name = 'examplespider1'
    allowed_domains = ['www.familug.org']
    start_urls = ['https://www.familug.org/search/label/Python',
                  'https://www.familug.org/search/label/Command']

    def parse(self, response):
        self.logger.info('A response from {} just arrived'.format(response.url))
        self.logger.debug('Nothing wrong in {}'.format(response.url))


class ExampleSpider2(scrapy.Spider):
    name = 'examplespider2'
    allowed_domains = ['www.familug.org']
    start_urls = ['https://www.familug.org/search/label/Python',
                  'https://www.familug.org/search/label/Command']

    def parse(self, response):
        for title in response.css('h3.post-title.entry-title a::text').getall():
            self.logger.info('Welcome' + title)
            yield {'title': title}

        for href in response.css('h3.post-title.entry-title a::attr(href)').getall():
            yield scrapy.Request(href, self.parse)


class ExampleSpider3(scrapy.spiders.CrawlSpider):
    name = 'examplespider3'
    allowed_domains = ['www.familug.org']
    start_urls = ['http://www.familug.org']

    rules = (
        # Extract links matching '.php'
        scrapy.spiders.Rule(LinkExtractor(allow=('.php',)), callback='parse_item'),
    )

    def parse_item(self, response):
        self.logger.info('Hi, this is an item page: {}'.format(response.url))
        item = TestItem()
        item['name'] = response.css('h3.post-title.entry-title a::text').get()
        return