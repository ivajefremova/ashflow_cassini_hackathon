# Run Order

This folder contains the MVP prototype for post-fire water-risk screening.

## Files

### `fire_severity_rocchette.py`
Computes wildfire burn severity from Sentinel-2 using dNBR.
Output: `dnbr_rocchette_2025.tif`

### `make_real_water_mask_rocchette.py`
Computes NDWI from Sentinel-2 and creates the water layer for the same area.
Output: `real_ndwi_rocchette.tif`

### `fire_water_risk_rocchette.py`
Main prototype script.
Uses burn severity + water mask + distance to water to create a post-fire water-risk map.
Output: `fire_water_risk_rocchette.png`

### `summary_stats_rocchette.py`
Prints simple summary statistics:
- burned area
- burn severity distribution
- burned area near water

---

## Run Order

### 1. Compute burn severity
python fire_severity_rocchette.py

### 2. Compute water mask
python make_real_water_mask_rocchette.py

### 3. Compute post-fire water-risk map
python fire_water_risk_rocchette.py

### 4. Print summary statistics
python summary_stats_rocchette.py