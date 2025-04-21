from line import Line, Point


class Cell(object):
    """
    A class representing a cell in a grid.
    """

    def __init__(self, x1, y1, x2, y2, window=None):
        """
        Initialize a cell with its coordinates and an optional window.

        :param x1: The x-coordinate of the top-left corner.
        :param y1: The y-coordinate of the top-left corner.
        :param x2: The x-coordinate of the bottom-right corner.
        :param y2: The y-coordinate of the bottom-right corner.
        :param window: An optional window object (default is None).
        """
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self.window = window
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self, x1, y1, x2, y2):
        """
        Draw the cell on the window.

        :param x1: The x-coordinate of the top-left corner.
        :param y1: The y-coordinate of the top-left corner.
        :param x2: The x-coordinate of the bottom-right corner.
        :param y2: The y-coordinate of the bottom-right corner.
        """
        if self.window:
            if self.has_left_wall:
                self.window.draw_line(Line(Point(x1, y1), Point(x1, y2)))
            if self.has_right_wall:
                self.window.draw_line(Line(Point(x2, y1), Point(x2, y2)))
            if self.has_top_wall:
                self.window.draw_line(Line(Point(x1, y1), Point(x2, y1)))
            if self.has_bottom_wall:
                self.window.draw_line(Line(Point(x1, y2), Point(x2, y2)))
        else:
            raise ValueError("No window provided to draw the cell.")
        
    def __repr__(self):
        """
        Return a string representation of the cell.

        :return: A string representing the cell's coordinates.
        """
        return f"Cell({self._x1}, {self._y1}, {self._x2}, {self._y2})"