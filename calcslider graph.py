import tkinter as tk
import numpy as np

class calcslider:
    def __init__(self, root):
        
        #makes graphh of 600 by 400 pixels and axes from -10 to 10
        self.width = 600
        self.height = 400
        self.x1, self.x2 = -10, 10
        self.y1, self.y2 = -10, 10

        #created drawing area/canvas
        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg="white")
        self.canvas.pack()
        
        #uses click method to send coordinates of mouse click
        self.canvas.bind("<Button-1>", self.click)
        
        #draws x and y axes when madde
        self.draw_axes()

    #converts math coordinates to screen coords
    def screenx(self, x):
        return (x - self.x1) / (self.x2 - self.x1) * self.width
    #changes math coordinates to screen coords and inverts y axis 
    def screeny(self, y):
        return self.height - (y - self.y1) / (self.y2 - self.y1) * self.height
    #converts screen coordinates to math coordinates
    def mathx(self, x):
        return self.x1 + x / self.width * (self.x2 - self.x1)
    #converts screen coordinates to math coordinates and inverts y axis
    def mathy(self, y):
        return self.y2 - y / self.height * (self.y2 - self.y1)
    #draws x axsis and y axis on canvas
    def draw_axes(self):
        self.canvas.create_line(0, self.screeny(0), self.width, self.screeny(0))
        self.canvas.create_line(self.screenx(0), 0, self.screenx(0), self.height)

    def plot(self, xs, ys):
        points = []
        for i in range(len(xs)):
            points += [self.screenx(xs[i]), self.screeny(ys[i])]
        self.canvas.create_line(points, fill="blue")
    #prints math coords of mouse clicks 
    def click(self, event):
        print(round(self.mathx(event.x), 2), round(self.mathy(event.y), 2))

root = tk.Tk()
graph = calcslider(root)

#can change the function being graphed by changing the equation in the y variable VVV
x = np.linspace(-5, 5, 100)
#will graph the function y = x^2 or can be changed if you want to graph a different function
y = x ** 2
graph.plot(x, y)

root.mainloop()