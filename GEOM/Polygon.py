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