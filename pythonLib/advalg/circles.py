from advalg.circle import Circle
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.widgets import Button

import numpy as np

class CircleAnimation:
    def __init__(self, circles, sampler):
        self.total_samples = 2000
        self.circles = circles
        self.sampler = sampler(circles)
        self.sample_success = 0
        self.sample_count = 0
        self.estimates = []
        self.total_area = sum([c.area() for c in circles])

        self.fig = plt.figure(constrained_layout = True)
        self.gs = self.fig.add_gridspec(3)
        self.fig.set_dpi(100)
        self.fig.set_size_inches(7, 7)

        self.ax, self.title = self.setup_ax()

        self.plot_ax = self.setup_plot_ax()

        self.sample = plt.Circle((5, -5), 0.1, ec='black')

        self.draw_circles()

        area = self.actual_area()
        self.plot_ax.plot(np.arange(1, self.total_samples+1), np.ones(self.total_samples) * area, lw=3, label="Actual")
        self.line = self.plot_ax.plot([], [], lw=3, label="Estimate")[0]
        self.plot_ax.legend()
        self.plot_ax.set_ylim(0, 2*area)

        self.anim = animation.FuncAnimation(self.fig, self.animate, 
                               init_func=self.init, 
                               frames=self.total_samples, 
                               interval=10,
                               blit=True,
                               repeat=False)
        plt.show()

    def setup_ax(self):
        ax = self.fig.add_subplot(self.gs[:2], xlim=(0, 100), ylim=(0,100))
        ax.set_aspect('equal', adjustable='box')
        title = ax.text(0.5, 0.88, "", bbox={'facecolor':'w', 'alpha':0.5, 'pad':5},transform=ax.transAxes, ha="center")
        return ax, title

    def setup_plot_ax(self):
        plot_ax = self.fig.add_subplot(self.gs[2], xlim=(0, self.total_samples))
        plot_ax.set_xlabel("Samples")
        plot_ax.set_ylabel("Area")
        return plot_ax

    def actual_area(self):
        area = 0
        for x in np.linspace(0,100,100):
            for y in np.linspace(0,100,100):
                if self.in_circle(x,y):
                    area += 1
        return area

    def in_circle(self, x, y):
        for c in self.circles:
            if c.inside(x,y):
                return True
        return False

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

    def update_plot(self):
        x = np.arange(1, self.sample_count+1)
        y = self.estimates
        self.line.set_data(x,y)

    def draw_circles(self):
        self.ax.patches = []
        for c in reversed(self.circles):
            circle = plt.Circle((c.x, c.y), c.radius, fc=c.color, alpha=0.85, ec="black")
            self.ax.add_patch(circle)
        self.fig.canvas.draw()

    def init(self):
        self.sample.center = (5, 5)
        self.ax.add_patch(self.sample)

        return self.sample, self.title, self.line

    def animate(self,i):
        self.sample_count = i+1
        c_i, p = self.sampler.sample()

        if self.sampler.good_sample(c_i, p):
            self.sample_success += 1

        self.estimates.append(self.area_estimate())
        
        self.update_sample(c_i, p)
        self.update_title()
        self.update_plot()
        
        return self.sample, self.title, self.line