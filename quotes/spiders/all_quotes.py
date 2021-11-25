# -*- coding: utf-8 -*-
import scrapy


class AllQuotesSpider(scrapy.Spider):
    name = 'all_quotes'
    allowed_domains = ['http://quotes.toscrape.com/js/']
    start_urls = ['http://quotes.toscrape.com/js//']

    def parse(self, response):
        pass
