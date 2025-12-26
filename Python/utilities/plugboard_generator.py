from pathlib import Path
import pandas as pd
import os

#### NOT YET IN USE ####
file_path = os.path.join(Path(__file__).resolve().parent, "plugboard_config.csv")
default_pairs = [("A", "G"), ("B", "F"), ("C", "E"), ("D", "H"), ("I", "J"),
         ("K", "L"), ("M", "N"), ("O", "P"), ("Q", "R"), ("S", "T")]

def generate_plugboard_config(pairs = default_pairs, filename = file_path):
    # Makes a plugboard.csv file that will hold the plugboard configuration
    
    data = {"Character": [], "Mapped To": []}
    for a, b in pairs:
        data["Character"].append(a)
        data["Mapped To"].append(b)
        data["Character"].append(b)
        data["Mapped To"].append(a) 
    pd.DataFrame(data).to_csv(filename, index = False)
    return

def read_plugboard_config(filename=file_path):
    df = pd.read_csv(filename)
    pairs = []
    for index, row in df.iterrows():
        pairs.append((row["Character"], row["Mapped To"]))
    return pairs