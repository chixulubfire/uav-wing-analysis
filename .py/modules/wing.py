class Wing:
    def __init__(
            self,
            airfoil,
            span,
            r_chord,
            t_chord,
            twist,
            sweep,
            dihedral
    ):
        self.airfoil = airfoil

        self.span = span
        self.r_chord = r_chord
        self.t_chord = t_chord

        self.twist = twist
        self.sweep = sweep
        self.dihedral = dihedral

        # Derived geometries
        self.area = self.r_chord * self.t_chord / 2 * self.span
        self.ar = self.span ** 2 / self.area
        self.taper = self.t_chord / self.r_chord
        self.mean_chord = (r_chord + t_chord) / 2