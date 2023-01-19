# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LyricsItem(scrapy.Item):
    title_si = scrapy.Field()
    title_en = scrapy.Field()
    singer_si = scrapy.Field()
    singer_en = scrapy.Field()
    lyricist_si = scrapy.Field()
    lyricist_en = scrapy.Field()
    composer_si = scrapy.Field()
    composer_en = scrapy.Field()
    lyrics = scrapy.Field()
    genre_si = scrapy.Field()
    genre_en = scrapy.Field()
    views = scrapy.Field()
    shares = scrapy.Field()
    
