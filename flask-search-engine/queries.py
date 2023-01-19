import json


def single_phrase_match(query,field):
		q = {
			"size": 200,
			"explain": True,
			"query": {
				"match_phrase": {
					field: {
						"query" : query,
						"analyzer": "standard", # standard, simple, whitespace, stop, keyword, pattern, <language>, fingerprint
					}
				}
			},
			"aggs": {
				"Singer Filter": {
					"terms": {
						"field": "singer_si.keyword",
						"size": 10
					}
				},
				"Composer Filter": {
					"terms": {
						"field": "composer_si.keyword",
						"size": 10
					}
				},
				"Lyricist Filter": {
					"terms": {
						"field": "lyricist_si.keyword",
						"size": 10
					}
				}
			}
		}

		q = json.dumps(q)
		return q

def single_field_match(query,field01):
		q = {
			"size": 200,
			"explain": True,
			"query": {
				"match": {
					field01: {
						"query" : query,
						"analyzer": "standard", # standard, simple, whitespace, stop, keyword, pattern, <language>, fingerprint
					}
				}
			},
			"aggs": {
				"Singer Filter": {
					"terms": {
						"field": "singer_si.keyword",
						"size": 10
					}
				},
				"Composer Filter": {
					"terms": {
						"field": "composer_si.keyword",
						"size": 10
					}
				},
				"Lyricist Filter": {
					"terms": {
						"field": "lyricist_si.keyword",
						"size": 10
					}
				}
			}
		}

		q = json.dumps(q)
		return q

def fuzzy_multi_match(query, fields, operator ='or'):
	q = {
		"size": 200,
		"explain": True,
		"query": {
			"multi_match": {
                "query": query,
                "fields": fields,
                "type": "best_fields", # best_fields, most_fields, cross-fields, phrase, phrase_prefix try all
                "operator": "or",
                #"minimum_should_match": 2, # How many terms must be included to match if the operator is or
                "analyzer": "standard", # standard, simple, whitespace, stop, keyword, pattern, <language>, fingerprint
                "fuzziness": "AUTO", # The number of character edits (insert, delete, substitute) to get the required term
                "fuzzy_transpositions": True, # Allow character swaps
                "lenient": False, # Avoid data type similarity requirement
                "prefix_length": 0, # Number of beginning characters left unchanged when creating expansions
                "max_expansions": 50, # Maximum number of variations created. Defaults to 50.
                "auto_generate_synonyms_phrase_query": True,
                "zero_terms_query": "none"
			}
		},
		"aggs": {
			"Singer Filter": {
				"terms": {
					"field": "singer_si.keyword",
					"size": 10
				}
			},
			"Composer Filter": {
				"terms": {
					"field": "composer_si.keyword",
					"size": 10
				}
			},
			"Lyricist Filter": {
				"terms": {
					"field": "lyricist_si.keyword",
					"size": 10
				}
			}
		}
	}

	q = json.dumps(q)
	return q


def sorted_fuzzy_multi_match(query, sort_num, fields, operator ='or'):
	print ('sort num is ',sort_num)
	q = {
		"size": sort_num,
		"sort": [
			{"views": {"order": "desc"}},
		],
		"query": {
			"multi_match": {
                "query": query,
                "fields": fields,
                "type": "best_fields", # best_fields, most_fields, cross-fields, phrase, phrase_prefix try all
                "operator": "or",
                #"minimum_should_match": 2, # How many terms must be included to match if the operator is or
                "analyzer": "standard", # standard, simple, whitespace, stop, keyword, pattern, <language>, fingerprint
                "fuzziness": "AUTO", # The number of character edits (insert, delete, substitute) to get the required term
                "fuzzy_transpositions": True, # Allow character swaps
                "lenient": False, # Avoid data type similarity requirement
                "prefix_length": 0, 
                "max_expansions": 50,
                "auto_generate_synonyms_phrase_query": True,
                "zero_terms_query": "none"
			}
		},
		"aggs": {
			"Singer Filter": {
				"terms": {
					"field": "singer_si.keyword",
					"size": 10
				}
			},
			"Composer Filter": {
				"terms": {
					"field": "composer_si.keyword",
					"size": 10
				}
			},
			"Lyricist Filter": {
				"terms": {
					"field": "lyricist_si.keyword",
					"size": 10
				}
			}
		}
	}
	q = json.dumps(q)
	return q

def multi_match(query, fields, operator ='or'):
	q = {
		"size": 200,
		"explain": True,
		"query": {
			"multi_match": {
                "query": query,
                "fields": fields,
                "type": "best_fields", # best_fields, most_fields, cross-fields, phrase, phrase_prefix try all
                "operator": operator,
                #"minimum_should_match": 2, # How many terms must be included to match if the operator is or
                "analyzer": "standard", # standard, simple, whitespace, stop, keyword, pattern, <language>, fingerprint
                "fuzziness": 0, # The number of character edits (insert, delete, substitute) to get the required term
                "fuzzy_transpositions": True, # Allow character swaps
                "lenient": False, # Avoid data type similarity requirement
                "prefix_length": 0, 
                "max_expansions": 50,
                "auto_generate_synonyms_phrase_query": True,
                "zero_terms_query": "none"
			}
		},
		"aggs": {
			"Singer Filter": {
				"terms": {
					"field": "singer_si.keyword",
					"size": 10
				}
			},
			"Composer Filter": {
				"terms": {
					"field": "composer_si.keyword",
					"size": 10
				}
			},
			"Lyricist Filter": {
				"terms": {
					"field": "lyricist_si.keyword",
					"size": 10
				}
			}
		}
	}

	q = json.dumps(q)
	return q