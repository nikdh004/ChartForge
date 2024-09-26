from .chart_base import ChartBase

class PieChart(ChartBase):
    def __init__(self, data, labels, values, title="Pie Chart", **kwargs):
        super().__init__(data, labels, values, title, **kwargs)

    def draw(self):
        # Logic to draw a pie chart
        pass
