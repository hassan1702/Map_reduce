from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017)
db = client['Assignment_1'] 
collection = db['Olympic_Athletes']

all_athletes = collection.find()

qualified_athletes = []

for athlete in all_athletes:
    edition = athlete['edition']
    year, olympics_type = edition.split(' ', 1)
    year = int(year)
    if olympics_type == 'Summer Olympics' and 1980 <= year <= 2020 and athlete['medal'] in ['Gold', 'Silver', 'Bronze']:
        qualified_athletes.append(athlete)

with open('athletes.txt', 'w') as output_file:
    for athlete in qualified_athletes:
        athlete_id = athlete['athlete_id']
        country = athlete['country_noc']
        year = athlete['edition'].split(' ')[0]
        event = athlete['event']
        medal = athlete['medal']
        output_file.write(f"{athlete_id} | {country} | {year} | {event} | {medal}\n")
