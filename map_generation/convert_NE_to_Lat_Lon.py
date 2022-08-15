import json
from pyproj import Proj, transform

with open('data.geojson') as input_data_file:
    data = json.load(input_data_file)

coordinates = data['features'][0]['geometry']['coordinates'][0]

northings_eastings = Proj('epsg:27700')
latitude_longitude = Proj('epsg:4326')

for index, coordinate_pair in enumerate(coordinates):
    easting, northing = coordinate_pair
    latitude, longitude = transform(northings_eastings, latitude_longitude, easting, northing)
    coordinates[index] = [longitude, latitude]

with open('newdata.geojson', 'w') as output_data_file:
    json.dump(data, output_data_file, indent=2)