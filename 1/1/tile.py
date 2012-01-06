# CSE 143 Homework 1 (Rectangle-Rama) solution, in Python
# Author: Marty Stepp
# This provided class implements a new type of objects representing rectangles.

class Tile:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    
    def draw(self, panel):
        panel.canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, outline="black", fill=self.color)
    
    def __str__(self):
        return "(x=" + str(self.x) + ",y=" + str(self.y) + ",w=" + str(self.width) + ",h=" + str(self.height) + ")"
