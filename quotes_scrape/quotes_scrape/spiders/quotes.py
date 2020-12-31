import scrapy
from scrapy_splash import SplashRequest

class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    def start_requests(self):
        yield SplashRequest(

            url='https://quotes.toscrape.com/js/',
            callback=self.parse,

        )





    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                'text':quote.css("span.text::text").extract_first(),
                'author':quote.css("small.author::text").extract_first(),
                'tags':quote.css("div.tags>a.tag::text").extract(),



            }
