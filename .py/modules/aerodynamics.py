import math

class Aerodynamics:
    def __init__(self, wing, physics):
        self.wing = wing
        self.physics = physics

        self.air_density = physics["air"]["air_density_kgm3"]
        self.dynamic_viscosity = physics["air"]["dynamic_viscosity_pas"]
        self.velocity = physics["air"]["velocity_ms"]

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

    def cl_2d(self,alpha):
        return 2 * math.pi * math.radians(alpha)

    def cl_high_ar(self, alpha):
        cl_2d = self.cl_2d(alpha)
        return cl_2d / (1 + cl_2d /
                        (math.pi * self.wing.ar * self.wing.oswald_efficiency))

    def cl_low_ar(self, alpha):
        cl_2d = self.cl_2d(alpha)
        return (cl_2d / (math.sqrt(1 +
                (cl_2d / (math.pi * self.wing.ar) ** 2))
                + (cl_2d / (math.pi * self.wing.ar))))

    def cl(self, alpha):
        if self.wing.ar >= 4:
            result = self.cl_high_ar(alpha)
        else:
            result = self.cl_low_ar(alpha)

        if alpha > self.wing.stall_angle - 5: # Stall model
            return result - (((alpha -
                    self.wing.stall_angle + 5) ** 2) / 100)
        else:
            return result

    def cf(self): # Flow assumed to be laminar (Re < 5 x 10^5)
        return 1.328 / math.sqrt(self.reynolds_number(self.wing.mean_chord))

    def cd0(self):
        return 0.02 # temporary simple assumption

    def cdi(self, alpha):
        return (self.cl(alpha) ** 2 / (math.pi
                * self.wing.ar * self.wing.oswald_efficiency))

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