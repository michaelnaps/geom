import numpy as np
import matplotlib.pyplot as plt
import time
# personal classes
from GEOM.Circle import *
from GEOM.Polygon import *
from GEOM.Vectors import *

if __name__ == '__main__':
    # test sphere module
    center = np.array( [[0],[1]] )
    radius = -1.0
    ccolor = 'indianred'

    # test polygon module
    vList = np.array( [
        [-2, 2, 2, -2],
        [1, 1, -1, -1]
    ] )
    pcolor = 'k'

    # Initialize shape variables.
    cvar = Circle( center, radius, ccolor )
    pvar = Polygon( vList, pcolor )
    vvar = Vectors( vList )

    # Plot shapes.
    fig, axs = plt.subplots()
    cvar.plot( fig, axs )
    pvar.plot( fig, axs )
    vvar.plot( fig, axs )
    plt.show( block=0 )
    plt.pause(1)

    # Test replot function.
    pvar.transform( R=rotZ( np.pi/2 ), dx=np.array( [[1],[1]] ) )
    cvar.transform( np.zeros( (2,1) ) )
    cvar.draw()
    pvar.draw()
    plt.pause(10)