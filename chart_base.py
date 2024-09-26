class ChartBase:
    def __init__(self, data, x, y, title="", **kwargs):
        self.data = data
        self.x = x
        self.y = y
        self.title = title
        self.config = kwargs

    def set_title(self, title):
        self.title = title

    def render(self):
        # Common logic for rendering charts (axes, labels, etc.)
        pass
