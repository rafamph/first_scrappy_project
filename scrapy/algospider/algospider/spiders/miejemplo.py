# -*- coding: utf-8 -*-
import scrapy


class MiejemploSpider(scrapy.Spider):
    name = 'miejemplo'
    allowed_domains = ['ejemplo.com']
    start_urls = ['http://ejemplo.com/']

    def parse(self, response):
        pass
