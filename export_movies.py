#!/usr/bin/python3
import csv
import json
import ast
import datetime

csvfile = open('tmdb_5000_movies.csv', 'r')
jsonfile = open('tmdb_5000_movies.json', 'w')

import datetime

# def __parse_date_format(stringDate):
# 	date = datetime.datetime.strptime(stringDate , '%Y-%m-%d').strftime('%Y-%m-%dT%H:%M:%S.%f')
# 	return date

def parseDate(strDate):
	parsedDate = strDate.split("-")
	parsedObject = list(map(int, parsedDate))
	return parsedObject

fieldnames = (
	'budget',
	'genres',
	'homepage',
	'id',
	'keywords',
	'original_language',
	'original_title',
	'overview',
	'popularity',
	'production_companies',
	'production_countries',
	'release_date',
	'revenue',
	'runtime',
	'spoken_languages',
	'status',
	'tagline',
	'title',
	'vote_average',
	'vote_count'
)
fieldfixers = {
	'budget': int,
	'genres': ast.literal_eval,
	'homepage': str,
	'id': int,
	'keywords': ast.literal_eval,
	'original_language': str,
	'original_title':str,
	'overview': str,
	'popularity': float,
	'production_companies': ast.literal_eval,
	'production_countries': ast.literal_eval,
	'release_date': str,
	'revenue': int,
	'runtime': int,
	'spoken_languages': ast.literal_eval,
	'status': str,
	'tagline': str,
	'title': str,
	'vote_average': float,
	'vote_count': int
}
reader = csv.DictReader(csvfile, fieldnames)

for row in reader:
	for key,value in row.items():
		try:
			ffunc = fieldfixers.get(key)
			if ffunc == 'release_date':
				stringDate = ffunc(value)
				convertDate = parseDate(stringDate)
				row[key] = convertDate
			elif ffunc:
					row[key] = ffunc(value)
		except:
			continue
	json.dump(row, jsonfile)
	jsonfile.write('\n')
