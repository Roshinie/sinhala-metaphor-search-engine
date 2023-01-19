from elasticsearch_dsl import Index
import json,re
from elasticsearch import Elasticsearch, helpers
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

es = Elasticsearch(
    cloud_id=config['ELASTIC']['cloud_id'],
    http_auth=(config['ELASTIC']['user'], config['ELASTIC']['password'])
)

INDEX = 'sinhala-songs'

def createIndex():
    index = Index(INDEX,using=es)
    res = index.create()
    print (res)

def read_all_songs():
    with open('summary-corpus/all_songs.json','r') as f:
        all_songs = json.loads(f.read())
        res_list = [i for n, i in enumerate(all_songs) if i not in all_songs[n + 1:]]
        return res_list

def clean_lyrics(lyrics):
    if lyrics:
        cleaned_lyrics_list = []
        lines = lyrics.split('\n')
        for index,line in enumerate(lines):
            line_stripped = re.sub('\s+',' ',line)
            line_punc_stripped = re.sub('[.!?\\-]', '', line_stripped)
            cleaned_lyrics_list.append(line_punc_stripped)
        last = len(cleaned_lyrics_list)
        final_list = []
        for index,line in enumerate(cleaned_lyrics_list):
            if line=='' or line==' ':
                if index!= last-1 and (cleaned_lyrics_list[index+1]==' ' or cleaned_lyrics_list[index+1]=='') :
                    pass
                else:
                    final_list.append(line)
            else:
                final_list.append(line)
        cleaned_lyrics = '\n'.join(final_list)
        return cleaned_lyrics
    else:
        return None

def genData(song_array):
    for song in song_array:

        title_en = song.get("title_en",None)
        singer_en = song.get("singer_en", None)
        lyricist_en = song.get("lyricist_en", None)
        composer_en = song.get("composer_en", None)
        title_si = song.get("title_si", None)
        singer_si = song.get("singer_si", None)
        lyricist_si = song.get("lyricist_si", None)
        composer_si = song.get("composer_si", None)
        lyrics = clean_lyrics(song.get("lyrics",None))
        metaphor = song.get("metaphor",None)
        source_domain_si = song.get('source_domain_si', None)
        source_domain_en = song.get("source_domain_en", None)
        target_domain_si = song.get("target_domain_si", None)
        target_domain_en = song.get("target_domain_en", None)
        intepretation = song.get("intepretation",None)
        views = song.get('views',None)

        yield {
            "_index": "sinhala-songs",
            "_source": {
                "title_en": title_en,
                "singer_en": singer_en,
                "lyricist_en": lyricist_en,
                "composer_en": composer_en,
                "title_si": title_si,
                "singer_si": singer_si,
                "lyricist_si": lyricist_si,
                "composer_si": composer_si,
                "lyrics": lyrics,
                "metaphor": metaphor,
                "source_domain_si": source_domain_si,
                "source_domain_en": source_domain_en,
                "target_domain_si": target_domain_si,
                "target_domain_en": target_domain_en,
                "intepretation": intepretation,
                "views" :views
            },
        }


createIndex()
all_songs = read_all_songs()
helpers.bulk(es,genData(all_songs))

