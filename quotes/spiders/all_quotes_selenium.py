# -*- coding: utf-8 -*-
import scrapy
from scrapy_selenium import SeleniumRequest
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from shutil import which


class AllQuotesSpiderSelenium(scrapy.Spider):
    name = 'all_quotes_selenium'

    def start_requests(self):
        yield SeleniumRequest(
            url='https://quotes.toscrape.com/js',
            wait_time=3,
            callback=self.parse
        )


    def parse(self, response):
        quotes = response.xpath("//div[@class='quote']")
        for quote in quotes:
            yield {
                'quote_1': quote.xpath(".//span[1]/text()").get(),
                'author': quote.xpath(".//span[2]/small/text()").get(),
                'tags': quote.xpath(".//div/a/text()").getall()
            }

        next_page = response.xpath("//li[@class='next']/a/@href").get()
        if next_page:
            absolute_url = f"https://quotes.toscrape.com{next_page}"
            yield SeleniumRequest(
                url=absolute_url,
                wait_time=3,
                callback=self.parse
            )