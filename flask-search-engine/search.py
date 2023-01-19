from elasticsearch import Elasticsearch, helpers
import configparser
import queries
import booster
from booster import isEnglish

config = configparser.ConfigParser()
config.read('config.ini')

es = Elasticsearch(
    cloud_id=config['ELASTIC']['cloud_id'],
    http_auth=(config['ELASTIC']['user'], config['ELASTIC']['password'])
)

INDEX = 'sinhala-songs'

def boost(boost_array):

    term1 ="title_en^{}".format(boost_array[0])
    term2 = "singer_en^{}".format(boost_array[1])
    term3 = "lyricist_en^{}".format(boost_array[2])
    term4 = "composer_en^{}".format(boost_array[3])
    term5 = "title_si^{}".format(boost_array[4])
    term6 = "singer_si^{}".format(boost_array[5])
    term7 = "lyricist_si^{}".format(boost_array[6])
    term8 = "composer_si^{}".format(boost_array[7])
    term9 = "lyrics^{}".format(boost_array[8])
    term10 = "metaphor^{}".format(boost_array[9])
    term11 = "source_domain_si^{}".format(boost_array[10])
    term12 = "source_domain_en^{}".format(boost_array[11])
    term13 = "target_domain_si^{}".format(boost_array[12])
    term14 = "target_domain_en^{}".format(boost_array[13])
    term15 = "intepretation^{}".format(boost_array[14])
    # term16 = "views^{}".format(boost_array[15])
    
    return [term1,term2,term3,term4,term5,term6,term7,term8,term9,term10,term11,term12,term13,term14,term15]

def search(phrase,search_type):

    tokens = phrase.split()

    if (search_type == "anywhere"):

        flags = booster.boost_field(phrase)
        fields = boost(flags)
        
        num = 0
        counted_list = False
        dig_list = [int(s) for s in tokens if s.isdigit()]

        if ("Top" in phrase or "top" in phrase or "හොඳම" in phrase or "හොදම" in phrase) and len(dig_list)==1:
            num = dig_list[0]
            counted_list =  True
        
        if counted_list == False:     # If the query contain a number call sort query
            query_body = queries.fuzzy_multi_match(phrase, fields)
        else:
            query_body = queries.sorted_fuzzy_multi_match(phrase, num, fields)

    elif (search_type == "title_only"):
        if (isEnglish(phrase)==True):
            query_body = queries.single_phrase_match(phrase, "title_en")
        else:
            query_body = queries.single_phrase_match(phrase, "title_sn")

    elif (search_type == "lyricist_only"):
        if (isEnglish(phrase)==True):
            query_body = queries.single_phrase_match(phrase, "lyricist_en")
        else:
            query_body = queries.single_phrase_match(phrase, "lyricist_si")

    elif (search_type == "source_only"):
        if (isEnglish(phrase)==True):
            query_body = queries.single_phrase_match(phrase, "source_domain_en")
        else:
            query_body = queries.single_phrase_match(phrase, "source_domain_si")

    elif (search_type == "target_only"):
        if (isEnglish(phrase)==True):
            query_body = queries.single_phrase_match(phrase, "target_domain_en")
        else:
            query_body = queries.single_phrase_match(phrase, "target_domain_si")

    elif (search_type == "metaphors_only"):
        if (isEnglish(phrase)==False):
            query_body = queries.multi_match(phrase, ["metaphor"])
        else:
            return("Cannot search metaphors in english")

    res = es.search(index=INDEX, body=query_body) # Calling the elastic search client with the corresponding query body
    return res