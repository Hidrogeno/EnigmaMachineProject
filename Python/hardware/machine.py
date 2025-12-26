from hardware.rotor import Rotor
from hardware.reflector import Reflector
from hardware.plugboard import Plugboard
class Enigma:
    reflector = Reflector()
    def __init__(self, shift):
        self.current_shift = shift
        self.rotor_a = Rotor(shift[0])
        self.rotor_b = Rotor(shift[1])
        self.rotor_c = Rotor(shift[2])
    
    def encrypt(self, message, plugboard=Plugboard()):
        encrypted_message = ""
        encrypted_char = ""
        for character in message.upper():
            encrypted_char = plugboard.swap(
                self.rotor_a.translate_back(
                    self.rotor_b.translate_back(
                        self.rotor_c.translate_back(
                            self.reflector.reflect(
                                self.rotor_c.step(
                                    self.rotor_b.step(
                                        self.rotor_a.step(
                                            plugboard.swap(character), True
                                        ), self.rotor_a.rollFlag
                                    ), self.rotor_b.rollFlag
                                )
                            )
                        )
                    )
                )
            )

            encrypted_message += encrypted_char
            self.current_shift = (self.rotor_a.position,self.rotor_b.position,self.rotor_c.position)
        return encrypted_message
    
    def get_shift(self):
        return self.current_shift