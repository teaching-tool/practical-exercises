from advalg.circles import CircleAnimation
from advalg.circle import Circle
import math
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.backend_bases import MouseButton
from matplotlib.widgets import Button, Slider

class State:
    def __init__(self):
        self.circles = []
        self.radius = 5
        self.dragging = None

    def circle_count(self):
        return len(self.circles)
    
    def set_radius(self, value):
        self.radius = value

    def add_circle(self, circle):
        self.circles.append(circle)
    
    def delete_circle(self, circle_idx):
        del self.circles[circle_idx]

    def set_dragging(self, circle):
        self.dragging = circle

state = State()
colors = [c for c in mcolors.TABLEAU_COLORS]
colors.reverse()
max_circles = len(colors)

# Set up circles area
fig,ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

# Add size slider
slider_ax = plt.axes([0.2, 0.9, 0.6, 0.05])
freq_slider = Slider(
    ax=slider_ax,
    label='Radius',
    valmin=1,
    valmax=25,
    valinit=state.radius,
    initcolor=None
)
freq_slider.on_changed(state.set_radius)

# On click event
def on_click(event):
    if not event.inaxes == ax:
        return

    x,y = event.xdata, event.ydata

    if event.button == MouseButton.LEFT:
        left_click(x,y)
    elif event.button == MouseButton.RIGHT:
        right_click(x,y)

def left_click(x, y):
    clicked_circle = in_circle(x,y)
    if clicked_circle is None:
        if state.circle_count() == max_circles:
            print("Maximum number of circles reached")
        else:
            add_circle(x, y, state.radius)
    else:
        state.set_dragging(state.circles[clicked_circle])

def right_click(x, y):
    clicked_circle = in_circle(x,y)
    if clicked_circle is not None:
        delete_circle(clicked_circle)

def inside(circle : plt.Circle, x, y):
    dx = x - circle.center[0]
    dy = y - circle.center[1]
    return math.sqrt(dx*dx + dy*dy) <= circle.radius

#Reverse
def in_circle(x, y):
    for i,c in enumerate(state.circles):
        if inside(c,x,y):
            return i
    return None

def add_circle(x, y, radius):
    color = colors.pop()
    circle = plt.Circle((x, y), radius, alpha=0.85, ec="black", fc=color)
    state.add_circle(circle)
    ax.add_patch(circle)
    fig.canvas.draw()

def delete_circle(circle_idx):
    circle = state.circles[circle_idx]
    colors.append(circle.get_fc())
    circle.remove()
    state.delete_circle(circle_idx)
    fig.canvas.draw()

def on_release(event):
    state.set_dragging(None)

def on_move(event):
    if not event.inaxes == ax or state.dragging is None:
        return
    state.dragging.center = (event.xdata, event.ydata)
    fig.canvas.draw()

def get_circles():
    circles = []

    for c in state.circles:
        x,y = c.center
        r = c.get_radius()
        color = c.get_fc()
        circles.append(Circle(x,y,r,color))
    
    return circles

def start_animation():
    #BEGIN ANIMATION
    pass

def on_start_clicked(event):
    circles = get_circles()
    start_animation()
    
# Add start button
btn_ax = plt.axes([0.45, 0.05, 0.1, 0.05])
btn = Button(btn_ax, "Start")
btn.on_clicked(on_start_clicked)

# Add click event to canvas
fig.canvas.mpl_connect('button_press_event', on_click)
fig.canvas.mpl_connect('button_release_event', on_release)
fig.canvas.mpl_connect('motion_notify_event', on_move)

def test_circle_sampler(sampler):
    plt.show()