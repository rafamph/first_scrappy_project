# -*- coding: utf-8 -*-
import scrapy


class BuscapeSpider(scrapy.Spider):
    name = 'buscape'
    allowed_domains = ['buscape.com.br/search/tv-led']
    start_urls = ['http://buscape.com.br/search/tv-led/']

    def parse(self, response):
        names = response.xpath('//*[@class="card--product__name u-truncate-multiple-line"]/text()').extract()
        images = response.xpath('//*[@class="card--product__thumb"]/@src').extract()
        prices = response.xpath('//*[@itemprop="lowPrice"]/@content').extract()
        yield{"names" : names[0], "images:" : images[0], "prices:" : prices[0]}
