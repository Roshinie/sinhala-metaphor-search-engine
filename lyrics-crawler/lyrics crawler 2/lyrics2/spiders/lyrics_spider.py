from scrapy.spiders import SitemapSpider


class LyricsSpider(SitemapSpider):
    name = "lyrics"
    allowed_domains = ['lyricslk.com']
    sitemap_urls = [
        'http://lyricslk.com/sitemap.xml'
    ]
    sitemap_rules = [('^(?!.*artist).*$', 'parse')]

   
    def parse(self, response):
        song_lines = response.xpath('//*[@id="lyricsBody"]/text()').getall()
        song = ''
        for line in song_lines:
            song_line = line.split('\n')[1].strip()
            song = song + " " + song_line
        yield {
            'title_si': response.xpath('//*[@id="lyricsTitle"]/h2/text()')[0].get().split(' - ')[0],
            'title_en': response.xpath('//*[@id="lyricsTitle"]/h1/text()')[0].get().split(' - ')[0],
            'singer_si': response.xpath('//*[@id="lyricsTitle"]/h2/text()')[0].get().split(' - ')[1],
            'singer_en': response.xpath('//*[@id="lyricsTitle"]/h1/text()')[0].get().split(' - ')[1],
            'song' : song
        }