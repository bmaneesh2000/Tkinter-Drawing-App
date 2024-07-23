import tkinter as tk
from tkinter import colorchooser

class WhiteBoardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Whiteboard")
        
        self.pen_color = 'black'
        
        # Create a frame for the toolbar
        self.toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        self.color_button = tk.Button(self.toolbar, text='Choose Color', command=self.choose_color)
        self.color_button.pack(side=tk.LEFT, padx=2, pady=2)
        
        self.save_button = tk.Button(self.toolbar, text='Save', command=self.save_canvas)
        self.save_button.pack(side=tk.LEFT, padx=2, pady=2)

        # Add buttons to the toolbar
        self.clear_button = tk.Button(self.toolbar, text='Clear', command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT, padx=2, pady=2)
        

        
        # Create the canvas
        self.canvas = tk.Canvas(self.root, bg='white', width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<Button-1>', self.on_button_press)
        
        self.old_x = None
        self.old_y = None

    def paint(self, event):
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                                    width=2, fill=self.pen_color, capstyle=tk.ROUND, smooth=tk.TRUE)
        self.old_x = event.x
        self.old_y = event.y

    def on_button_press(self, event):
        self.old_x = event.x
        self.old_y = event.y

    def clear_canvas(self):
        self.canvas.delete('all')

    def choose_color(self):
        self.pen_color = colorchooser.askcolor(color=self.pen_color)[1]

    def save_canvas(self):
        self.canvas.postscript(file='whiteboard.ps')
        print("Canvas saved as whiteboard.ps")

if __name__ == "__main__":
    root = tk.Tk()
    app = WhiteBoardApp(root)
    root.mainloop()

