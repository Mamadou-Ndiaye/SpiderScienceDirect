import scrapy
from scrapy import Request

class SpiderArticleScienceDiect(scrapy.Spider):
    name = 'articleScienceDirect'
    start_urls = ['https://www.sciencedirect.com/articlelist/covid']
    #start_urls = ['https://www.sciencedirect.com/articlelist/covid?offset=100']
    #filtrer une url plusieurs fois
    #custom_settings = {
    #    'DUPEFILTER_CLASS': 'scrapy.dupefilters.BaseDupeFilter',
    #}

##    def parse(self, response):
##        #yield response.follow(self.start_urls[0], self.autreparse)
##        return Request(self.start_urls[0], callback = self.autreparse)
##
##    def autreparse(self,response):
##        items = dict()
##        Domain = self.start_urls[0].rsplit('/')
##        all_li_items = response.css("#srp-results-list .push-m")
##        for li in all_li_items:
##            items['type']=li.css('.u-clr-grey8::text').extract_first()
##            items['titre'] = li.css('.text-s::text').extract_first()
##            Liens = li.css('.text-s').xpath('@href').get()
##            items['url']= str(Domain[0]) + "//" + str(Domain[2]) + str(Liens)
##            items['book'] = li.css('.subtype-srctitle-link span::text').extract_first()
##            items['date'] = li.css('.preceding-comma:nth-child(2)::text').extract_first()
##            items['auteurs1'] = li.css('.hor li:nth-child(1) .author::text').extract_first()
##            items['auteurs2'] = li.css('.hor li:nth-child(2) .author::text').extract_first()
##            #a=response.follow(Liens, self.secondparse)
##            #yield items
##            #items['abs']=response.follow(Liens, self.secondparse)
##            yield items
##
##    def secondparse(self,response):
##         yield {'abs':response.css('.author p::text').extract()}
    
    def parse(self,response):
        items = dict()
        Domain = self.start_urls[0].rsplit('/')

        def autreparse(response):
            return response.css('.author p::text').extract()
            
            
        all_li_items = response.css("#srp-results-list .push-m")
        for li in all_li_items:
            Types = li.css('.u-clr-grey8::text').extract_first()
            Titre = li.css('.text-s::text').extract_first()
            Liens = li.css('.text-s').xpath('@href').get()
            #lienComplet = str(Domain[0]) + "//" + str(Domain[2]) + str(Liens)
            Book = li.css('.subtype-srctitle-link span::text').extract_first()
            Date = li.css('.preceding-comma:nth-child(2)::text').extract_first()
            Auteurs1 = li.css('.hor li:nth-child(1) .author::text').extract_first()
            Auteurs2 = li.css('.hor li:nth-child(2) .author::text').extract_first()
            #abstract = response.follow(Liens, self.secondparse)
           
            items['type']= Types
            items['titre']= Titre
            items['url'] = response.urljoin(Liens)
            items['book'] = Book
            items['date'] = Date
            items['auteurs1']= Auteurs1
            items['auteurs2']= Auteurs2
            #items['abstract'] = abstract
            yield items
            
        #next_page = response.css('#srp-pagination a::attr(href)').get()
        next_page = response.css('li.next-link a::attr(href)').get()
        #items['test'] = response.urljoin(next_page)
        #yield Request(response.urljoin(next_url), callback=self.parse_anime_list_page)
        print("urljoin ",response.urljoin(next_page))
        if next_page is not None:
            #yield response.follow(next_page, callback =self.parse)
            yield Request(response.urljoin(next_page), callback=self.parse)
##    
##    def secondparse(self,response):
##        yield {'abs':response.css('.author p::text').extract()} 
        
