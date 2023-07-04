import numpy as np
import matplotlib.pyplot as plt

def areaRect(Rectangle):
    l = max( Rectangle.vList[0] ) - min( Rectangle.vList[0] );
    w = max( Rectangle.vList[1] ) - min( Rectangle.vList[1] );
    return l*w;

class Polygon:
    def __init__(self, vertices, color='9C9C9C'):
        self.Nv = vertices.shape[1];

        # Initialize vertices.
        # Append first vertex to end for plotting.
        self.vList = np.empty( (2, self.Nv+1) );
        self.vList[:,:self.Nv] = vertices;
        self.vList[:,-1] = vertices[:,0];

        # Initialize empty fig/axs variables.
        self.color = color;
        self.fig = None;
        self.axs = None;

    def plot(self, fig=None, axs=None,
             grid=True):
        if fig is not None:
            self.fig = fig;
            self.axs = axs;
        if self.fig is None or self.axs is None:
            self.fig, self.axs = plt.subplots();

        # Plot polygon.
        self.axs.plot( self.vList[0], self.vList[1] );

        # Axis parameters.
        self.axs.grid( grid );
        self.axs.axis( 'equal' );

        # Return instance of self.
        return self;