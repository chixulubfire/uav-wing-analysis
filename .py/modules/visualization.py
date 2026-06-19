import numpy as np
import matplotlib.pyplot as plt
import math as mt

class Visualization:
    def __init__(self, aerodynamics):
        self.aerodynamics = aerodynamics

        self.n = aerodynamics.physics["numerics"]["airfoil_points"]

    def plot_airfoil(self, title):
        if self.aerodynamics.wing.airfoil.type == "NACA4":
            self.plot_naca4(title)
        else:
            pass

    def plot_naca4(self, title):
        # NACA 4-digit coordinate generation adapted from:
        # https://web.itu.edu.tr/~atares/courses/CA/3.1.1_NACA4.html

        m = self.aerodynamics.wing.airfoil.max_camber
        p = self.aerodynamics.wing.airfoil.max_camber_loc
        t = self.aerodynamics.wing.airfoil.max_thickness
        c = self.aerodynamics.wing.mean_chord

        # naca4 coefficients
        a0 = 1.4845
        a1 = -0.6300
        a2 = -1.7580
        a3 = 1.4215
        a4 = -0.5075

        n = self.n # Points to graph
        x = np.linspace(0, c, n) # x coordinate
        y = np.zeros(n) # y coordinate
        yc = np.zeros(n) # y coordinate of camber line
        dyc = np.zeros(n) # gradient of camber line
        yt = np.zeros(n) # thickness distribution
        xu = np.zeros(n) # x coordinate of upper surface
        yu = np.zeros(n) # y coordinate of upper surface
        xl = np.zeros(n) # x coordinate of lower surface
        yl = np.zeros(n) # y coordinate of lower surface

        for i in range(n):
            if x[i] / c < p:
                yc[i] = ((c * m / p ** 2) *
                         (2 * p * (x[i] / c) - (x[i] / c) ** 2))
                dyc[i] = ((2 * m) / p ** 2) * (p - (x[i] / c))
            else:
                yc[i] = ((c * m / (1 - p) ** 2) *
                         (1 - 2 * p + 2 * p * (x[i] / c)
                          - (x[i] / c) ** 2))
                dyc[i] = (((2 * m) / (1 - p) ** 2)
                          * (p - (x[i] / c)))

        for i in range(n):
            yt[i] = (t * c) * (
                        a0 * mt.sqrt(x[i] / c) + a1 * (x[i] / c)
                        + a2 * (x[i] / c) ** 2 + a3 * (x[i] / c)
                        ** 3 + a4 * (x[i] / c) ** 4)
            teta = mt.atan(dyc[i])
            xu[i] = x[i] - yt[i] * mt.sin(teta)
            xl[i] = x[i] + yt[i] * mt.sin(teta)
            yu[i] = yc[i] + yt[i] * mt.cos(teta)
            yl[i] = yc[i] - yt[i] * mt.cos(teta)

        plt.title(title)
        plt.axis('equal')
        plt.plot(xu, yu, color='black')
        plt.plot(xl, yl, color='black')
        plt.plot(x, yc, 'b--')
        plt.yticks([])
        plt.xticks([])
        plt.show()

    def plot(self, title):
        results = self.aerodynamics.alpha_sweep()

        alpha = results["alpha"]
        cl = results["cl"]
        cd = results["cd"]
        ld = results["ld"]

        fig, axs = plt.subplots(3, 1, figsize=(6, 10), sharex=True)

        # CL
        axs[0].axvline(x=self.aerodynamics.wing.stall_angle,
                       color='red', linestyle='--', linewidth=2)
        axs[0].plot(alpha, cl)
        axs[0].set_ylabel("CL")
        axs[0].grid(True)
        axs[0].set_title(title + " Aerodynamic Performance vs Angle of Attack")

        # CD
        axs[1].axvline(x=self.aerodynamics.wing.stall_angle,
                       color='red', linestyle='--', linewidth=2)
        axs[1].plot(alpha, cd)
        axs[1].set_ylabel("CD")
        axs[1].grid(True)

        # L/D
        axs[2].axvline(x=self.aerodynamics.wing.stall_angle,
                       color='red', linestyle='--', linewidth=2)
        axs[2].plot(alpha, ld)
        axs[2].set_ylabel("L/D")
        axs[2].set_xlabel("Angle of Attack (deg)")
        axs[2].grid(True)

        plt.tight_layout()
        plt.show()