import numpy as np
import matplotlib.pyplot as plt

class Circle:
    def __init__(self, center, radius,
            color='#9C9C9C'):
        self.x = center
        self.r = radius

        # Plotting parameters.
        self.fig = None
        self.axs = None
        self.spherepatch = None
        self.color = color
        self.linewidth = 2.0
        self.grid = True

    def setLineWidth(self, width):
        self.linewidth = width

    def distance(self, pt):
        # Check if circle is filled/empty.
        if self.r < 0:
            sign = -1
        else:
            sign =  1

        # Get distance from center.
        d = np.linalg.norm( pt - self.x )

        # Return distance from edge of circle.
        return sign*d - self.r

    def transform(self, center=None, radius=None):
        # Update position of sphere.
        if center is not None:
            self.x = center
        if radius is not None:
            self.r = radius
        # Return instance of self.
        return self

    def update(self, center=None, radius=None):
        # Transform if necessary.
        self.transform( center, radius )

        # Remove sphere patch from drawing and replot.
        self.circlepatch.remove()
        self.draw()

        # Return instance of self.
        return self

    def draw(self, fig=None, axs=None):
        if fig is not None:
            self.fig = fig
            self.axs = axs
        if self.fig is None or self.axs is None:
            self.fig, self.axs = plt.subplots()

        if self.r < 0:
            edge = self.color
            face = 'none'
        else:
            edge = 'k'
            face = self.color

        self.circlepatch = plt.Circle( self.x[:,0], self.r,
            facecolor=face, edgecolor=edge,
            linewidth=self.linewidth )
        self.axs.add_patch( self.circlepatch )

        # Return instance of self.
        return self
