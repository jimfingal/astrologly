import json
import arrow
import os 
import signs

path = os.path.join(os.path.dirname(__file__), 'data/moondata.json')

with open(path) as f:
    moondata = json.loads(f.read())


moon_lookup = {}

for key, values in moondata.iteritems():
    moon_lookup[int(key)] = map(lambda x: (arrow.get(x[0], 'YYYY MMM DD HH:mm'), x[1]), values)


def get_moon_sign(parsed_date):
    year_lookup = moon_lookup[parsed_date.year]

    for cutoff, sign in year_lookup:
        if parsed_date < cutoff:
            return signs.sign_map.get(sign)