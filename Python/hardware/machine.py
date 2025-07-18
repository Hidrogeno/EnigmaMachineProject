from hardware.rotor import Rotor
class Enigma:
    def __init__(self, shift):
        self.shift = shift
        self.rotor_a = Rotor(shift[0])
        self.rotor_b = Rotor(shift[1])
        self.rotor_c = Rotor(shift[2])
    
    def encrypt(self, message):
        encrypted_message = ""
        for character in message.upper():
            encrypted_message += self.rotor_c.step(self.rotor_b.step(self.rotor_a.step(character,True), self.rotor_a.rollFlag),self.rotor_b.rollFlag)
            self.current_shift = (self.rotor_a.position,self.rotor_b.position,self.rotor_c.position)
        return encrypted_message

    def decrypt(self, message):
        decrypted_message = ""
        for character in message.upper():
            decrypted_message += self.rotor_c.anti_step(self.rotor_b.anti_step(self.rotor_a.anti_step(character,True), self.rotor_a.rollFlag),self.rotor_b.rollFlag)
            self.current_shift = (self.rotor_a.position,self.rotor_b.position,self.rotor_c.position)
        return decrypted_message