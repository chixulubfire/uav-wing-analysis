class Airfoil:
    def __init__(self, name):
        self.name = name

        if "NACA" in name and len(name) == 8: #NACA4
            self.max_camber = int(name[4]) / 100
            self.max_camber_loc = int(name[5]) / 10
            self.max_thickness = int(name[6:8]) / 100
        else:
            raise ValueError("Error: Invalid airfoil. "
                             "Check supported_airfoils.txt")