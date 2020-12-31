import scrapy
from scrapy_splash import SplashRequest

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotestoscrape.com']
    start_urls = ['http://quotestoscrape.com/']
    def start_requests(self):
        yield SplashRequest(

            url='https://quotes.toscrape.com/js/',
            callback=self.parse,

        )





    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                'text':quote.css("span.text::text").extract_first(),
                'author':quote.css("small.text::author").extract_first(),
                'tags':quote.css("div.tags>a.tag::text").extract(),



            }
