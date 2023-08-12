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
    def __init__(self, vertices, fig=None, axs=None,
            color='k', arrows=True, zorder=1):
        self.Nv = vertices.shape[1]

        # Initialize vertices.
        self.vList = vertices

        # Initialize fig and axs members.
        if fig is None:
            self.fig, self.axs = plt.subplots()
        else:
            self.fig = fig
            self.axs = axs

        # Initialize empty fig/axs variables.
        self.color = color
        self.linewidth = 2.0
        self.linestyle = None
        self.grid = 1
        self.zorder = zorder
        self.facecolor= 'none'

    def setLineWidth(self, width):
        self.linewidth = width
        # Return instance of self.
        return self

    def setLineStyle(self, style):
        self.linestyle = style
        # Return instance of self.
        return self

    def setVertices(self, vertices):
        self.vList = vertices
        # Return instance of self.
        return self

    def transform(self, R=None, dx=None):
        # Default terms.
        if R is None:  R = np.eye( 2,2 )
        if dx is None:  dx = 0
        # Update position of vertices.
        self.vList = R@self.vList + dx
        # Return instance of self.
        return self

    def draw(self):
        # Plot polygon.
        self.pathpatch = patches.PathPatch(
            path.Path( self.vList.T ),
            facecolor=self.facecolor, edgecolor=self.color,
            linewidth=self.linewidth, linestyle=self.linestyle,
            zorder=self.zorder )
        self.axs.add_patch( self.pathpatch )

        # Return instance of self.
        return self

    def update(self, vertices=None, R=None, dx=None):
        # Transform if necessary.
        if vertices is not None:
            self.setVertices( vertices )
        if R is not None or dx is not None:
            self.transform( R, dx )

        # Replot the new polygon.
        self.pathpatch.remove()
        self.draw()

        # Return instance of self.
        return self
