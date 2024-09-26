from .chart_base import ChartBase

class BarChart(ChartBase):
    def __init__(self, data, x, y, title="Bar Chart", **kwargs):
        super().__init__(data, x, y, title, **kwargs)

    def draw(self):
        # Logic to draw a bar chart
        pass
