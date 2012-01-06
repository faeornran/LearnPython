#!/usr/bin/python
# CSE 143 Homework 1 (Rectangle-Rama), in Python
# Author: Marty Stepp
#
# This provided main program uses your RectangleManager class.
# It displays a DrawingPanel, creates several random Rectangle objects,
# and adds them to your manager.  It also listens for mouse clicks, notifying
# your rectangle manager when the mouse buttons are pressed.
#
# A left-click raises a rectangle to the top of the Z-order.
# A Shift-left-click lowers a rectangle to the bottom of the Z-order.
# A right-click (or a Ctrl-left-click for Mac people) deletes a rectangle.
# A Shift-right-click (or a Shift-Ctrl-left-click for Mac people) deletes 
# all rectangles touching the mouse point.

from drawingpanel import *
from random import *
from tile import *
from tilemanager import *

# constants for the drawing panel size, rectangle sizes, and # of rects
WIDTH = 300
HEIGHT = 300
MIN_SIZE = 20
MAX_SIZE = 100
TILES = 20

manager = TileManager()
panel = DrawingPanel(300, 300)


# functions to respond to mouse events
def event_handler2(event):
    event_handler(event, True)
def event_handler(event, right=False):
    shift = event.state & 0x001 != 0
    ctrl = event.state & 0x004 != 0   # ctrl-click ~= right-click (Mac)
    right = right or ctrl
    print("click at x=" + str(event.x) + ", y=" + str(event.y) + ", right=" + str(right) + ", shift=" + str(shift) + ", ctrl=" + str(ctrl) + ", state=" + str(event.state))
    if right:
        if shift:
            manager.delete_all(event.x, event.y)
        else:
            manager.delete(event.x, event.y)
    else:
        if shift:
            manager.lower(event.x, event.y)
        else:
            manager.rise(event.x, event.y)
    
    # repaint all of the rectangles
    panel.clear()
    manager.draw_all(panel)


# main
# create several random rectangles and put them into a manager
               # random color
    
for i in range(TILES):
    w = randint(MIN_SIZE, MAX_SIZE)   # random coordinates
    h = randint(MIN_SIZE, MAX_SIZE)
    x = randint(0, WIDTH - w - 1)
    y = randint(0, HEIGHT - h - 1)
    
    r = randint(0, 255)               # random color
    g = randint(0, 255)
    b = randint(0, 255)
    color = "#%02x%02x%02x" % (r, g, b)
    
    # add random rectangle to manager
    tile = Tile(x, y, w, h, color)
    manager.add_tile(tile)

manager.draw_all(panel)

# listen for mouse clicks
panel.canvas.bind("<Button-1>", event_handler)
panel.canvas.bind("<Button-2>", event_handler2)
panel.canvas.bind("<Button-3>", event_handler2)

panel.mainloop()
