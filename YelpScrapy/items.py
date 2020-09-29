import scrapy


class YelpscrapyItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    biz_id = scrapy.Field()
    img_link = scrapy.Field()
    tel = scrapy.Field()
    email = scrapy.Field()
    address = scrapy.Field()
    rating = scrapy.Field()
    review_count = scrapy.Field()
    categories = scrapy.Field()
    site = scrapy.Field()
    hours = scrapy.Field()
    about_biz = scrapy.Field()
    amenities = scrapy.Field()
