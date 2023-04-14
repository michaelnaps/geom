import numpy as np
import matplotlib.pyplot

class Grid:
    """
    A function to store the coordinates of points on a 2-D grid and evaluate
    arbitrary functions on those points.
    """
    def __init__(self, xx_ticks, yy_ticks):
        """
        Stores the input arguments in attributes.
        """
        self.xx_ticks = xx_ticks
        self.yy_ticks = yy_ticks

    def eval(self, fun):
        """
        This function evaluates the function  fun (which should be a function)
        on each point defined by the grid.
        """

        dim_domain = [numel(self.xx_ticks), numel(self.yy_ticks)]
        dim_range = [numel(fun(np.array([[0], [0]])))]
        fun_eval = np.nan * np.ones(dim_domain + dim_range)
        for idx_x in range(0, dim_domain[0]):
            for idx_y in range(0, dim_domain[1]):
                x_eval = np.array([[self.xx_ticks[idx_x]],
                                   [self.yy_ticks[idx_y]]])
                fun_eval[idx_x, idx_y, :] = np.reshape(fun(x_eval),
                                                       [1, 1, dim_range[0]])

        # If the last dimension is a singleton, remove it
        if dim_range == [1]:
            fun_eval = np.reshape(fun_eval, dim_domain)

        return fun_eval

    def mesh(self):
        """
        Shorhand for calling meshgrid on the points of the grid
        """

        return np.meshgrid(self.xx_ticks, self.yy_ticks)

    def plot_threshold(self, f_handle, threshold=10,
        xrange=[-10,10], yrange=[-10,10]):
        """
        The function evaluates the function f_handle on points placed on the grid.
        """
        def f_handle_clip(val):
            return clip(f_handle(val), threshold)

        f_eval = self.eval(f_handle_clip)
        # print(f_eval)

        [xx_mesh, yy_mesh] = self.mesh()
        f_dim = numel(f_handle_clip(np.zeros((2, 1))))
        if f_dim == 1:
            # scalar field
            fig = plt.gcf()
            axis = fig.add_subplot(111, projection='3d')

            axis.plot_surface(xx_mesh,
                              yy_mesh,
                              f_eval.transpose(),
                              cmap=cm.gnuplot2)
            axis.set_zlim(0, threshold)
        elif f_dim == 2:
            # vector field
            # grid.eval gives the result transposed with respect to
            # what meshgrid expects
            f_eval = f_eval.transpose((1, 0, 2))

            # print(f_eval)
            # vector field
            plt.quiver(xx_mesh,
                       yy_mesh,
                       f_eval[:, :, 0],
                       f_eval[:, :, 1],
                       angles='xy',
                       scale_units='xy')
            axis = plt.gca()
        else:
            raise NotImplementedError(
                'Field plotting for dimension greater than two not implemented'
            )

        axis.set_xlim(xrange[0], xrange[1])
        axis.set_ylim(yrange[0], yrange[1])
        plt.xlabel('x')
        plt.ylabel('y')
