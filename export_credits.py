#!/usr/bin/python3
import csv
import json
import ast

csvfile = open('tmdb_5000_credits.csv', 'r')
jsonfile = open('tmdb_5000_credits.json', 'w')
fieldnames = (
    "movie_id",
    "title",
    "cast",
    "crew"
    )

fieldfixers = {
    "movie_id": int,
    "title": str,
    "cast": ast.literal_eval,
    "crew": ast.literal_eval
}
reader = csv.DictReader(csvfile, fieldnames)

for row in reader:
	for key,value in row.items():
		try:
			ffunc = fieldfixers.get(key)
			if ffunc:
					row[key] = ffunc(value)
		except:
			continue
	json.dump(row, jsonfile)
	jsonfile.write('\n')
