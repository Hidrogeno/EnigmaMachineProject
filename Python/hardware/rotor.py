import string
AB = string.ascii_uppercase #ALPHABET
class Rotor:
    length = len(AB)

    def __init__(self, position):
        self.position = position
        self.rollFlag = False
    
    def turn(self):
        # Turns the rotor one position, it restarts once it has made a full turn
        
        self.position = (self.position + 1) % self.length
        self.rollFlag = (self.position == 0)       
    
    def translate(self, character):
        # Takes one character and outputs it's corresponding character
        # with the current translation table 
        
        if character not in AB:
            return character
        index = AB.index(character)
        return AB[(index + self.position) % self.length]
    
    def translate_back(self, character):
        # Reverse method for signal reflection
        
        if character not in AB:
            return character
        index = AB.index(character)
        new_index = (AB.index(character) - self.position) % self.length
        return AB[new_index]
    
    def set_flag(self, flag):
        self.rollFlag = flag

    def step(self, character, flag):
        # Translates the input character and turns one position if the flag is raised
        
        if flag:    #It is important that the turn happens before the translation
            self.turn() 
        result = self.translate(character)
        return result
