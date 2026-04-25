# Technical Report: Satellite-Based Intelligence for Post-Fire Water Contamination

**Project Title:** ASHFLOW
**Category:** Tracking and preventing water pollution   
**Hackathon:** 11th Cassini EU Hackathon 2026

---

## 1. Executive Summary
This report details a high-fidelity API and monitoring system designed to mitigate the secondary environmental impacts of wildfires. While fire damage is often measured in hectares burned, the subsequent contamination 
of water reservoirs via ash runoff represents a multi-billion euro threat to the European agricultural and insurance sectors. By integrating **Copernicus Sentinel** data, we provide a predictive risk-modeling tool that tracks toxic
runoff from the burn scar to the reservoir.

---

## 2. The Problem Landscape

### 2.1 The "Black Water" Phenomenon
Wildfires create a chemically complex layer of ash containing concentrated nitrates, phosphates, and heavy metals (e.g., Lead, Arsenic). When the first significant rain event occurs post-fire, this material is mobilized.

* **The Erosion Factor:** Fires destroy the vegetation that stabilizes soil, leading to massive sediment transport.
* **The Hydrological Link:** Rain carries this sediment into streams and eventually into large-scale water reservoirs.

### 2.2 Economic Impact & Stakeholder Analysis
We have identified two primary sectors suffering from a **"data gap"** in post-fire recovery:

#### **A. Agricultural Businesses**
* **Equipment Damage:** Ash and fine sediment clog advanced irrigation filters and pumps, leading to mechanical failure.
* **Crop Health:** High pH levels and heavy metal concentrations in irrigation water can lead to crop toxicity and loss of "organic" certifications.
* **Financial Loss:** Operational costs typically spike by **15–25%** due to emergency water hauling.

#### **B. Insurance Companies**
* **Inaccurate Risk Assessment:** Traditional models fail to account for the delay between a fire and the resulting water quality claim.
* **Payout Volatility:** Without predictive data, insurers cannot advise clients on mitigation, leading to avoidable maximum-loss payouts.

---

## 3. Space Data & Earth Observation Strategy

Our solution relies on the synergy between Copernicus assets to create a holistic view of the disaster.

| Satellite / Service | Instrument / Data | Application |
| :--- | :--- | :--- |
| **Sentinel-2** | Multispectral (MSI) | NIR and SWIR bands are used to calculate the **Normalized Burn Ratio (NBR)** to map fire perimeters and severity. |
| **Sentinel-3** | OLCI & SLSTR | Monitoring water quality parameters like **Chlorophyll-a** and **Total Suspended Matter (TSM)** to validate runoff models. |
| **CLMS** | Digital Elevation Models | Utilized to determine **topographic slope** and the flow direction of water toward reservoirs. |



---

## 4. Technical Architecture

### 4.1 The Contamination Risk API
The core of our project is a RESTful API that processes spatial data and returns a **Contamination Probability Index (CPI)**.

$$CPI = (B \times 0.45) + (S \times 0.25) + (P \times 0.30)$$

* **Burnt Content ($B$ - 45%):** High-severity burns produce more mobile ash.
* **Topographic Slope ($S$ - 25%):** Steeper terrain accelerates runoff.
* **Proximity & Connectivity ($P$ - 30%):** Calculated using distance to reservoirs and river network connectivity.

### 4.2 Threshold Logic & Visualization
When the API detects a CPI exceeding **0.75**, the system triggers a **"Critical State"** on the dashboard.

1.  **Primary Screen:** Interactive Map showing fire perimeters (Red) and Reservoir catchments (Blue).
2.  **Secondary Screen:** Displays estimated contaminant load and specific warnings (e.g., *"High Risk of Pump Clogging"*).

---

## 5. Implementation & Code Logic

### 5.1 Data Pipeline
The program follows a structured processing flow:

1.  **Collection Querying:** Using the **Sentinel Hub API** to pull the latest L2A imagery.
2.  **Masking & Indices:** Automated cloud masking followed by NBR calculation.
3.  **Watershed Analysis:** Utilizing libraries like **PySheds** to delineate the drainage basin of the target reservoir.
4.  **API Payload:** Results are serialized into JSON for the frontend.

#### Technical Report: Post-Fire Downstream Contaminant Risk Pipeline

This report details a specialized analytical framework designed to quantify water quality risks following wildfire events. By integrating Earth Observation (EO) data with land-use classifications and hydrological modeling, the pipeline identifies specific chemical threats to European water reservoirs.

---

##### Burn Severity and Perimeter Mapping
The process initiates with fire detection utilizing **Sentinel-2** satellite imagery. By calculating the **differenced Normalized Burn Ratio (dNBR)**, the system establishes a precise burned area perimeter and classifies fire severity levels. While these datasets are standard within the Copernicus ecosystem, they serve as the critical trigger for the downstream analytical chain.

The dNBR is calculated as:
$$\Delta NBR = NBR_{pre\_fire} - NBR_{post\_fire}$$
Where:
$$NBR = \frac{NIR - SWIR}{NIR + SWIR}$$

---

##### Geospatial Intersection and Baseline Analysis
The identified burned area is overlaid onto two preloaded, static EU datasets to determine the environmental baseline:
* **CORINE Land Cover:** Defines the land use of the affected area (e.g., forest, agricultural, industrial, or mining).
* **LUCAS Topsoil Map:** Provides a 1 km resolution profile of heavy metal concentrations inherently present in the soil.

This intersection establishes the specific "source term"—identifying exactly what material burned and what chemical constituents were present in the soil—forming a unique data layer not currently available in the commercial market.

---

##### Land-Use Based Contaminant Profiling
Following the intersection, the pipeline assigns a generalized contaminant profile based on the land-use class. This classification is the core differentiator of the system, recognizing that specific chemical risks vary by fuel source:

| Land-Use Class | Primary Contaminant Focus |
| :--- | :--- |
| **Forestry** | PAHs, organic carbon, and phosphorus. |
| **Agriculture** | Pesticide residues and fertilizer-derived copper ($Cu$) and zinc ($Zn$). |
| **Industrial / Mining** | High-risk heavy metal loads (e.g., $As, Cd, Cr, Hg, Pb$). |
| **Urban Fringe** | Volatile Organic Compounds (VOCs) and benzene. |

---

##### Hydrological Transport Modeling
The transport of these contaminants is modeled using **EU-DEM** elevation data and **EU-Hydro** river networks. By identifying reservoirs within the downstream catchment and integrating **ERA5 rainfall forecasts**, the model estimates slope-driven runoff velocity. This produces specific arrival windows:
* **Days to Weeks:** Arrival of sediment and organic contamination.
* **Months to 2 Years:** Arrival of heavy metal loads.

---

##### Risk Quantification and Interface Delivery
The final output is a localized risk score delivered via a map interface. Each downstream reservoir is assigned a risk profile categorized by contaminant class, providing water management authorities with:
1.  **Probability** of contamination.
2.  **Timing estimates** for arrival.
3.  **Specific chemical threats** based on the upstream burn profile.

### 5.2 Processing Details
> [Insert deep dive into your specific Python/C++/Java functions, database schema in Supabase, or frontend logic here.]

---

## 6. Conclusion & Future Roadmap
By turning complex satellite imagery into a simple **"Risk Score,"** we empower businesses to move from a reactive to a proactive stance. 


---

### 👥 Team Contributions
* **Iva Jefremova:** UI/UX Design Lead, Presentation Logic, & Frontend Integration.
* **Aleksei Pankov:** Satellite Data Processing & Backend Architecture.
* **Oskar Podkowa:** Leadership and Team Coordination, Economic Research & Business Logic Development.
#### The team displays collective contribution to the code and the presentation
