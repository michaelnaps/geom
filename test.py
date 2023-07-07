import numpy as np
import matplotlib.pyplot as plt
import time
# personal classes
import Geometry.Circle as circ
import Geometry.Polygon as poly

if __name__ == '__main__':
    # test sphere module
    center = np.array( [[0],[1]] );
    radius = -1.0;
    ccolor = 'indianred';

    # test polygon module
    vList = np.array( [
        [-1, 1, 2, -1.5],
        [1, 1, -1, -1.5]
    ] );
    pcolor = 'yellowgreen';

    # Initialize shape variables.
    cvar = circ.Circle( center, radius, ccolor );
    pvar = poly.Polygon( vList, pcolor );

    # Plot shapes.
    fig, axs = plt.subplots();
    cvar.plot( fig, axs );
    pvar.plot( fig, axs );
    plt.show(block=0);
    plt.pause(1);

    # Test replot function.
    cvar.transform( np.array( [[0],[0]] ) );
    plt.pause(10);