class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

class Line(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas, fill_color=None):
        canvas.create_line(
            self.p1.x, self.p1.y,
            self.p2.x, self.p2.y,
            fill=fill_color,
            width=2
        )

    def __str__(self):
        return f"Line({self.p1}, {self.p2})"

    def __repr__(self):
        return f"Line({self.p1}, {self.p2})"

    def __eq__(self, other):
        if not isinstance(other, Line):
            return NotImplemented
        return (self.p1 == other.p1 and self.p2 == other.p2) or (self.p1 == other.p2 and self.p2 == other.p1)