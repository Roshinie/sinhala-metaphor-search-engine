import scrapy
from lyrics.items import LyricsItem
from mtranslate import translate
import re

def translation_array(stringArray):
    translated_array = []
    for string in stringArray:
        translated_array.append(translate(string, 'si', 'en'))
    return translated_array
        
class LyricsSpider(scrapy.Spider):
    name = 'lyrics_scraper'
        
    for i in range(1,23):
        start_urls = ["https://sinhalasongbook.com/all-sinhala-song-lyrics-and-chords/?_page="+str(i)]
            
    def parse(self, response):
        for href in response.xpath("//main[contains(@id, 'genesis-content')]//div[contains(@class, 'entry-content')]//div[contains(@class, 'pt-cv-wrapper')]//h4[contains(@class, 'pt-cv-title')]/a/@href"):
            url = href.extract()

            yield scrapy.Request(url, callback=self.parse_dir_contents)  

    def parse_dir_contents(self, response):

        item = LyricsItem()

        #song title
        title = response.xpath("//div[contains(@class, 'site-inner')]//header[contains(@class, 'entry-header')]/h1/text()").extract()[0]
        item['title'] = re.split('[\–|-]', title)[1].strip()
            
        #artist name
        artist = response.xpath("//div[contains(@class, 'entry-content')]//div[contains(@class, 'su-column su-column-size-3-6')]//span[contains(@class, 'entry-categories')]/a/text()").extract()
        item['artist'] = translation_array(artist)
                
        #lyricist
        lyricist = response.xpath("//div[contains(@class, 'entry-content')]//div[contains(@class, 'su-column su-column-size-2-6')]//span[contains(@class, 'lyrics')]/a/text()").extract()
        item['lyricist'] = translation_array(lyricist)
        
        #musicComposer
        musicComposer = response.xpath("//div[contains(@class, 'entry-content')]//div[contains(@class, 'su-column su-column-size-2-6')]//span[contains(@class, 'music')]/a/text()").extract()
        item['musicComposer'] = translation_array(musicComposer)
        
        #genre
        genre = response.xpath("//div[contains(@class, 'entry-content')]//div[contains(@class, 'su-column su-column-size-3-6')]//span[contains(@class, 'entry-tags')]/a/text()").extract()
        item['genre'] = translation_array(genre)
        
        #views
        views = response.xpath("//div[contains(@class, 'entry-content')]/div[contains(@class, 'tptn_counter')]/text()").extract()[0]
        item['views']  = int(re.sub('[^0-9,]', "", views).replace(',', ''))
            
        #shares
        shares = response.xpath("//div[contains(@class, 'entry-content')]//div[contains(@class, 'nc_tweetContainer swp_share_button total_shares total_sharesalt')]/span[contains(@class, 'swp_count')]/text()").extract()[0]
        item['shares'] = int(re.sub('[^0-9,]', "", shares).replace(',', ''))
       
        #lyrics
        lyrics = response.xpath("//div[contains(@class, 'entry-content')]//pre/text()").extract()           
        song = ''
        check_newline = False
            
        for line in lyrics:
            lines = (re.sub("[\da-zA-Z\d0-9\-—\[\]\(\)\}\{\@\_\!\#\+\$\%\^\&\*\<\>\?\|\~\:\∆\/]", "", line)).split('\n')
            for line_l in lines:
                if not(line_l.isspace() or line_l == ""):
                    song += line_l.strip()
                    check_newline = True
                else:
                    if check_newline:
                        song += '\\n'
                        check_newline = False
                            
        item['lyrics'] = song

        yield item

