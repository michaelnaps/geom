import numpy as np
import matplotlib.pyplot as plt

# personal classes
import Geometry.Circle as circ
import Geometry.Polygon as poly

if __name__ == '__main__':
    # test sphere module
    center = np.array( [[0],[1]] );
    radius = -1.0;
    color = 'indianred';

    cvar = circ.Circle( center, radius, color );
    cvar.plot();

    # test polygon module
    vList = np.array( [
        [-1, 1, 2, -1.5],
        [1, 1, -1, -1.5]
    ] );
    color = 'yellowgreen';

    pvar = poly.Polygon( vList, color );

    pvar.plot( cvar.fig, cvar.axs );
    plt.show();