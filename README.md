# Generic Spatial DataViz Toolkit

A reproducible framework for geospatial data visualization in Python (Matplotlib + GeoPandas + Pandas), designed for academic rigor and minimalist aesthetics.

## Core Design Principles
1. **Extreme Minimalism:** Removal of redundant axes, grids, and bounding boxes (despined approach).
2. **Conditional Coloring:** Grayscale mapping by default. Hues are strictly reserved for conveying discrete analytical insights.
3. **Maximized Data-to-Ink Ratio:** Elimination of chart junk to ensure visual focus remains exclusively on spatial and statistical phenomena.

## Directory Structure
- `/themes`: Global configuration files (`.mplstyle`) for Matplotlib.
- `/palettes`: YAML configurations for semantically structured, accessible color palettes.
- `/utils`: Core functions for coordinate removal, academic footer attribution, and conditional plotting.
- `/templates`: Boilerplate scripts for rapid, standardized spatial analysis.
- `/data`: Synthetic datasets (`.csv`, `.geojson`) demonstrating expected data formats.

## Data Formatting Guidelines
To ensure compatibility with the templates, format your data as follows:
- **Spatial Data (`.geojson`, `.shp`, `.parquet`):** Must contain a categorical column (e.g., `status` or `category`) to apply conditional highlight logic.
- **Tabular Data (`.csv`):** Long-format data is preferred for time-series (e.g., `year`, `group_id`, `metric_value`).

## Usage Example

```python
import matplotlib.pyplot as plt
import geopandas as gpd

# 1. Load Academic Theme
plt.style.use('themes/academic_minimalist.mplstyle')

# 2. Load and Plot Data
gdf = gpd.read_file('data/sample_regions.geojson')
gdf.plot(color='#E0E0E0', edgecolor='white')
plt.show()
