import geopandas as gpd
import matplotlib.pyplot as plt
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))
from geo_style import configure_map, add_footer, plot_minimalist_functional, load_palette

plt.style.use('../themes/academic_minimalist.mplstyle')
colors = load_palette('../palettes/colors.yaml')

def generate_spatial_analysis_panel(data_path):
    fig, ax = plt.subplots(figsize=(10, 8))
    gdf = gpd.read_file(data_path)
    plot_minimalist_functional(
        gdf=gdf, target_column='status', target_value='Target Feature',
        highlight_color=colors['highlight']['primary_positive'], ax=ax
    )
    ax.set_title("Spatial Distribution Analysis", pad=20)
    configure_map(ax)
    add_footer(fig, source="Synthetic Spatial Grid", author="Researcher Name")
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    generate_spatial_analysis_panel("../data/sample_regions.geojson")
