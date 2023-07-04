import numpy as np
import matplotlib.pyplot as plt

class Circle:
    def __init__(self, center, radius,
            color='#9C9C9C'):
        self.x = center;
        self.r = radius;

        # Plotting parameters.
        self.fig = None;
        self.axs = None;
        self.color = color;
        self.linewidth = 2.0;

    def setLineWidth(self, width):
        self.linewidth = width;

    def distance(self, pt):
        if self.r < 0:
            sign = -1;
        else:
            sign =  1;

        d = np.linalg.norm( pt - self.x )

        # Return distance from point.
        return sign*d - self.r;

    def plot(self, fig=None, axs=None,
            grid=True):
        if fig is not None:
            self.fig = fig;
            self.axs = axs;
        if self.fig is None or self.axs is None:
            self.fig, self.axs = plt.subplots();

        if self.r < 0:
            edge = self.color;
            face = 'none';
        else:
            edge = 'none';
            face = self.color;

        spherepatch = plt.Circle( self.x[:,0], self.r,
            facecolor=face, edgecolor=edge,
            linewidth=self.linewidth );
        self.axs.add_patch( spherepatch );

        self.axs.grid( grid );
        self.axs.axis( 'equal' );

        # Return instance of self.
        return self;
