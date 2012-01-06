'''
Created on Jan 4, 2012

@author: vaughanj
'''
class TileManager:
    def __init__(self):
        self.list = []
        
    def add_tile(self, rect):
        self.list.append(rect)
        
    def draw_all(self, panel):
        for rect in self.list:
            rect.draw(panel)
            
            
    def tile_touches(self, rect, x, y):
        return (rect.x <= x) and (rect.x + rect.width >= x) \
              and (rect.y <= y) and (rect.y + rect.height >= y)
    
    def get_top(self, x, y):
        for i in range(len(self.list)-1, -1, -1):
            rect = self.list[i]
            if self.tile_touches(rect, x, y):
                return i
                break
        return -1
            
    def align(self, fn, x, y):
        i = self.get_top(x, y)
        if i != -1:
            fn(self.list, i)
        
    def rise(self, x, y):
        self.align((lambda l, i: l.append(l.pop(i))), x, y)

    def lower(self, x, y):
        self.align((lambda l, i: l.insert(0, l.pop(i))), x, y)
    
    def delete(self, x, y):
        i = self.get_top(x, y)
        if i != -1:
            self.list.pop(i)
    
    def delete_all(self, x, y):
        for rect in self.list.__reversed__():
            if self.tile_touches(rect, x, y):
                self.list.remove(rect)
            