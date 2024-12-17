import tkinter as tk
from tkinter.font import Font

class TkLabel:
    def __init__(self, text: str, x: int, y: int, bg: str, root: tk.Tk):
        self.text = text
        self.x = x
        self.y = y
        self.bg = bg
        self.label = tk.Label(root, text=self.text, bg=self.bg, width=0, height=0, font=('Helvetica', 12), anchor='nw')

    def bind(self, sequence: str, func) -> None:
        self.label.bind(sequence, func)

    def build(self) -> tk.Label:
        lines = self.text.split('\n')
        widestLine = max(lines, key=len)
        numOfLines = len(lines)
        gap = 5

        self.width = Font(font=('Helvetica', 12)).measure(widestLine) + gap
        self.height = (Font(font=('Helvetica', 12)).metrics("linespace") * numOfLines) + gap

        self.label.config(width=self.width, height=self.height)
        self.label.place(anchor='nw', x=self.x, y=self.y, width=self.width, height=self.height)

        return self.label

    def destroy(self):
        self.label.destroy();

class TkRect:
    def __init__(self, x: int, y: int, fillColor: str, outlineColor: str, canvas: tk.Canvas):
        self.canvas = canvas
        self.x0 = x
        self.y0 = y
        self.x1 = x
        self.y1 = y
        self.fillColor = fillColor
        self.outlineColor = outlineColor
        self.rect = None
        # self.rect = canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, fill=fillColor, outline=outlineColor)

    def update(self, x: int, y: int) -> None:
        if self.rect == None:
            return;
        self.x1 = x
        self.y1 = y
        self.canvas.coords(self.rect, self.x0, self.y0, self.x1, self.y1)
    
    def build(self) -> None:
        self.rect = self.canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, fill=self.fillColor, outline=self.outlineColor)

    def destroy(self) -> None:
        if self.rect == None:
            return;
        self.canvas.delete(self.rect)

