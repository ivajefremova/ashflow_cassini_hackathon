"""
AquaFire — Configuration
All fixed parameters for the Corinthia fire demo.
"""

import os

# ── Fixed fire event ──────────────────────────────────────────────────────────
IGNITION_DATE    = "2024-09-29"
FIRE_NAME        = "Corinthia wildfire"
FIRE_REGION      = "Corinthia, Peloponnese, Greece"
FIRE_TOTAL_HA    = 8195          # confirmed by Copernicus EMSR767
COPERNICUS_REF   = "EMSR767"

# ── Output paths ──────────────────────────────────────────────────────────────
OUTPUT_DIR         = "./output"
STATS_FILE         = os.path.join(OUTPUT_DIR, "lake_upstream_stats.json")
DNBR_FILE          = os.path.join(OUTPUT_DIR, "dnbr_corinthia.tif")

# ── Severity labels ───────────────────────────────────────────────────────────
SEVERITY_LABELS = {
    0: "unburned",
    1: "low",
    2: "moderate-low",
    3: "moderate-high",
    4: "high",
}

SEVERITY_MULTIPLIER = {
    0: 0.0,
    1: 0.5,
    2: 0.75,
    3: 1.0,
    4: 1.4,
}

# ── Contaminant categories ────────────────────────────────────────────────────
# Each category has: emission factors (kg/ha), decay class, risk level
CORINE_TO_CATEGORY = {
    "forest_shrub": {
        "label":       "Forest / Shrubland",
        "contaminants": ["PAHs", "Dissolved organic carbon", "Phosphorus", "Nitrates"],
        "risk_level":  "moderate",
        "decay_class": "organic",
        "emission_factors": {
            "PAHs":                     0.050,
            "Dissolved organic carbon": 0.300,
            "Phosphorus":               0.022,
            "Nitrates":                 0.070,
        },
    },
    "agricultural": {
        "label":        "Agricultural Land",
        "contaminants": ["Pesticide residues", "Copper", "Zinc", "Nitrates"],
        "risk_level":   "moderate-high",
        "decay_class":  "nutrient",
        "emission_factors": {
            "Pesticide residues": 0.015,
            "Copper":             0.020,
            "Zinc":               0.025,
            "Nitrates":           0.150,
        },
    },
    "industrial_mining": {
        "label":        "Industrial / Mining",
        "contaminants": ["Arsenic", "Lead", "Cadmium", "Chromium", "Mercury"],
        "risk_level":   "high",
        "decay_class":  "heavy_metal",
        "emission_factors": {
            "Arsenic":   0.008,
            "Lead":      0.012,
            "Cadmium":   0.003,
            "Chromium":  0.006,
            "Mercury":   0.001,
        },
    },
    "urban_fringe": {
        "label":        "Urban Fringe",
        "contaminants": ["VOCs", "Benzene", "Lead", "Microplastics"],
        "risk_level":   "moderate-high",
        "decay_class":  "organic",
        "emission_factors": {
            "VOCs":          0.080,
            "Benzene":       0.010,
            "Lead":          0.015,
            "Microplastics": 0.020,
        },
    },
}

# ── Decay constants (negative exponential per month) ─────────────────────────
# load_month_m = peak_load * exp(-k * (m - 1))
DECAY_CONSTANTS = {
    "organic":     0.35,   # PAHs, DOC, VOCs — fast
    "nutrient":    0.20,   # phosphorus, nitrates — medium
    "heavy_metal": 0.10,   # As, Pb, Cd — slow, persistent
}

# ── Risk thresholds (kg/month above which risk is flagged) ───────────────────
RISK_THRESHOLDS = {
    "PAHs":                     {"high": 50,   "moderate": 15},
    "Dissolved organic carbon": {"high": 300,  "moderate": 80},
    "Phosphorus":               {"high": 25,   "moderate": 8},
    "Nitrates":                 {"high": 80,   "moderate": 25},
    "Pesticide residues":       {"high": 8,    "moderate": 2},
    "Copper":                   {"high": 10,   "moderate": 3},
    "Zinc":                     {"high": 12,   "moderate": 4},
    "Arsenic":                  {"high": 2,    "moderate": 0.5},
    "Lead":                     {"high": 3,    "moderate": 0.8},
    "Cadmium":                  {"high": 0.5,  "moderate": 0.1},
    "Chromium":                 {"high": 2,    "moderate": 0.5},
    "Mercury":                  {"high": 0.2,  "moderate": 0.05},
    "VOCs":                     {"high": 30,   "moderate": 8},
    "Benzene":                  {"high": 5,    "moderate": 1},
    "Microplastics":            {"high": 10,   "moderate": 3},
}
DEFAULT_THRESHOLD = {"high": 10, "moderate": 3}
