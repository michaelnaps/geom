import numpy as np
from GEOM.Vehicle2D import *


# Hyper parameter(s).
W = 1e12
dt = 1e-3
m1 = 1
m2 = 8


def nModel(X, M, i=0, dt=1e-3):
    n = X.shape[1]
    dX = np.hstack( [X[0][i] - X[0][j] for j in range( n ) if i != j ] )
    dY = np.hstack( [X[1][i] - X[1][j] for j in range( n ) if i != j ] )
    H  = np.hstack( [x**2 + y**2 for x, y in zip( dX, dY )] )

    xacc = np.array( [0] )
    yacc = np.array( [0] )
    for m, dx, dy, h in zip( M[:i]+M[i+1:], dX, dY, H ):
        xacc = xacc + W*m*(dx/np.sqrt( h ))/h
        yacc = yacc + W*m*(dy/np.sqrt( h ))/h

    vel = np.array( [
        [ X[0][i] ],
        [ X[1][i] ],
        -xacc,
        -yacc
    ] )

    return X[:,i,None] + dx*vel

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

    X = np.hstack( (x1, x2) )
    M = [m1, m2]

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
    axs.axis( [-100,100,-100,100] )
    plt.show( block=0 )

    # Simulation
    Nt = np.inf
    t = 0
    while t < Nt:
        X = np.hstack( (x1, x2) )
        x1 = nModel( X, M )
        print( x1[:2].T )
        planet1.update( x1[:2] )
        plt.pause( dt )
        t += 1
