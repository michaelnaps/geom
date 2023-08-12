import numpy as np
from GEOM.Vectors import *

def areaRect(Rectangle):
    l = max( Rectangle.vList[0] ) - min( Rectangle.vList[0] )
    w = max( Rectangle.vList[1] ) - min( Rectangle.vList[1] )
    return l*w

class Polygon( Vectors ):
    def __init__(self, vertices, fig=None, axs=None, color='k', zorder=1):
        # Add line between final point and first point.
        Nv = vertices.shape[1]
        vList = np.empty( (2, Nv+1) )
        vList[:,:Nv] = vertices
        vList[:,-1] = vertices[:,0]

        # Initialize parent class.
        Vectors.__init__( self, vList,
            fig=fig, axs=axs, color=color,
            zorder=zorder, arrows=False )

    def setColor(self, color):
        self.facecolor = color
        # Return instance of self.
        return self

class Grid:
    def __init__(self, gamma, xBounds, yBounds,
        fig=None, axs=None, color='grey', zorder=1):
        # Dimensions of grid (assume square).
        self.n = round( (xBounds[1] - xBounds[0])/gamma )
        self.m = round( (yBounds[1] - yBounds[0])/gamma )
        self.gamma = gamma

        # Grid zeros points (starts from top-left).
        x0 = xBounds[0]
        y0 = yBounds[1]
        v0 = np.array( [
            [x0, x0+gamma, x0+gamma, x0],
            [y0, y0, y0-gamma, y0-gamma]
        ] )

        # Generate vector list from v0.
        self.gList = [ [None for i in range( self.m )]
            for j in range( self.n ) ]
        for i in range( self.n ):
            for j in range( self.m ):
                self.gList[i][j] = Polygon( v0, fig=fig, axs=axs,
                    color=color, zorder=zorder )
                self.gList[i][j].transform( dx=[[i*gamma],[-j*gamma]] )

    def setCellColor(self, i, j, color):
        self.gList[i][j].facecolor = color
        # Return instance of self.
        return self

    def setLineWidth(self, width):
        for gRow in self.gList:
            for cell in gRow:
                cell.setLineWidth( width )
        # Return instance of self.
        return self

    def setLineStyle(self, style):
        for gRow in self.gList:
            for cell in gRow:
                cell.setLineStyle( style )
        # Return instance of self.
        return self

    def transform(self, R=None, dx=None):
        for gRow in self.gList:
            for cell in gRow:
                cell.transform( R=R, dx=dx )
        # Return instance of self.
        return self

    def draw(self):
        # Draw each cell in grid list
        for gRow in self.gList:
            for cell in gRow:
                cell.draw()
        # Return instance of self.
        return self

    def update(self, R=None, dx=None):
        for gRow in self.gList:
            for cell in gRow:
                cell.update( R=R, dx=dx )
        # Return instance of self.
        return self
