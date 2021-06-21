from advalg.circle import Circle
import math
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.backend_bases import MouseButton
from matplotlib.widgets import Button, Slider

class CircleEditor:
    def __init__(self, start_action):
        self.start_action = start_action
        self.circles = []
        self.radius = 5
        self.dragging = None
        self.colors = [c for c in mcolors.TABLEAU_COLORS]
        self.colors.reverse()
        self.max_circles = len(self.colors)

        # Set up figure
        fig = plt.figure()
        fig.set_size_inches(8,6)
        fig.canvas.manager.set_window_title("Circle Editor")
        self.fig = fig

        # Set up drawings axes
        ax = plt.axes([0.125, 0.125, 0.75, 0.75])
        ax.set_aspect('equal', adjustable='box')
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        self.ax = ax

        # Add size slider
        slider_ax = plt.axes([0.3, 0.9, 0.4, 0.05])
        freq_slider = Slider(
            ax=slider_ax,
            label='Radius',
            valmin=1,
            valmax=25,
            valinit=self.radius,
            initcolor="none"
        )
        freq_slider.on_changed(self.set_radius)

        # Add start button
        btn_ax = plt.axes([0.45, 0.01, 0.1, 0.05])
        btn = Button(btn_ax, "Start")
        btn.on_clicked(self.on_start_clicked)

        # Add click event to canvas
        fig.canvas.mpl_connect('button_press_event', self.on_click)
        fig.canvas.mpl_connect('button_release_event', self.on_release)
        fig.canvas.mpl_connect('motion_notify_event', self.on_move)

        # Show the editor
        plt.show()

    def set_radius(self, r):
        self.radius = r

    def on_click(self, event):
        if not event.inaxes == self.ax:
            return

        x,y = event.xdata, event.ydata

        if event.button == MouseButton.LEFT:
            self.left_click(x,y)
        elif event.button == MouseButton.RIGHT:
            self.right_click(x,y)

    def left_click(self, x, y):
        clicked_circle = self.in_circle(x,y)
        if clicked_circle is None:
            if len(self.circles) == self.max_circles:
                print("Maximum number of circles reached")
            else:
                self.add_circle(x, y, self.radius)
        else:
            self.dragging = self.circles[clicked_circle]

    def right_click(self, x, y):
        clicked_circle = self.in_circle(x,y)
        if clicked_circle is not None:
            self.delete_circle(clicked_circle)

    def inside(self, circle, x, y):
        dx = x - circle.center[0]
        dy = y - circle.center[1]
        return math.sqrt(dx*dx + dy*dy) <= circle.radius

    def in_circle(self, x, y):
        circle_indices = list(enumerate(self.circles))
        for i,c in reversed(circle_indices):
            if self.inside(c,x,y):
                return i
        return None

    def add_circle(self, x, y, radius):
        color = self.colors.pop()
        circle = plt.Circle((x, y), radius, alpha=0.85, ec="black", fc=color)
        self.circles.append(circle)
        self.ax.add_patch(circle)
        self.fig.canvas.draw()

    def delete_circle(self, circle_idx):
        circle = self.circles[circle_idx]
        self.colors.append(circle.get_fc())
        circle.remove()
        del self.circles[circle_idx]
        self.fig.canvas.draw()

    def on_release(self, event):
        self.dragging = None

    def on_move(self, event):
        if not event.inaxes == self.ax or self.dragging is None:
            return
        self.dragging.center = (event.xdata, event.ydata)
        self.fig.canvas.draw()

    def get_circles(self):
        circles = []

        for c in reversed(self.circles):
            x,y = c.center
            r = c.get_radius()
            color = c.get_fc()
            circles.append(Circle(x,y,r,color))
        
        return circles

    def on_start_clicked(self, event):
        circles = self.get_circles()
        self.start_action(circles)
