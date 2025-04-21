from line import Line, Point
from maze import Cell, Maze
from window import Window

def main():
    win = Window(800, 600)
    maze = Maze(50, 50, 10, 10, 50, 50, win)

    print("Maze created with entrance and exit.")
    print("Solving the maze...")
    maze.solve()

    win.wait_for_close()
    print("Window closed. Exiting...")

main()
# This code creates a window with a specified width and height, and waits for the user to close it.