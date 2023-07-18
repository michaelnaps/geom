import numpy as np
from Sphere import *

class Robot:
    def __init__(self, sphere, role, color, name):
        self.x = sphere.center
        self.r = sphere.radius
        self.tag_r = sphere.distance_influence
        self.role = role
        self.color = color
        self.name = name

    @property
    def sphere(self):
        return Sphere(self.x, self.r, self.tag_r)

    def plot(self, dinf_color='k'):
        self.sphere.plot(color=self.color, dinf_color=dinf_color)

    def move(self, dt=0.001, u=None):
        m = 1
        if u is None:
            u = np.array([[0],[0]])
        self.x = self.x + dt*u

    def distance(self, points):
        return self.sphere.distance(points)

    def distance_grad(self, points):
        return self.sphere.distance_grad(points)

    def control(self, dt, walls, robots, wgain=1, pgain=1):
        q = walls[0].distance(self.x)
        P = wgain*walls[0].distance_grad(self.x)

        if q.ndim == 1:
            q.shape = (q.shape[0], 1)

        for wall in walls[1:]:
            q = np.concatenate((q, [wall.distance(self.x)]), axis=1)
            P = np.concatenate((P, wgain*wall.distance_grad(self.x)), axis=1)

        if self.role == 'evader':
            for robot in robots:
                if not robot.name == self.name:
                    if robot.role == 'evader':
                        robot_dist = robot.distance(self.x)
                        robot_grad = robot.distance_grad(self.x)

                        if robot_dist.ndim == 1:
                            robot_dist.shape = (1,1)

                        q = np.concatenate((q, robot_dist), axis=1)
                        P = np.concatenate((P, robot_grad), axis=1)

                    elif robot.role == 'pursuer' or robot.role == 'paused':
                        u_ref = -pgain*robot.distance_grad(self.x)

        elif self.role == 'pursuer':
            i_min = -1
            d_min = np.inf

            for i, robot in enumerate(robots):
                if not robot.name == self.name:
                    d_current = robot.distance(self.x)[0]
                    if d_current < d_min:
                        i_min = i
                        d_min = d_current

            print('minimum robot:', robots[i_min].name)
            u_ref = robots[i_min].distance_grad(self.x)

        elif self.role == 'paused':
            u_ref = np.array([[0],[0]])

        u = qp_supervisor(-P.T, -q.T, u_ref=u_ref)
        self.move(dt=dt, u=u)

    def impact(self, evader):
        dist = self.distance(evader.x)
        dist -= evader.r
        if dist < self.tag_r:
            return True
        return False
