import numpy as np
from GEOM.Polygon import *

def orderByDistance(X, i0=0):
    xnext = X[:,i0,None]
    Xordr = np.copy( xnext )
    Xref = np.delete( X, obj=i0, axis=1 )
    while Xref.shape[1] > 0:
        dList = [((xnext - xref[:,None].T)@(xnext - xref[:,None]))[0][0] for xref in Xref.T]
        inext = dList.index( min( dList ) )
        xnext = Xref[:,inext,None]
        Xordr = np.hstack( (Xordr, xnext) )
        Xref = np.delete( Xref, obj=inext, axis=1 )
    return Xordr

class LevelSet:
    def __init__(self, F, e, a, xBounds, yBounds,
        tol=1e-12, fig=None, axs=None, color='k', zorder=1):
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
        x1List = a*np.array( [i for i in range( self.n )] ) + x0
        x2List = a*np.array( [i for i in range( self.m )] ) + y0
        self.grid = []
        for x1 in x1List:
            for x2 in x2List:
                self.grid = self.grid + [np.array( [[x1],[x2]] )]

        # Evaluate points in mesh for level sets.
        self.hList = []
        self.levels = {}
        for x in self.grid:
            h = self.checkVal( x )
            self.includeVal( x, h )
            if h is not None and h not in self.hList:
                self.hList = self.hList + [h]

        # Create polygons out of levels curves.
        for h in self.hList:
            self.levels[h] = orderByDistance( self.levels[h] )
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
