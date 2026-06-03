import os
import sys
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath('utils'))
from geo_style import configure_map, add_footer, plot_minimalist_functional, load_palette

# 1. Environment Configuration
os.makedirs('outputs', exist_ok=True)
plt.style.use('themes/academic_minimalist.mplstyle')
colors = load_palette('palettes/colors.yaml')

def export_real_spatial_map():
    """Generates a spatial map using real-world public GeoJSON data."""
    # Fetch stable global spatial data
    url_geo = "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json"
    gdf = gpd.read_file(url_geo)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Isolate target region via functional highlighting
    plot_minimalist_functional(
        gdf=gdf, target_column='name', target_value='Brazil',
        highlight_color=colors['highlight']['primary_positive'], ax=ax
    )
    
    # Establish bounding box for South America
    ax.set_xlim(-85, -30)
    ax.set_ylim(-60, 15)
    
    ax.set_title('Spatial Distribution: Target Region Isolation (Empirical Data)', pad=20)
    configure_map(ax)
    add_footer(fig, source='Public GeoJSON Boundary Dataset', author='Toolkit Automation')
    
    plt.tight_layout()
    plt.savefig('outputs/real_public_map.png', dpi=300, bbox_inches='tight')
    plt.close()
    print('SUCCESS: Spatial map successfully rendered to outputs/real_public_map.png')

def export_real_trend_chart():
    """Generates a longitudinal trend chart using empirical gapminder data."""
    # Fetch empirical statistical data
    url_csv = "https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv"
    df = pd.read_csv(url_csv)
    
    fig, ax = plt.subplots(figsize=(9, 5))
    
    # Define analytical sample
    target_nations = ['Brazil', 'Argentina', 'Bolivia']
    df_filtered = df[df['country'].isin(target_nations)]
    
    # Execute conditional plotting
    for country in target_nations:
        subset = df_filtered[df_filtered['country'] == country]
        # Highlight specific variant while suppressing background noise
        line_color = colors['highlight']['primary_alert'] if country == 'Bolivia' else colors['base']['context_gray']
        ax.plot(subset['year'], subset['lifeExp'], marker='o', label=country, color=line_color)
    
    ax.axhline(60, color=colors['highlight']['secondary_focus'], linestyle='--', linewidth=1.5)
    ax.set_title('Longitudinal Trend: Life Expectancy Variations (Empirical Data)', pad=20)
    ax.set_ylabel('Life Expectancy (Years)')
    add_footer(fig, source='Gapminder Foundation Dataset', author='Toolkit Automation')
    
    plt.tight_layout()
    plt.savefig('outputs/real_public_chart.png', dpi=300, bbox_inches='tight')
    plt.close()
    print('SUCCESS: Trend chart successfully rendered to outputs/real_public_chart.png')

if __name__ == '__main__':
    export_real_spatial_map()
    export_real_trend_chart()
