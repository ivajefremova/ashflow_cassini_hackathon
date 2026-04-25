import openeo

conn = openeo.connect("openeofed.dataspace.copernicus.eu")
conn.authenticate_oidc()

spatial_extent = {
    "west": 10.77,
    "south": 42.76,
    "east": 10.82,
    "north": 42.80
}

temporal_extent = ["2025-07-12", "2025-07-25"]

cube = conn.load_collection(
    "SENTINEL2_L2A",
    spatial_extent=spatial_extent,
    temporal_extent=temporal_extent,
    bands=["B03", "B08"]
)

green = cube.band("B03")
nir = cube.band("B08")

ndwi = (green - nir) / (green + nir)
ndwi_mean = ndwi.reduce_dimension(dimension="t", reducer="mean")

result = ndwi_mean.save_result(format="GTiff")
result.download("real_ndwi_rocchette.tif")

print("Saved: real_ndwi_rocchette.tif")