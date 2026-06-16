import json
from .airfoil import Airfoil
from .wing import Wing

def build_wing(config):
    airfoil = Airfoil(config["airfoil"])

    return Wing(
        airfoil,
        config["wing_span_m"],
        config["root_chord_length_m"],
        config["tip_chord_length_m"],
        config["twist_angle_deg"],
        config["sweep_angle_deg"],
        config["dihedral_angle_deg"]
    )

# load configs
def load_json(filename):
    with open(filename, "r") as file:
        return json.load(file)

class Simulation:
    def __init__(self):
        self.sim_config = load_json("../configs/simulation.json")
        self.trial = load_json(self.sim_config["trial"])
        self.baseline = load_json("../configs/baseline.json")

        self.wing = build_wing(self.trial)
        self.base_wing = build_wing(self.baseline)