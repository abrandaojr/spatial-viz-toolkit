import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))
from geo_style import add_footer, load_palette

plt.style.use('../themes/academic_minimalist.mplstyle')
colors = load_palette('../palettes/colors.yaml')

def generate_longitudinal_trend(data_path):
    df = pd.read_csv(data_path)
    fig, ax = plt.subplots(figsize=(9, 5))
    for group in df['group_id'].unique():
        subset = df[df['group_id'] == group]
        is_alert = 'Alert' in subset['category'].values or 'Deficit' in subset['category'].values
        line_color = colors['highlight']['primary_alert'] if is_alert else colors['base']['context_gray']
        ax.plot(subset['year'], subset['metric_value'], marker='o', label=group, color=line_color)
    ax.axhline(50, color=colors['highlight']['secondary_focus'], linestyle='--', linewidth=1)
    ax.set_title("Longitudinal Trend Analysis", pad=20)
    ax.set_ylabel("Metric Value")
    add_footer(fig, source="Synthetic Trend Data", author="Researcher Name")
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    generate_longitudinal_trend("../data/sample_trends.csv")
