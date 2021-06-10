import matplotlib.pyplot as plt
from numpy import select
import math

class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def area(self):
        return math.pi * self.radius * self.radius

    def inside(self, x, y):
        dx = x - self.x
        dy = y - self.y
        return math.sqrt(dx*dx + dy*dy) <= self.radius

circles = [
    Circle(4,6,1,"red"),
    Circle(2,8,1.5,"blue"),
    Circle(7,3,2,"green")
]

mouse_down = False
selected_circle = None

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])

def draw_circles():
    ax.patches = []
    for c in circles:
        ax.add_patch(plt.Circle((c.x, c.y), c.radius, fc=c.color, alpha=0.85, ec="black"))
    fig.canvas.draw()

draw_circles()

def update_circle(x,y):
    global selected_circle
    for c in circles:
        if c.inside(x,y):
            selected_circle = c
            break

def onclick(event):
    global mouse_down
    mouse_down = True
    if event.xdata != None and event.ydata != None:
        update_circle(event.xdata, event.ydata)
    # print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
    #       (event.button, event.x, event.y, event.xdata, event.ydata))

def onmove(event):
    if mouse_down and selected_circle and event.xdata != None and event.ydata != None:
        selected_circle.x = event.xdata
        selected_circle.y = event.ydata
        draw_circles()

def onrelease(event):
    global mouse_down
    global selected_circle
    mouse_down = False
    selected_circle = None

cid = fig.canvas.mpl_connect('button_press_event', onclick)
cid2 = fig.canvas.mpl_connect('motion_notify_event', onmove)
cid3 = fig.canvas.mpl_connect('button_release_event', onrelease)
plt.show()