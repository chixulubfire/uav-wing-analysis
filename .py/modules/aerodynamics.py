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

        self.n = (
            self.physics)["numerics"]["airfoil_points"]
        self.a_min = (
            self.physics)["numerics"]["alpha_min_deg"]
        self.a_max = (
            self.physics)["numerics"]["alpha_max_deg"]
        self.a_step = (
            self.physics)["numerics"]["alpha_step"]
        self.convergence\
            = self.physics["numerics"]["convergence_tolerance"]

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

    def ld(self,alpha):
        return self.lift(alpha) / self.drag(alpha)

    def alpha_sweep(self):
        alphas = []
        cls = []
        cds = []
        lds = []

        alpha = self.a_min
        while alpha <= self.a_max:
            cl = self.cl(alpha)
            cd = self.cd(alpha)
            ld = cl / cd if cd > 0 else 0

            alphas.append(alpha)
            cls.append(cl)
            cds.append(cd)
            lds.append(ld)

            alpha += self.a_step

        return {
            "alpha": alphas,
            "cl": cls,
            "cd": cds,
            "ld": lds
        }