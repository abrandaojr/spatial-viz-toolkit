import os
import sys
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath('utils'))
from geo_style import configure_map, add_footer, plot_minimalist_functional, load_palette

# 1. Setup Environment
os.makedirs('outputs', exist_ok=True)
plt.style.use('themes/academic_minimalist.mplstyle')
colors = load_palette('palettes/colors.yaml')

def export_spatial_map():
    fig, ax = plt.subplots(figsize=(10, 8))
    gdf = gpd.read_file('data/sample_regions.geojson')
    plot_minimalist_functional(
        gdf=gdf, target_column='status', target_value='Target Feature',
        highlight_color=colors['highlight']['primary_positive'], ax=ax
    )
    ax.set_title('Spatial Distribution Analysis', pad=20)
    configure_map(ax)
    add_footer(fig, source='Synthetic Spatial Grid', author='Researcher Name')
    plt.tight_layout()
    plt.savefig('outputs/spatial_map.png', dpi=300, bbox_inches='tight')
    plt.close()
    print('SUCCESS: Map exported to outputs/spatial_map.png')

def export_trend_chart():
    df = pd.read_csv('data/sample_trends.csv')
    fig, ax = plt.subplots(figsize=(9, 5))
    for group in df['group_id'].unique():
        subset = df[df['group_id'] == group]
        is_alert = 'Critical Alert' in subset['category'].values or 'Observed Deficit' in subset['category'].values
        line_color = colors['highlight']['primary_alert'] if is_alert else colors['base']['context_gray']
        ax.plot(subset['year'], subset['metric_value'], marker='o', label=group, color=line_color)
    ax.axhline(50, color=colors['highlight']['secondary_focus'], linestyle='--', linewidth=1.5)
    ax.set_title('Longitudinal Trend Analysis', pad=20)
    ax.set_ylabel('Metric Value')
    add_footer(fig, source='Synthetic Trend Data', author='Researcher Name')
    plt.tight_layout()
    plt.savefig('outputs/trend_chart.png', dpi=300, bbox_inches='tight')
    plt.close()
    print('SUCCESS: Chart exported to outputs/trend_chart.png')

if __name__ == '__main__':
    export_spatial_map()
    export_trend_chart()
