class Picture:
    def __init__(self, width, height, values):
        self.width = width
        self.height = height
        self.values = values


    def show_values(self, x, y):
        return self.values[y][x]


    def set_values(self, x, y, custom):
        self.values[y][x] = custom


class BinaryPicture(Picture):
    def __init__(self, width, height, values=None):
        if not values:
            values = [[0] * width for _ in range(height)]
        super().__init__(width, height, values)


class MonochromePicture(Picture):
    def __init__(self, width, height, values=None):
        if not values:
            values = [[0] * width for _ in range(height)]
        super().__init__(width, height, values)


class ColorPicture(Picture):
    def __init__(self, width, height, values=None):
        if not values:
            values = [[[0, 0, 0] for _ in range(width)] for _ in range(height)]
        super().__init__(width, height, values)
