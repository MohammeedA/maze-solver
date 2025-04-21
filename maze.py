import random
import time
from line import Line, Point

class Maze(object):
    """
    A class representing a maze.
    """

    def __init__(self, x1, y1, num_rows, num_cols, cell_width, cell_height, window=None, seed=None):
        """
        Initialize a maze with its dimensions and an optional window.

        :param x1: The x-coordinate of the top-left corner.
        :param y1: The y-coordinate of the top-left corner.
        :param num_rows: The number of cells in the x-direction.
        :param num_cols: The number of cells in the y-direction.
        :param cell_width: The width of each cell.
        :param cell_height: The height of each cell.
        :param window: An optional window object (default is None).
        """
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.window = window
        if seed is not None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        """
        Create the cells of the maze based on the specified dimensions.
        """
        self.cells = []
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                # Calculate cell coordinates - j is for x (columns), i is for y (rows)
                x1 = self._x1 + j * self.cell_width  # Changed from i to j
                y1 = self._y1 + i * self.cell_height # Changed from j to i
                x2 = x1 + self.cell_width
                y2 = y1 + self.cell_height
                cell = Cell(x1, y1, x2, y2, self.window)
                row.append(cell)
            self.cells.append(row)
            
        # Draw cells if window exists
        if self.window:
            for i in range(self.num_rows):
                for j in range(self.num_cols):
                    self._draw_cell(i, j)

    def _break_entrance_and_exit(self):
        """
        Break the entrance (top wall of top-left cell) and exit (bottom wall of bottom-right cell).
        """
        # Break entrance (top wall of first cell)
        self.cells[0][0].has_top_wall = False
        if self.window:
            self._draw_cell(0, 0)
        
        # Break exit (bottom wall of last cell)
        self.cells[-1][-1].has_bottom_wall = False
        if self.window:
            self._draw_cell(self.num_rows-1, self.num_cols-1)

    def _draw_cell(self, i, j):
        """
        Draw a cell in the maze.

        :param i: The x-index of the cell.
        :param j: The y-index of the cell.
        """
        if not self.window:
            return
            
        cell = self.cells[i][j]
        x1 = cell._x1
        y1 = cell._y1
        x2 = cell._x2
        y2 = cell._y2
        cell.draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        """
        Animate the maze drawing process.
        """
        if self.window:
            self.window.redraw()
            time.sleep(0.05)  # Adjust the sleep time for animation speed
        else:
            raise ValueError("No window provided to animate the maze.")
    
    def _break_walls_r(self, i, j):
        """
        Recursive method to break walls between cells using depth-first traversal.
        Preserves the outer walls of the maze except for entrance and exit.
        
        :param i: Current cell's row index
        :param j: Current cell's column index
        """
        # Mark current cell as visited
        self.cells[i][j].visited = True
        self._draw_cell(i, j)
        
        # Get all possible directions and randomize their order
        possible_directions = []
        
        # Up - Allow in all rows except breaking the top border wall (except entrance)
        if i > 0 and not self.cells[i-1][j].visited:
            possible_directions.append((i-1, j))
                
        # Right - Allow if not at rightmost column
        if j < self.num_cols-1 and not self.cells[i][j+1].visited:
            possible_directions.append((i, j+1))
            
        # Down - Allow in all rows except breaking the bottom border wall (except exit)
        if i < self.num_rows-1 and not self.cells[i+1][j].visited:
            possible_directions.append((i+1, j))
                
        # Left - Allow if not at leftmost column
        if j > 0 and not self.cells[i][j-1].visited:
            possible_directions.append((i, j-1))
        
        # Randomize the order of directions
        random.shuffle(possible_directions)
        
        # Try each direction
        for next_i, next_j in possible_directions:
            # If the next cell hasn't been visited yet
            if not self.cells[next_i][next_j].visited:
                # Break walls between current cell and chosen cell
                if next_i < i:  # Going up
                    self.cells[i][j].has_top_wall = False
                    self.cells[next_i][next_j].has_bottom_wall = False
                elif next_i > i:  # Going down
                    self.cells[i][j].has_bottom_wall = False
                    self.cells[next_i][next_j].has_top_wall = False
                elif next_j < j:  # Going left
                    self.cells[i][j].has_left_wall = False
                    self.cells[next_i][next_j].has_right_wall = False
                else:  # Going right
                    self.cells[i][j].has_right_wall = False
                    self.cells[next_i][next_j].has_left_wall = False
                
                # Recursively process the next cell
                self._break_walls_r(next_i, next_j)
    
    def _reset_cells_visited(self):
        """
        Reset the visited status of all cells in the maze.
        """
        for row in self.cells:
            for cell in row:
                cell.visited = False
    
    def solve(self):
        """
        Solve the maze using a depth-first search algorithm.
        """
        # Start solving from the entrance (top-left cell)
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        """
        Recursive method to solve the maze.

        :param i: Current cell's row index
        :param j: Current cell's column index
        :return: True if the exit is reached, False otherwise
        """
        self._animate()
        # Mark current cell as visited
        self.cells[i][j].visited = True
        if self.cells[i][j] == self.cells[-1][-1]:
            # Reached the exit
            return True
        # Get all possible directions
        possible_directions = []
        # Up
        if i > 0 and not self.cells[i-1][j].visited and not self.cells[i][j].has_top_wall:
            possible_directions.append((i-1, j))
        # Right
        if j < self.num_cols-1 and not self.cells[i][j+1].visited and not self.cells[i][j].has_right_wall:
            possible_directions.append((i, j+1))
        # Down
        if i < self.num_rows-1 and not self.cells[i+1][j].visited and not self.cells[i][j].has_bottom_wall:
            possible_directions.append((i+1, j))
        # Left
        if j > 0 and not self.cells[i][j-1].visited and not self.cells[i][j].has_left_wall:
            possible_directions.append((i, j-1))
        
        for next_i, next_j in possible_directions:
            # If the next cell hasn't been visited yet
            if not self.cells[next_i][next_j].visited:
                # Draw the move
                self.cells[i][j].draw_move(self.cells[next_i][next_j])
                # Recursively process the next cell
                if self._solve_r(next_i, next_j):
                    return True
                else:
                    # Undo the move if it doesn't lead to a solution
                    self.cells[i][j].draw_move(self.cells[next_i][next_j], undo=True)
        
        return False

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
        self.visited = False  # Add visited flag for maze generation

    def draw(self, x1, y1, x2, y2):
        """
        Draw the cell on the window.

        :param x1: The x-coordinate of the top-left corner.
        :param y1: The y-coordinate of the top-left corner.
        :param x2: The x-coordinate of the bottom-right corner.
        :param y2: The y-coordinate of the bottom-right corner.
        """
        if self.window:
            # Draw existing walls in black, removed walls in background color
            if self.has_left_wall:
                self.window.draw_line(Line(Point(x1, y1), Point(x1, y2)))
            else:
                self.window.draw_line(Line(Point(x1, y1), Point(x1, y2)), fill_color="white")
                
            if self.has_right_wall:
                self.window.draw_line(Line(Point(x2, y1), Point(x2, y2)))
            else:
                self.window.draw_line(Line(Point(x2, y1), Point(x2, y2)), fill_color="white")
                
            if self.has_top_wall:
                self.window.draw_line(Line(Point(x1, y1), Point(x2, y1)))
            else:
                self.window.draw_line(Line(Point(x1, y1), Point(x2, y1)), fill_color="white")
                
            if self.has_bottom_wall:
                self.window.draw_line(Line(Point(x1, y2), Point(x2, y2)))
            else:
                self.window.draw_line(Line(Point(x1, y2), Point(x2, y2)), fill_color="white")
        else:
            raise ValueError("No window provided to draw the cell.")
    
    def draw_move(self, to_cell, undo=False):
        """
        Draw a move from this cell to another cell.

        :param to_cell: The target cell to move to.
        :param undo: If True, draw the move in reverse (default is False).
        """
        if self.window:
            if undo:
                self.window.draw_line(
                    Line(
                        Point( abs((self._x1 + self._x2))/2, abs((self._y1 + self._y2))/2), 
                        Point( abs((to_cell._x1 + to_cell._x2))/2, abs(to_cell._y1 + to_cell._y2)/2)
                    ),
                    fill_color="gray"
                )
            else:
                self.window.draw_line(
                    Line(
                        Point( abs(self._x1 + self._x2)/2, abs(self._y1 + self._y2)/2), 
                        Point( abs(to_cell._x1 + to_cell._x2)/2, abs(to_cell._y1 + to_cell._y2)/2)
                    ),
                    fill_color="red"
                )
        else:
            raise ValueError("No window provided to draw the move.")

    def __repr__(self):
        """
        Return a string representation of the cell.

        :return: A string representing the cell's coordinates.
        """
        return f"Cell({self._x1}, {self._y1}, {self._x2}, {self._y2})"