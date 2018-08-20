# -*- coding: utf-8 -*-
import scrapy

class FrasesSpider(scrapy.Spider):
    name = 'frases'
    allowed_domains = ['quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com//']

    def parse(self, response):
        #h1 = response.xpath('//h1/a/text()').extract()
        #list = response.xpath('//*[@class="tag-item"]/a/text()').extract()
        all_quotes = []
        all_phrases = []
        all_keywords = []
        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:
            text = quote.xpath('.//*[@class="text"]/text()').extract()
            all_quotes.append(text)
        authors = response.xpath('//*[@class="author"]')
        for i in range(len(authors)):
            text2 = authors.xpath('//*[@itemprop="author"]/text()').extract()[i]
            all_phrases.append(text2)
        keywords = response.xpath('//*[@class="keywords"]/@content').extract()
        for j in range(len(keywords)):
            text3 = keywords[j]
            all_keywords.append(text3)
        relative_url = response.xpath("//*[@class = 'next']/a/@href").extract_first()
        absolute_url = response.urljoin(relative_url)
        
        for k in range(len(all_quotes)):
            #print(all_quotes[k][0])
            #print("\n")
            #print(all_phrases[k])
            #print("\n")
            #print(all_keywords[k])
            #print("\n\n\n\n\n")
            yield{"Quote": all_quotes[k][0], "Phrases": all_phrases[k], "Keywords": all_keywords[k]}

        yield(scrapy.Request(absolute_url))
