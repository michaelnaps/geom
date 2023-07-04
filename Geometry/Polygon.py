import numpy as np
import matplotlib.pyplot as plt

class Polygon:
    def __init__(self, vertices, color='9C9C9C'):
        self.Nv = vertices.shape[1];

        self.vList = np.empty( (2, self.Nv+1) );
        self.vList[:,:self.Nv] = vertices;
        self.vList[:,-1] = vertices[:,0];

        # initialize empty fig/axs variables
        self.color = color;
        self.fig = None;
        self.axs = None;

    def plot(self, fig=None, axs=None):
        if fig is not None:
            self.fig = fig;
            self.axs = axs;
        if self.fig is None or self.axs is None:
            self.fig, self.axs = plt.subplots();

        # Plot polygon...
        self.axs.plot( self.vList[0], self.vList[1] );

        # Return instance of self.
        return self;