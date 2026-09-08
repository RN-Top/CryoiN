# 🧭 Eyerin View & Cryoin

An interactive geospatial observation deck that visualizes a 13-station harmonic network mapped across a 1500s-style azimuthal equidistant polar projection. The system features a boreal convergence anchor at the polar center (**Sophia**) and radiates outward to the Antarctic perimeter barrier (**Cryoin**).

---

## 🌐 Overview

The platform merges cartographic modeling with an integrated generative AI mission assistant:

* **Central Anchor**: Node 0 — *Sophia (The Apex)* positioned at the polar coordinate origin ($r=0.00, \theta=0.0^\circ$).
* **12 Radial Stations**: A distributed network of ancient alignments, geological vortices, and oceanic conduits extending out to the Southern Ice Rim at $r=1.00$.
* **Harmonic Resonance Matrix**: Dynamic telemetry tracking Solfeggio vibrational frequencies (Hz), azimuth vectors, and harmonic triad geometry.
* **Transit Horizon Calculations**: Real-time UTC predictive pass windows calculated across custom cycle cadences.
* **Mission Assistant**: In-app terminal powered by Google Gemini (`gemini-2.5-flash`) for localized cartographic intelligence and alignment analysis.

---

## 📍 Station Registry

| ID | Station Name | Polar Radius ($r$) | Azimuth ($\theta$) | Frequency | Classification |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **0** | **Sophia (The Apex)** | `0.00` | `0.00°` | 963 Hz | Central Keystone / Convergence Core |
| **1** | **Giza Plateau** | `0.33` | `31.13°` | 432 Hz | Pyramidal Cardinal Gateway |
| **2** | **Stonehenge** | `0.22` | `358.17°` | 528 Hz | Megalithic Archaeoastronomy |
| **3** | **Hessdalen Valley** | `0.15` | `11.19°` | 639 Hz | Atmospheric Ion Light Station |
| **4** | **Mount Kailash** | `0.33` | `81.31°` | 852 Hz | Trans-Himalayan Axis Mundi |
| **5** | **Teotihuacan** | `0.39` | `261.16°` | 741 Hz | Solar Avenue of the Ancestors |
| **6** | **Southwest Florida** | `0.35` | `278.20°` | 417 Hz | Calusa Estuary Nexus |
| **7** | **Detroit / Canton** | `0.26` | `276.52°` | 396 Hz | Laurentian Freshwater Basin |
| **8** | **Roanoke, Virginia** | `0.29` | `280.06°` | 528 Hz | Blue Ridge Rift Threshold |
| **9** | **Sedona** | `0.31` | `248.24°` | 432 Hz | Ferrous Sandstone Vortex Core |
| **10** | **Angkor Wat** | `0.43` | `103.87°` | 639 Hz | Microcosmic Celestial Reflection |
| **11** | **Machu Picchu** | `0.57` | `287.46°` | 741 Hz | Andean Intihuatana Sun Tether |
| **12** | **Cryoin (Antarctica)** | `1.00` | `180.00°` | 174 Hz | Outer Cryosphere Perimeter Rim |

---

## 🛠️ Tech Stack

* **UI & Dashboard**: [Streamlit](https://streamlit.io/)
* **Cartographic Engine**: [Matplotlib](https://matplotlib.org/) (Polar Projection)
* **Data Structures**: [NumPy](https://numpy.org/) & [Pandas](https://pandas.pydata.org/)
* **LLM Engine**: [Google GenAI SDK](https://github.com/googleapis/python-genai) (`gemini-2.5-flash`)

---

## 🚀 Deployment (Streamlit Community Cloud)

1. Fork or push this repository to GitHub with:
   * `app.py`
   * `requirements.txt`
   * `README.md`
2. Navigate to [share.streamlit.io](https://share.streamlit.io) and click **Create app**.
3. Select this repository, set branch to `main`, and main file path to `app.py`.
4. Open **Advanced settings** $\rightarrow$ **Secrets**.
5. Supply your API key:
   ```toml
   GEMINI_API_KEY = "your_google_gemini_api_key"
