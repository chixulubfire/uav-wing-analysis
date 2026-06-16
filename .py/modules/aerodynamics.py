import math

class Aerodynamics:
    def __init__(self, wing, physics):
        self.wing = wing
        self.physics = physics

        self.air_density = physics["air"]["air_density_kgm3"]
        self.dynamic_viscosity = physics["air"]["dynamic_viscosity_pas"]
        self.velocity = physics["air"]["velocity_pas"]

        self.oswald_efficiency = physics["model"]["oswald_efficiency"]
        self.stall_angle = physics["model"]["stall_angle_deg"]

    def reynolds_number(self):
        pass

    def cl(self):
        pass

    def cdi(self):
        pass

    def cd(self):
        pass

    def lift(self):
        pass

    def drag(self):
        pass