import json, os


f = open('map.json', 'r')
data = json.load(f)
f.close()

geojson = {
    "type": "FeatureCollection",
    "features": []
}

data = data[1]['children']['locations']

for i in data:
    if 'lat' in i.keys() and 'lng' in i.keys():
        lat = i['lng']
        lng = i['lat']
    elif 'position' in i.keys():
        lat = i['position'][1]
        lng = i['position'][0]
    else:
        lat, lng = 0,0
    if i['reference'] != '':
        reference = i['reference'][0]

    geojson['features'].append({
        "type": "Feature",
        "properties": {
            "name": i['name'],
            'code': reference
        },
        "geometry": {
            "type": "Point",
            "coordinates": [lat, lng]
        }
    })

with open('parsedMap.geojson', 'w') as f:
    json.dump(geojson, f)
