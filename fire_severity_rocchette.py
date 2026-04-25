import openeo

conn = openeo.connect("openeofed.dataspace.copernicus.eu")
conn.authenticate_oidc()

spatial_extent = {
    "west": 10.77,
    "south": 42.76,
    "east": 10.82,
    "north": 42.80
}

before_dates = ["2025-06-25", "2025-07-08"]
after_dates = ["2025-07-12", "2025-07-25"]

cube_before = conn.load_collection(
    "SENTINEL2_L2A",
    spatial_extent=spatial_extent,
    temporal_extent=before_dates,
    bands=["B08", "B12"]
)

nir_before = cube_before.band("B08")
swir_before = cube_before.band("B12")
nbr_before = (nir_before - swir_before) / (nir_before + swir_before)
nbr_before_mean = nbr_before.reduce_dimension(dimension="t", reducer="mean")

cube_after = conn.load_collection(
    "SENTINEL2_L2A",
    spatial_extent=spatial_extent,
    temporal_extent=after_dates,
    bands=["B08", "B12"]
)

nir_after = cube_after.band("B08")
swir_after = cube_after.band("B12")
nbr_after = (nir_after - swir_after) / (nir_after + swir_after)
nbr_after_mean = nbr_after.reduce_dimension(dimension="t", reducer="mean")

dnbr = nbr_before_mean - nbr_after_mean

result = dnbr.save_result(format="GTiff")
result.download("dnbr_rocchette_2025.tif")

print("Saved: dnbr_rocchette_2025.tif")