import numpy as np
from GEOM.Vehicle2D import *


# Hyper parameter(s).
W = 1e12
dt = 1e-3
m1 = 1
m2 = 8


def model(X, M, dt=1e-6):
    dx = X[0][0] - X[1][0]
    dy = X[0][1] - X[1][1]
    h = np.sqrt( dx**2 + dy**2 )[0]

    dx1 = np.array( [
        X[0][2],
        X[0][3],
        -M[1]*W*(dx/h)/h**2,
        -M[1]*W*(dy/h)/h**2,
    ] )
    return X[0] + dt*dx1


if __name__ == '__main__':
    # Initial conditions.
    x1 = np.array( [[50],[50],[1e5],[-3e5]] )
    x2 = np.zeros( (4,1) )

    # Plot variables.
    fig, axs = plt.subplots()
    planet1 = Vehicle2D( x1[:2],
        fig=fig, axs=axs,
        radius=m1, color='k',
        zorder=m2, pause=dt ).draw()
    planet2 = Vehicle2D( x2[:2],
        fig=fig, axs=axs,
        radius=m2,
        color='cornflowerblue',
        zorder=m1, pause=dt ).draw()
    axs.axis( 'equal' )
    axs.axis( [-150,150,-100,100] )
    plt.show( block=0 )

    # Simulation
    Nt = np.inf
    t = 0
    while t < Nt:
        x1 = model( [x1,x2], [m1,m2] )
        print( x1[:2].T )
        planet1.update( x1[:2] )
        plt.pause( dt )
        t += 1
