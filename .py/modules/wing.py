class Wing:
    def __init__(
            self,
            airfoil,
            span,
            r_chord,
            t_chord,
            twist,
            sweep,
            dihedral,

            efficiency,
            stall_angle
    ):
        self.airfoil = airfoil

        self.span = span
        self.r_chord = r_chord
        self.t_chord = t_chord

        self.twist = twist
        self.sweep = sweep
        self.dihedral = dihedral

        self.oswald_efficiency = efficiency
        self.stall_angle = stall_angle

        # Derived geometries
        self.area = (self.r_chord + self.t_chord) / 2 * self.span
        self.ar = self.span ** 2 / self.area
        self.taper = self.t_chord / self.r_chord
        self.mean_chord = ((2/3) * self.r_chord *
                           ((1 + self.taper + self.taper**2)/(1 + self.taper)))