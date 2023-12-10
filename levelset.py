import numpy as np
import matplotlib.pyplot as plt
from GEOM.LevelSet import *

if __name__ == '__main__':
    bound = 10
    F = lambda x: (x.T@x)[0][0]
    lset = LevelSet( F, 5, 0.05, [-bound,bound], [-bound,bound], tol=1e-22 ).draw()
    lset.axs.axis( 'equal' )
    lset.axs.axis( [-5, 5, -5, 5] )
    plt.show( block=0 )
    input( 'Press ENTER to exit program...' )