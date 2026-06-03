import matplotlib.pyplot as plt
import yaml

def load_palette(yaml_path):
    with open(yaml_path, 'r') as file:
        return yaml.safe_load(file)

def configure_map(ax):
    ax.axis('off')
    ax.set_aspect('equal')

def add_footer(fig, source="Data Source", author="Author Name"):
    text = f"Source: {source} | Visualization: {author}"
    fig.text(0.02, 0.02, text, fontsize=9, color='#777777', ha='left')

def plot_minimalist_functional(gdf, target_column, target_value, highlight_color, ax):
    gdf.plot(ax=ax, color='#E0E0E0', edgecolor='white', linewidth=0.3)
    highlight_gdf = gdf[gdf[target_column] == target_value]
    if not highlight_gdf.empty:
        highlight_gdf.plot(ax=ax, color=highlight_color, edgecolor='none')
