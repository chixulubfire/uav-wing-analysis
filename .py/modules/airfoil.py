class Airfoil:
    def __init__(self, name):
        self.name = name

        if "NACA" in name and len(name) == 8:
            self.naca4(name[4:8])
        else:
            print("Error: Invalid airfoil. Check supported_airfoils.txt")

    def naca4(self, code):
        self.max_camber = int(code[0]) / 100
        self.max_camber_loc = int(code[1]) / 10
        self.max_thickness = int(code[2:4]) / 100