import ee

ee.Initialize(project='gee-mb-06')

lon_min, lat_min, lon_max, lat_max = -55.0, -5.0, -54.9, -4.9
aoi = ee.Geometry.Rectangle([lon_min, lat_min, lon_max, lat_max])

collection = (ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
              .filterBounds(aoi)
              .filterDate('2024-01-01', '2024-12-31')
              .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 60)))

image = collection.median().clip(aoi)

worldcover = ee.ImageCollection("ESA/WorldCover/v200").first()
dem = ee.Image("USGS/SRTMGL1_003")
gedi = ee.Image('LARSE/GEDI/GEDI04_B_002')

print('WorldCover bands:', worldcover.bandNames().getInfo())
print('DEM bands:', dem.bandNames().getInfo())
print('GEDI bands:', gedi.bandNames().getInfo())
