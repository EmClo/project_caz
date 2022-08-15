import geopandas as gpd


gpd.read_file("Charging_Order_Boundary.shp").to_file('data.geojson', driver='GeoJSON')