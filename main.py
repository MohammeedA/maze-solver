from line import Line, Point
from maze import Cell
from window import Window

def main():
    win = Window(800, 600)
    cell = Cell(0, 0, 100, 100, win)
    cell.has_left_wall = True
    cell.has_right_wall = True
    cell.has_top_wall = True
    cell.has_bottom_wall = False
    cell.draw(0, 0, 100, 100)
    cell1 = Cell(0, 100, 100, 200, win)
    cell1.has_left_wall = True
    cell1.has_right_wall = True
    cell1.has_top_wall = False
    cell1.has_bottom_wall = True
    cell1.draw(0, 100, 100, 200)
    cell.draw_move(cell1, undo=True)

    win.wait_for_close()
    print("Window closed. Exiting...")

main()
# This code creates a window with a specified width and height, and waits for the user to close it.