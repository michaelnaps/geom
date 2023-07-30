import numpy as np
import matplotlib.pyplot as plt
import time
# personal classes
from GEOM.Circle import *
from GEOM.Polygon import *
from GEOM.Vectors import *
from GEOM.Vehicle2D import *

def model(x, dt=0.01):
    A = np.array( [[0, -1],[1, 0]] )
    dx = A@x
    return x + dt*dx

if __name__ == '__main__':
    # test sphere module
    center = np.array( [[0],[1]] )
    radius = -1.0
    ccolor = 'indianred'
    pcolor = 'cornflowerblue'

    # test polygon module
    vList = np.array( [
        [-2, 2, 2, -2],
        [1, 1, -1, -1]
    ] )

    # Initialize shape variables.
    fig, axs = plt.subplots()
    axs.set_ylim( (-5, 5) )
    axs.axis( 'equal' )
    cvar = Circle( center, radius,
        fig=fig, axs=axs, color=ccolor )
    pvar = Polygon( vList,
        fig=fig, axs=axs, color=pcolor )
    vvar = Vectors( vList,
        fig=fig, axs=axs )

    # Plot shapes.
    cvar.draw()
    pvar.draw()
    vvar.draw()
    plt.show( block=0 )
    plt.pause(1)

    # Test replot function.
    cvar.transform( np.zeros( (2,1) ) )
    pvar.transform( R=rotZ( np.pi/4 ), dx=np.array( [[1],[1]] ) )
    cvar.update()
    pvar.update()

    # Test Vehicle class.
    x0 = np.array( [[1], [0]] )

    vhccolor = 'purple'
    vhc = Vehicle2D( x0, fig=fig, axs=axs, color=vhccolor )
    plt.pause(5)

    # # Test swarm.
    # X0 = np.random.rand( 2, 3 )
    # swarm = Swarm( X0 )