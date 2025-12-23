class Plugboard:
    # This part of the code emulates the plugboard functionality of the Enigma machine.

    def __init__(self, pairs=None):
        self.mapping = {}
        if pairs is not None: # If no pairs are given, the plugboard does nothing
            for a, b in pairs:
                self.mapping[a] = b
                self.mapping[b] = a

    def swap(self, character):
        return self.mapping.get(character, character)