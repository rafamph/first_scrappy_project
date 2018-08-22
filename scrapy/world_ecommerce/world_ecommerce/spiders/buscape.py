# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy.selector import Selector

class BuscapeSpider(scrapy.Spider):
    name = 'buscape'
    allowed_domains = ['buscape.com.br/search/tv-led']
    start_urls = ['http://buscape.com.br/search/tv-led/']

    def parse(self, response):
        names = response.xpath('//*[@itemprop="name"]/text()').extract()
        #images = response.xpath('//*[@class="card--product__thumb"]/@src').extract()
        prices = response.xpath('//*[@itemprop="lowPrice"]/@content').extract()
        #for i in range(len(names)):
            #yield{"names:" : names[i], "images:" : images[i], "prices:" : prices[i]}

        driver = webdriver.Chrome('/home/raflicky/Downloads/chromedriver')
        driver.get("buscape.com.br/search/tv-led")

        images = driver.find_element_by_path('//*[@class="card--product__thumb"]/@src').extract()

        for i in range(len(names)):
            yield{"names:" : names[i], "images:" : images[i], "prices:" : prices[i]}

	#yield{"names" : names[0], "images:" : images[0], "prices:" : prices[0]}
	#new_pages = response.xpath('//*[@class="button--link__checkout btn-neemu-addtocart"]/@data-link').extract() 
        #for new_page in new_pages:
            #new_url = response.urljoin(new_page)
            #new_response = (scrapy.Request(new_url))
            
