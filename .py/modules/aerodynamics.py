import math

class Aerodynamics:
    def __init__(self, wing, physics):
        self.wing = wing
        self.physics = physics

        self.air_density = physics["air"]["air_density_kgm3"]
        self.dynamic_viscosity = physics["air"]["dynamic_viscosity_pas"]
        self.velocity = physics["air"]["velocity_ms"]

        self.oswald_efficiency = physics["model"]["oswald_efficiency"]
        self.stall_angle = physics["model"]["stall_angle_deg"]

    def reynolds_number(self, chord):
        return (self.air_density * self.velocity
                * chord / self.dynamic_viscosity)

    def cl(self, alpha):
        return 2 * math.pi * math.radians(alpha)

    def cf(self): # Flow assumed to be laminar (Re < 5 x 10^5)
        return 1.328 / math.sqrt(self.reynolds_number(self.wing.mean_chord))

    def cd0(self):
        return 0.02 # temporary simple assumption

    def cdi(self, alpha):
        return (self.cl(alpha) ** 2 / (math.pi
                * self.wing.ar * self.oswald_efficiency))

    def cd(self, alpha):
        return self.cd0() + self.cdi(alpha)

    def lift(self, alpha):
        return (0.5 * self.air_density * self.velocity
                ** 2 * self.wing.area * self.cl(alpha))

    def drag(self, alpha):
        return (0.5 * self.air_density * self.velocity
                ** 2 * self.wing.area * self.cd(alpha))