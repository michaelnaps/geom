import numpy as np

from GEOM.Circle import *
from GEOM.Vectors import *

# Class: Vehicle2D
# Assumptions: Model is discrete.
class Vehicle2D:
    def __init__(self, x0, radius=0.5,
            fig=None, axs=None, zorder=10,
            color='yellowgreen',
            draw_tail=1, tail_length=100,
            grid=1, pause=1e-3):
        # Initialize fig and axs members.
        if fig is None:
            self.fig, self.axs = plt.subplots()
        else:
            self.fig = fig
            self.axs = axs

        # figure scaling, grid, equal axes
        self.axs.grid( grid )

        # Vehicle body.
        self.body = Circle( x0, radius,
            fig=self.fig, axs=self.axs, zorder=zorder+1,
            color=color )

        # Vehicle tail.
        self.draw_tail = draw_tail
        self.Nt = tail_length
        tail0 = np.kron( x0 ,np.ones( (1, self.Nt) ) )
        self.tail = Vectors( tail0,
            fig=self.fig, axs=self.axs, zorder=zorder,
            color=color )
        self.tail.setLineWidth( 2 )
        self.tail.setLineStyle( None )

        # Forward tail variables (optional).
        self.forward_tail_color = None
        self.forward_tail_patch = None

        # simulation pause
        self.pause = pause

    def initForwardTail(self, xList, zorder=10, color='orange'):
        # Initialize forward tail.
        self.forward_tail_zorder = zorder
        self.forward_tail_color = color
        self.drawForwardTail( xList )

        # Return instance of self.
        return self

    def updateVehicle(self, x):
        # Update vehicle location.
        self.body.update( center=x, radius=None )
        # Return instance of self.
        return self

    def updateTail(self, x):
        # Set new tail vertices.
        tail = self.tail.vList
        tail[:,:-1] = tail[:,1:]
        tail[:,-1] = x[:,0]

        # Update vector list.
        self.tail.setVertices( tail )

        # Return instance of self.
        return self

    def updateForwardTail(self, xList):
        # Re-initialize forward tail.
        self.forward_tail_patch.remove()
        self.drawForwardTail( xList )

        # Return instance of self.
        return self

    def update(self, x):
        # Update body and tail values appropriately.
        self.updateVehicle( x )
        if self.draw_tail:
            self.updateTail( x )

        # Return instance of self.
        return self

    def drawVehicle(self):
        # create vehicle circle
        self.body.draw()

        # Return instance of self.
        return self

    def drawTail(self):
        # create vehicle tail object
        self.tail.draw()

        # Return instance of self.
        return self

    def drawForwardTail(self, xList):
        # Initialize tail variables
        self.forward_tail_patch = patches.PathPatch( path.Path( xList.T ),
            color=self.forward_tail_color, linewidth=self.tail.linewidth, linestyle=self.tail.linestyle,
            fill=0, zorder=self.forward_tail_zorder )

        # Add patch.
        self.axs.add_patch( self.forward_tail_patch )

        # Return instance of self.
        return self

    def draw(self, pause=0):
        # Draw vehicle and tail appropriately.
        self.drawVehicle()
        if self.draw_tail:
            self.drawTail()

        # Pause if necessary.
        if pause:
            plt.pause( self.pause )

        # Return instance of self.
        return self

    def setLimits(self, xlim=None, ylim=None):
        if xlim is not None:
            self.axs.set_xlim( xlim[0], xlim[1] )
        if ylim is not None:
            self.axs.set_ylim( ylim[0], ylim[1] )
        # Return instance of self.
        return self

    def setFigureDimensions(self, w=None, h=None):
        if w is not None:
            self.fig.set_figwidth( w )
        if h is not None:
            self.fig.set_figheight( h )
        # Return instance of self.
        return self

class Swarm2D( Vehicle2D ):
    def __init__(self, X0, radius=0.5,
            fig=None, axs=None, zorder=10,
            color='yellowgreen',
            draw_tail=1, tail_length=100,
            grid=1, pause=1e-3):
        # Initialize fig and axs members.
        if fig is None:
            self.fig, self.axs = plt.subplots()
        else:
            self.fig = fig
            self.axs = axs

        # Initialize vehicle list.
        self.vhcList = [
            Vehicle2D( x0[:,None], radius=radius,
                fig=self.fig, axs=self.axs, zorder=zorder+i,
                color=color, draw_tail=draw_tail,
                grid=1, pause=1e-3 )
            for i, x0 in enumerate( X0.T )
        ]
        self.pause = pause

    def update(self, X):
        # Update individual vhc terms.
        for x, vhc in zip( X.T, self.vhcList ):
            vhc.update( x[:,None] )

        # Return instance of self.
        return self

    def draw(self):
        # Update individual vhc terms.
        for vhc in self.vhcList:
            vhc.draw()