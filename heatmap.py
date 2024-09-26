from .chart_base import ChartBase

class Heatmap(ChartBase):
    def __init__(self, data, x, y, title="Heatmap", **kwargs):
        super().__init__(data, x, y, title, **kwargs)

    def draw(self):
        # Logic to draw a heatmap
        pass
