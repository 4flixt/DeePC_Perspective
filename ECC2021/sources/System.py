import numpy as np

class System:
    """
    Helper class to simulate linear discrete time dynamical systems in state-space form.
    Initiate with system matrices: A,B,C,D such that:

    x_next = A@x + B@u
    y      = C@x + D@u

    Passing D is optional.
    Passing x0 is optional (will results to all zero per default).

    Run a simulation step with make_step method.

    Reset with reset method.

    Query stored results with methods u, y, x.
    """
    def __init__(self,A,B,C,D=None, x0=None, dt=1):
        self.A = A
        self.B = B
        self.C = C

        self.n_x = A.shape[0]
        self.n_u = B.shape[1]
        self.n_y = C.shape[0]

        if D is None:
            D = np.zeros((self.n_y, self.n_u))

        self.D = D

        if x0 is None:
            x0 = np.zeros((self.n_x,1))

        self.x0 = x0
        self._x = []
        self._u = []
        self._y = []

        self.dt = dt
        self.t_now = 0
        self._time = []


    def make_step(self,u):
        """
        Run a simulation step by passing the current input.
        Returns the current measurement y.
        """

        self._x.append(self.x0)
        self._u.append(u)
        y = self.C@self.x0+self.D@u
        self._y.append(y)
        self._time.append(self.t_now)

        self.x0 = self.A@self.x0 + self.B@u

        self.t_now += self.dt

        return y

    def reset(self, x0=None):
        if x0 is not None:
            self.x0 = x0
        else:
            self.x0 = np.zeros((8,1))

        self._x = []
        self._u = []
        self._y = []
        self._time = []
        self.t_now = 0

    @property
    def x(self):
        return np.concatenate(self._x,axis=1).T

    @x.setter
    def x(self, *args):
        raise Exception('Cannot set x directly.')

    @property
    def u(self):
        return np.concatenate(self._u,axis=1).T

    @u.setter
    def u(self, *args):
        raise Exception('Cannot set u directly.')

    @property
    def y(self):
        return np.concatenate(self._y,axis=1).T

    @y.setter
    def y(self, *args):
        raise Exception('Cannot set y directly.')

    @property
    def time(self):
        return np.array(self._time)

    @time.setter
    def time(self, *args):
        raise Exception('Cannot set time directly.')


def random_u(u0, switch_prob=0.5, max_amp=np.pi):
    # Hold the current value with 80% chance or switch to new random value.
    u_next = (0.5-np.random.rand(u0.shape[0],1))*max_amp # New candidate value.
    switch = np.random.rand() >= (1-switch_prob) # switching? 0 or 1.
    u0 = (1-switch)*u0 + switch*u_next # Old or new value.
    return u0
