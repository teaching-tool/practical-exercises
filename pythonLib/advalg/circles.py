
from matplotlib import pyplot as plt
from matplotlib import animation
import math

import numpy as np

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

class CircleAnimation:
    def __init__(self, circles, sampler):
        self.circles = circles
        self.sampler = sampler(circles)
        self.sample_success = 0
        self.sample_count = 0
        self.estimates = []
        self.total_area = sum([c.area() for c in circles])

        fig = plt.figure(constrained_layout = True)
        gs = fig.add_gridspec(3)
        fig.set_dpi(100)
        fig.set_size_inches(6, 6)

        #Setup drawing ax
        self.ax = fig.add_subplot(gs[:2], xlim=(0, 10), ylim=(0,10))
        self.ax.set_aspect('equal', adjustable='box')
        self.title = self.ax.text(0.5, 0.88, "", bbox={'facecolor':'w', 'alpha':0.5, 'pad':5},transform=self.ax.transAxes, ha="center")

        #Setup plot ax
        self.plot_ax = fig.add_subplot(gs[2], xlim=(0, 100), ylim=(0, 30))
        self.line = self.plot_ax.plot([], [], lw=3, label="Estimate")[0]
        self.plot_ax.set_xlabel("Samples")
        self.plot_ax.set_ylabel("Area")
        self.plot_ax.legend()

        self.sample = plt.Circle((5, -5), 0.1, ec='black')

        anim = animation.FuncAnimation(fig, self.animate, 
                               init_func=self.init, 
                               frames=100, 
                               interval=100,
                               blit=True,
                               repeat=False)

        plt.show()

    def area_estimate(self):
        ratio = self.sample_success / self.sample_count
        return ratio * self.total_area

    def update_title(self):
        estimate = f"Area Estimate: {self.area_estimate():.2f}"
        success = f"Success: {self.sample_success}/{self.sample_count}"
        self.title.set_text(f"{estimate}\n{success}")

    def update_sample(self, c_i, p):
        (x,y) = p
        c = self.circles[c_i]
        self.sample.center = (x, y)
        self.sample.set_facecolor(c.color)
        ratio = self.sample_success / self.sample_count

    def update_plot(self):
        x = np.arange(1, self.sample_count+1)
        y = self.estimates
        self.line.set_data(x,y)

    def init(self):
        self.sample.center = (5, 5)
        self.ax.add_patch(self.sample)

        for c in reversed(self.circles):
            circle = plt.Circle((c.x, c.y), c.radius, fc=c.color, alpha=0.85, ec="black")
            self.ax.add_patch(circle)

        return self.sample, self.title, self.line

    def animate(self,i):
        self.sample_count = i+1
        self.estimates.append(self.area_estimate())
        c_i, p = self.sampler.sample()

        if self.sampler.good_sample(c_i, p):
            self.sample_success += 1
        
        self.update_sample(c_i, p)
        self.update_title()
        self.update_plot()
        
        return self.sample, self.title, self.line