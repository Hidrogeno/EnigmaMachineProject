from constants import ALPHABET as AB
class Rotor:
    length = len(AB)-1
    rollFlag = False

    def __init__(self, position):
        self.position = position
    
    def turn(self):
        # Turns the rotor one position, it restarts once it has made a full turn
        if self.position < self.length:
            self.position = self.position+1
            self.setFlag(False) 
        else: 
            self.position = 0
            self.setFlag(True)
    
    def translate(self, character):
        # Takes one character and outputs it's corresponding character
        # with the current translation table 
        
        pos = self.position
        translationTable = dict(zip(AB, AB[pos:] + AB[:pos]))
        return translationTable[character] if character in translationTable else character
    
    def setFlag(self, flag):
        self.rollFlag = flag

    def step(self, character, flag):
        result = self.translate(character)
        if flag:
            self.turn()
        return result
        