import numpy as np

import matplotlib.pyplot as plt
import matplotlib.path as path
import matplotlib.patches as patches

def rotZ(theta):
    R = np.array( [
        [np.cos( theta ), -np.sin( theta )],
        [np.sin( theta ),  np.cos( theta )]
    ] )
    return R

class Vectors:
    def __init__(self, vertices, color='k', arrows=True):
        self.Nv = vertices.shape[1]

        # Initialize vertices.
        self.vList = vertices

        # Initialize empty fig/axs variables.
        self.color = color
        self.fig = None
        self.axs = None
        self.linewidth = 2.0
        self.grid = True

    def setLineWidth(self, width):
        self.linewidth = width

    def transform(self, R=np.eye( 2, 2 ), dx=np.zeros( (2, 1) )):

        # Update position of vertices.
        self.vList = R@self.vList + dx

    def draw(self, R=None, dx=None):
        # Transform if necessary.
        if R is not None or dx is not None:
            self.transform( R, dx )

        # Replot the new polygon.
        self.pathpatch.remove()
        self.plot( fig=self.fig, axs=self.axs )

        # Return instance of self.
        return self

    def plot(self, fig=None, axs=None):
        if fig is not None:
            self.fig = fig
            self.axs = axs
        if self.fig is None or self.axs is None:
            self.fig, self.axs = plt.subplots()

        # Plot polygon.
        self.pathpatch = patches.PathPatch(
            path.Path( self.vList.T ),
            facecolor='none', edgecolor=self.color,
            linewidth=self.linewidth )
        self.axs.add_patch( self.pathpatch )

        # Axis parameters.
        self.axs.grid( self.grid )
        self.axs.axis( 'equal' )

        # Return instance of self.
        return self
