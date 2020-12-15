#!/usr/bin/python3
import json
import pymongo

client = pymongo.MongoClient('mongodb://nastava.is.pmf.uns.ac.rs:27017')
#ime baze
db = client['MirelaNesic']
#ime kolekcije
# credits_collection = db['credits']
# data = [json.loads(line) for line in open('tmdb_5000_credits.json', 'r')]
# credits_collection.insert_many(data)

movies_collection = db['movies']
data = [json.loads(line) for line in open('tmdb_5000_movies.json', 'r')]
movies_collection.insert_many(data)

client.close()
