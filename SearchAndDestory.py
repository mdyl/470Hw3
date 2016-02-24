from bing_search_api import BingSearchAPI
import json

my_key = "dWls875YJyXwh7dmX3LdIaETO9IDjfkdG4g8533M9zs"
query_string = raw_input("What is your query? ")
bing = BingSearchAPI(my_key)
params = { '$format': 'json',
              '$top': 10,
              '$skip': 0}
searchJSON = bing.search('news',query_string,params).json()
print searchJSON[1]

