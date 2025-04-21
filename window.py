from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width: int, height: int):
        self.__root = Tk()
        self.__root.title("Window")
        self.canvas = Canvas(self.__root, width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=True)
        self.running = False
    
    def redraw(self):
        # Redraw the canvas if needed
        self.canvas.update_idletasks()
        self.canvas.update()
        self.__root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.destroy()

    def on_resize(self, event):
        # Handle window resize if needed
        pass