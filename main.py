from line import Line, Point
from maze import Cell
from window import Window

def main():
    win = Window(800, 600)
    
    
    cell3 = Cell(200, 200, 300, 300, win)
    cell3.has_left_wall = False
    cell3.has_right_wall = True
    cell3.has_top_wall = False
    cell3.has_bottom_wall = True
    cell3.draw(200, 200, 300, 300)

    win.wait_for_close()
    print("Window closed. Exiting...")

main()
# This code creates a window with a specified width and height, and waits for the user to close it.