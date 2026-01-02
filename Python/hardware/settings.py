import os
import pandas as pd

#### NOT YET IN USE ####

class Config:
    # This will hold the current settings for the Enigma machine
    
    def __init__(self, settings):
        self.settings = settings

class Settings:
    # This is the archetype for the EnigmaMachine settings
    plugboard_path = os.path.join("Python", "utilities", "plugboard_config.csv")

    def __init__(self, rotor_positions, plugboard_pairs = None):
        self.positions = rotor_positions
        if plugboard_pairs is None:
            self.plugboard = pd.read_csv(self.plugboard_path)
        else:
            self.plugboard = pd.read_csv(plugboard_pairs)