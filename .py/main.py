import json
from modules.airfoil import Airfoil

# load configs
def load_json(filename):
    with open(filename, "r") as file:
        return json.load(file)

class Simulation:
    def __init__(self):
        self.sim_config = load_json("simulation.json")
        self.trial = load_json(self.sim_config["trial"])
        self.baseline = load_json("baseline.json")

sim = Simulation()

# build objects
airfoil = Airfoil(sim.trial["airfoil"])
base_airfoil = Airfoil(sim.baseline["airfoil"])