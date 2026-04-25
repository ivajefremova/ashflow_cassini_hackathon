import tifffile
import numpy as np
from scipy.ndimage import distance_transform_edt

# load dNBR and NDWI
dnbr = np.squeeze(tifffile.imread("dnbr_rocchette_2025.tif"))
ndwi = np.squeeze(tifffile.imread("real_ndwi_rocchette.tif"))

# burn severity
severity = np.zeros_like(dnbr, dtype=int)
severity[(dnbr >= 0.10) & (dnbr < 0.27)] = 1
severity[(dnbr >= 0.27) & (dnbr < 0.44)] = 2
severity[(dnbr >= 0.44)] = 3

# water mask
water_mask = ndwi > 0.0

# distance to water (in pixels)
distance_to_water = distance_transform_edt(~water_mask)

# Sentinel-2 resolution is ~10 m for this type of grid
pixel_size_m = 10
pixel_area_m2 = pixel_size_m * pixel_size_m

# basic counts
total_pixels = severity.size
burned_pixels = np.sum(severity > 0)
low_pixels = np.sum(severity == 1)
moderate_pixels = np.sum(severity == 2)
high_pixels = np.sum(severity == 3)

# burned near water thresholds
within_100m = np.sum((severity > 0) & (distance_to_water <= 10))
within_300m = np.sum((severity > 0) & (distance_to_water <= 30))
within_500m = np.sum((severity > 0) & (distance_to_water <= 50))

# area conversion
def pixels_to_hectares(n):
    return n * pixel_area_m2 / 10000

print("=== ROCCHETTE SUMMARY ===")
print(f"Total pixels: {total_pixels}")
print(f"Burned pixels: {burned_pixels} ({burned_pixels/total_pixels*100:.2f}%)")
print()
print("Burn severity:")
print(f"  Low:      {low_pixels} px  | {pixels_to_hectares(low_pixels):.2f} ha")
print(f"  Moderate: {moderate_pixels} px  | {pixels_to_hectares(moderate_pixels):.2f} ha")
print(f"  High:     {high_pixels} px  | {pixels_to_hectares(high_pixels):.2f} ha")
print()
print("Burned area near water:")
print(f"  Within 100 m: {within_100m} px | {pixels_to_hectares(within_100m):.2f} ha")
print(f"  Within 300 m: {within_300m} px | {pixels_to_hectares(within_300m):.2f} ha")
print(f"  Within 500 m: {within_500m} px | {pixels_to_hectares(within_500m):.2f} ha")