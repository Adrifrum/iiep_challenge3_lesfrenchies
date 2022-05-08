from unicodedata import name
import pandas as pd
import csv
import json
from collections import OrderedDict

df = pd.read_excel('Saint-Lucia-IIEP-topup.xlsx')

df = df.replace('true','Available', regex=True)
df = df.replace('false','Unavailable', regex=True)

json_result_string = df.to_json(
    orient='records',
    double_precision=12,
    date_format='iso'
)
json_result = json.loads(json_result_string)


geojson = {
    'type': 'FeatureCollection',
    'features': []
}
for record in json_result:
    geojson['features'].append({
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [record['longitude'], record['latitude']],
        },
        'properties': record,
    })


with open('output.json', 'w') as f:
    f.write(json.dumps(geojson, indent=2))
