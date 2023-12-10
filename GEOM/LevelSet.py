import numpy as np
from GEOM.Polygon import *

class LevelSet:
    def __init__(self, F, e, a, xBounds, yBounds,
        tol=1e-3, fig=None, axs=None, color='k', zorder=1):
        # Figure variables.
        if fig is None:
            fig, axs = plt.subplots()
        self.fig = fig
        self.axs = axs

        # Define and save dimension parameters.
        self.n = round( (xBounds[1] - xBounds[0])/a ) + 1
        self.m = round( (yBounds[1] - yBounds[0])/a ) + 1

        # Level set parameters.
        self.F = F  # Objective function.
        self.e = e  # Level set differences.
        self.a = a  # Grid differences.
        self.tol = tol  # Region tolerance.

        # Create mesh over x-y plane.
        x0 = xBounds[0]
        y0 = yBounds[0]
        self.xList = a*np.array( [i for i in range( self.n )] ) + x0
        self.yList = a*np.array( [i for i in range( self.m )] ) + y0

        # Evaluate points in mesh for level sets.
        self.hList = []
        self.levels = {}
        for x in self.xList:
            for y in self.yList:
                xy = np.array( [[x],[y]] )
                h = self.checkVal( xy )
                self.includeVal( xy, h )
                if h is not None and h not in self.hList:
                    self.hList = self.hList + [h]

        # Create polygons out of levels curves.
        self.curves = [ Polygon( self.levels[h], fig=self.fig, axs=self.axs,
            color=color, zorder=zorder ) for h in self.hList ]

    def checkVal(self, x):
        h = self.F( x )/self.e
        hint = round( h )
        return hint if h - hint < self.tol else None

    def includeVal(self, x, h):
        if h is None:
            # Return instance of self.
            return self

        # Check if h is in levels dict., add if not.
        if h in self.levels:
            self.levels[h] = np.hstack( (self.levels[h], x) )
        else:
            self.levels[h] = x

        # Return instance of self.
        return self

    def draw(self):
        for curve in self.curves:
            curve.draw()
        # Return instance of self.
        return self
