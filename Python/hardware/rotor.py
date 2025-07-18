import string
AB = string.ascii_uppercase
class Rotor:
    length = len(AB)-1
    rollFlag = False

    def __init__(self, position):
        self.position = position
    
    def turn(self):
        # Turns the rotor one position, it restarts once it has made a full turn
        
        if self.position < self.length:
            self.position = self.position+1
            self.set_flag(False) 
        else: 
            self.position = 0
            self.set_flag(True)
    
    def translate(self, character):
        # Takes one character and outputs it's corresponding character
        # with the current translation table 
        
        pos = self.position
        translation_table = dict(zip(AB, AB[pos:] + AB[:pos]))
        return translation_table[character] if character in translation_table else character
    
    def translate_back(self, character):
        # Reverse method for manual decription mode
        
        pos = self.position
        translation_table = dict(zip(AB[pos:] + AB[:pos], AB))
        return translation_table[character] if character in translation_table else character
    
    def set_flag(self, flag):
        self.rollFlag = flag

    def step(self, character, flag):
        # Translates the input character and turns one position if the flag is raised
        
        result = self.translate(character)
        if flag:
            self.turn()
        return result
        
    def anti_step(self,character,flag):
        # Translates the input character and turns one position if the flag is raised
        
        result = self.translate_back(character)
        if flag:
            self.turn()
        return result
