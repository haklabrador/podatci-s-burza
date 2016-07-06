# mali test program koji ce da preuzeti finansijske podatke sa yahoo servera i da ih ucita u memoriju u pajton dictionary

import urllib
import json
from pprint import pprint

prices = []

def get_data():
	f = urllib.urlopen('http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20IN%20%28%22YHOO%22%29&format=json&env=http://datatables.org/alltables.env')
	js = f.read()

	d = json.loads(js)

	prices.append((d['query']['created'],
				   d['query']['results']['quote']['Symbol'],
		           d['query']['results']['quote']['Ask']))

