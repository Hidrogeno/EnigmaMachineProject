class Reflector:
    # TODO: Add support for different dictionaries
    wiring = {
        "A": "O", "B": "I", "C": "P", "D": "F", "E": "T", "F": "D",
        "G": "J", "H": "V", "I": "B", "J": "G", "K": "Y", "L": "Q",
        "M": "S", "N": "U", "O": "A", "P": "C", "Q": "L", "R": "X", "S": "M",
        "T": "E", "U": "N", "V": "H", "W": "Z", "X": "R", "Y": "K", "Z": "W"
        }

    def __init__(self):
        pass
    
    def reflect(self, character):
        return self.wiring.get(character, character)