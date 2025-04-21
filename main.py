from line import Line, Point
from window import Window

def main():
    win = Window(800, 600)
    
    line = Line(Point(100, 100), Point(200, 200))
    win.draw_line(line, fill_color="blue")
    line2 = Line(Point(200, 100), Point(100, 200))
    win.draw_line(line2, fill_color="red")

    win.wait_for_close()
    print("Window closed. Exiting...")

main()
# This code creates a window with a specified width and height, and waits for the user to close it.