# Velocity Verlet Integrator as a Functor containing the integrator specs


class VelocityVerlet:
    # Initializes Integrator with time step & force field
    def __init__(self, dt, force_field):
        self.dt = dt
        self.force_field = force_field

    def __call__(self, x, v, m, *args, **kwargs):
        a_1 = self.force_field(x)
        x = x + v * self.dt + 0.5 * a_1 * self.dt**2
        a_2 = self.force_field(x)
        v = v + 0.5 * (a_1 + a_2) * self.dt
        return x, v