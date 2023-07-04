import numpy as np
import matplotlib.pyplot as plt

class Circle:
    def __init__(self, center, radius, color='#9C9C9C'):
        self.x = center;
        self.r = radius;
        self.color = color;
        self.linewidth = 2.0;
        return;

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
             lims=None, grid=True):
        if fig is None or axs is None:
            fig, axs = plt.subplots();

        if self.r < 0:
            edge = self.color;
            face = 'none';
        else:
            edge = 'none';
            face = self.color;

        spherepatch = plt.Circle( self.x[:,0], self.r,
            facecolor=face, edgecolor=edge,
            linewidth=self.linewidth );
        axs.add_patch( spherepatch );

        axs.grid( grid );
        axs.axis( 'equal' );

        # Return instance of self.
        return self;
