import unittest
from maze import Cell

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

if __name__ == '__main__':
    unittest.main()