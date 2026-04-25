import tifffile
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import distance_transform_edt
from matplotlib.colors import ListedColormap

# --- load dNBR ---
dnbr = tifffile.imread("dnbr_rocchette_2025.tif")
dnbr = np.squeeze(dnbr)

# --- load NDWI ---
ndwi = tifffile.imread("real_ndwi_rocchette.tif")
ndwi = np.squeeze(ndwi)

print("dNBR min/max:", np.nanmin(dnbr), np.nanmax(dnbr))
print("NDWI min/max:", np.nanmin(ndwi), np.nanmax(ndwi))

# --- burn severity classes ---
severity = np.zeros_like(dnbr, dtype=int)
severity[(dnbr >= 0.10) & (dnbr < 0.27)] = 1
severity[(dnbr >= 0.27) & (dnbr < 0.44)] = 2
severity[(dnbr >= 0.44)] = 3

# --- real water mask from NDWI ---
# for sea, 0.0 is usually a reasonable first try
water_mask = ndwi > 0.0

# --- distance to water ---
distance_to_water = distance_transform_edt(~water_mask)

near_water_factor = 1 - (distance_to_water / np.nanmax(distance_to_water))
near_water_factor = np.clip(near_water_factor, 0, 1)

# --- risk score ---
severity_norm = severity / 3.0
risk = severity_norm * near_water_factor

risk_class = np.zeros_like(risk, dtype=int)
risk_class[(risk > 0.15) & (risk <= 0.35)] = 1
risk_class[(risk > 0.35) & (risk <= 0.60)] = 2
risk_class[(risk > 0.60)] = 3

burn_cmap = ListedColormap(["black", "yellow", "orange", "red"])
risk_cmap = ListedColormap(["black", "yellow", "orange", "red"])

plt.figure(figsize=(8, 8))
plt.imshow(severity, cmap=burn_cmap)
plt.title("Burn Severity - Rocchette fire")
plt.show()

plt.figure(figsize=(8, 8))
plt.imshow(water_mask, cmap="Blues")
plt.title("Real Water Mask - Rocchette")
plt.show()

plt.figure(figsize=(8, 8))
plt.imshow(near_water_factor, cmap="Blues")
plt.colorbar(label="Near-water factor")
plt.title("Proximity to Water")
plt.show()

plt.figure(figsize=(8, 8))
plt.imshow(risk_class, cmap=risk_cmap)
plt.title("Post-Fire Water Risk - Rocchette\nYellow=low, Orange=medium, Red=high")
plt.show()

plt.imsave("fire_water_risk_rocchette.png", risk_class, cmap=risk_cmap)
print("Saved: fire_water_risk_rocchette.png")