import unittest
from maze import Cell, Maze

class TestCell(unittest.TestCase):
    def setUp(self):
        # Create a cell without window for basic tests
        self.cell = Cell(0, 0, 10, 10)
        
    def test_cell_initialization(self):
        self.assertEqual(self.cell._x1, 0)
        self.assertEqual(self.cell._y1, 0) 
        self.assertEqual(self.cell._x2, 10)
        self.assertEqual(self.cell._y2, 10)
        self.assertIsNone(self.cell.window)
        
    def test_default_walls(self):
        self.assertTrue(self.cell.has_left_wall)
        self.assertTrue(self.cell.has_right_wall)
        self.assertTrue(self.cell.has_top_wall)
        self.assertTrue(self.cell.has_bottom_wall)
        
    def test_draw_without_window(self):
        with self.assertRaises(ValueError):
            self.cell.draw(0, 0, 10, 10)
            
    def test_draw_move_without_window(self):
        target_cell = Cell(10, 0, 20, 10)
        with self.assertRaises(ValueError):
            self.cell.draw_move(target_cell)
            
    def test_cell_repr(self):
        expected = "Cell(0, 0, 10, 10)"
        self.assertEqual(repr(self.cell), expected)

class TestMaze(unittest.TestCase):
    def setUp(self):
        # Create a small test maze without a window
        self.maze = Maze(0, 0, 2, 2, 10, 10)
        
    def test_reset_cells_visited(self):
        # First mark all cells as visited
        for row in self.maze.cells:
            for cell in row:
                cell.visited = True
                
        # Verify all cells are marked as visited
        for row in self.maze.cells:
            for cell in row:
                self.assertTrue(cell.visited)
                
        # Reset visited status
        self.maze._reset_cells_visited()
        
        # Verify all cells are now marked as not visited
        for row in self.maze.cells:
            for cell in row:
                self.assertFalse(cell.visited)
    
    def test_reset_cells_visited_mixed_state(self):
        # Mark only some cells as visited
        self.maze.cells[0][0].visited = True
        self.maze.cells[1][1].visited = True
        
        # Reset visited status
        self.maze._reset_cells_visited()
        
        # Verify all cells are now marked as not visited
        for row in self.maze.cells:
            for cell in row:
                self.assertFalse(cell.visited)

if __name__ == '__main__':
    unittest.main()