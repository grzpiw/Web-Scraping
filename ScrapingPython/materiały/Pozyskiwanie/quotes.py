import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']
    start_urls = ['https://quotes.toscrape.com']

    def parse(self, response):
        self.log(f'I just visited {response.url}')
        
        for quote in response.css('div.quote'):
            item = {'author_name': quote.css('small.author::text').extract_first(),
                    'text': quote.css('span.text::text').extract_first(),
                    'tags': quote.css('a.tag::text').extract()}
            yield item
            
        next_page_url = response.urljoin(response.css('li.next > a::attr(href)').extract_first())
        
        if next_page_url:
            yield scrapy.Request(url=next_page_url, callback=self.parse)
