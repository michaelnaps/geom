import numpy as np
import matplotlib.pyplot as plt
import matplotlib.path as path
import matplotlib.patches as patches

def areaRect(Rectangle):
    l = max( Rectangle.vList[0] ) - min( Rectangle.vList[0] );
    w = max( Rectangle.vList[1] ) - min( Rectangle.vList[1] );
    return l*w;

def rotZ(theta):
    R = np.array( [
        [np.cos( theta ), -np.sin( theta )],
        [np.sin( theta ),  np.cos( theta )]
    ] );
    return R;

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
        self.linewidth = 2.0;
        self.grid = True;

    def setLineWidth(self, width):
        self.linewidth = width;

    def transform(self, R=None, dx=None):
        if R is None:
            R = np.eye( 2,2 );
        if dx is None:
            dx = np.zeros( (2,1) );

        self.vList = R@self.vList + dx;

        # Replot the new polygon.
        self.pathpatch.remove();
        self.plot( fig=self.fig, axs=self.axs );

        # Return instance of self.
        return self;

    def plot(self, fig=None, axs=None):
        if fig is not None:
            self.fig = fig;
            self.axs = axs;
        if self.fig is None or self.axs is None:
            self.fig, self.axs = plt.subplots();

        # Plot polygon.
        self.pathpatch = patches.PathPatch(
            path.Path( self.vList.T ),
            facecolor='none', edgecolor=self.color,
            linewidth=self.linewidth );
        self.axs.add_patch( self.pathpatch );

        # Axis parameters.
        self.axs.grid( self.grid );
        self.axs.axis( 'equal' );

        # Return instance of self.
        return self;