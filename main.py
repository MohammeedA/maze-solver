from window import Window

def main():
    win = Window(800, 600)
    win.wait_for_close()
    print("Window closed. Exiting...")

main()
# This code creates a window with a specified width and height, and waits for the user to close it.