import math
import numpy as np
from scipy.integrate import quad

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

        self.reynolds_number = (self.air_density * self.velocity
                * self.wing.mean_chord / self.dynamic_viscosity)
        self.a0 = 2 * math.pi

        self.planform_correction = 0 # Temporary estimate

        self.lift_curve_slope = (self.a0 /
                    (1 + ((self.a0 *
                    (1 + self.planform_correction)) /
                    (math.pi * self.wing.ar))))

        def zero_lift_angle():
            m = self.wing.airfoil.max_camber
            p = self.wing.airfoil.max_camber_loc
            c = self.wing.mean_chord

            def dz_dx(x):
                if x / c < p:
                    return (2 * m / p ** 2) * (p - x / c)
                else:
                    return (2 * m / (1 - p) ** 2) * (p - x / c)

            def integrand(theta: float) -> float:
                x = 0.5 * c * (1 - np.cos(theta))
                return dz_dx(x) * (np.cos(theta) - 1)

            alpha_l0, _ = quad(integrand, 0, np.pi)

            return alpha_l0 / np.pi  # radians

        self.zero_lift_angle = zero_lift_angle()

    def cl(self, alpha):
        result = (self.lift_curve_slope *
                  (math.radians(alpha) - self.zero_lift_angle))

        if alpha > self.wing.stall_angle - 5: # Stall model
            return max(0, result - (((alpha -
                    self.wing.stall_angle + 5) ** 2) / 100))
        else:
            return result

    def cf(self): # Flow assumed to be laminar (Re < 5 x 10^5)
        return 1.328 / math.sqrt(self.reynolds_number)

    def ff(self):
        return (1 + 2.7 * self.wing.airfoil.max_thickness +
                100 * self.wing.airfoil.max_thickness ** 4)

    def cd0(self):
        return self.cf() * self.ff() * 2
        # Wing isolated - ratio of wetted to
        # reference area assumed to be 2

    def cdi(self, alpha):
        return (self.cl(alpha) ** 2 / (math.pi
                * self.wing.ar * self.wing.oswald_efficiency))

    def cd(self, alpha):
        result = self.cd0() + self.cdi(alpha)

        if alpha > self.wing.stall_angle - 5: # Stall model
            return result + (((alpha -
                    self.wing.stall_angle + 5) ** 2) / 1500)
        else:
            return result

    def ld(self,alpha):
        return self.cl(alpha) / self.cd(alpha)

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