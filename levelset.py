import numpy as np
import matplotlib.pyplot as plt
from GEOM.LevelSet import *

if __name__ == '__main__':
    F = lambda x: (x.T@x).reshape(1,)[0]
    lset = LevelSet( F, 10, 0.1, [-5,5], [-5,5] ).draw()

    lset.axs.axis( 'equal' )
    lset.axs.axis( [-5, 5, -5, 5] )
    plt.show( block=0 )
    input( 'Press ENTER to exit program...' )