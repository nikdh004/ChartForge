class Theme:
    DEFAULT = {
        'background_color': '#ffffff',
        'text_color': '#000000',
        'grid_color': '#e6e6e6'
    }

    DARK = {
        'background_color': '#333333',
        'text_color': '#ffffff',
        'grid_color': '#555555'
    }

def apply_theme(chart, theme=Theme.DEFAULT):
    # Logic to apply a theme to the chart
    chart.config['theme'] = theme
    pass
