import sys
from os.path import expanduser
sys.path.insert( 0, expanduser('~')+'/prog/four' )

import numpy as np
from GEOM.Polygon import *
from FOUR.Transforms import *

def dist(x, y):
    return ((x - y).T@(x - y))[0][0]

def orderByDist(X, i0=0):
    # Initialize x-instance and ordered set variables.
    xnext = X[:,i0,None]
    Xordr = np.copy( xnext )

    # Copy X to reference variable, excluding xnext.
    Xref = np.delete( X, obj=i0, axis=1 )
    while Xref.shape[1] > 0:  # While Xref is non-empty.
        # Create list of distances from most recent point.
        dList = [dist( xnext, xref[:,None] ) for xref in Xref.T]

        # Isolate minimum index.
        inext = dList.index( min( dList ) )

        # Replacemore recent with minimum and add to set.
        xnext = Xref[:,inext,None]
        Xordr = np.hstack( (Xordr, xnext) )

        # Delete saved point from reference.
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
        self.a = a  # Grid density.
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

        # Create polygons out of level set points.
        self.iterations = {}
        self.transforms = {}
        self.smooth = {}
        for h in self.hList:
            # Order the level set by distance between points.
            if self.levels[h].shape[1] != 1:
                self.levels[h] = orderByDist( self.levels[h] )
                self.levels[h] = np.hstack( (self.levels[h], self.levels[h][:,0,None]) )
                self.iterations[h] = np.array( [[i for i in range( self.levels[h].shape[1] )]] )
                self.transforms[h] = RealFourier( self.iterations[h], self.levels[h], N=100 ).dmd()
                smoothIter = np.array( [[0.1*i for i in range( 10*self.levels[h].shape[1] )]] )
                self.smooth[h] = self.transforms[h].solve( smoothIter )
        self.levelPlots = [ Polygon( self.smooth[h], fig=self.fig, axs=self.axs,
            color=color, zorder=zorder ) for h in self.hList if self.levels[h].shape[1] != 1 ]

    def checkVal(self, x):
        h = self.F( x )/self.e
        hint = round( h )
        return hint if abs( h - hint ) < self.tol else None

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
        for level in self.levelPlots:
            level.draw()
        # Return instance of self.
        return self
