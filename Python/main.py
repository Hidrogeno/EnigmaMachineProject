import rotor
import ui

current_shift = ui.setup()
rotor_a = rotor.Rotor(current_shift[0])
rotor_b = rotor.Rotor(current_shift[1])
rotor_c = rotor.Rotor(current_shift[2])
encrypted_message = ""
message = input ("\n\nGive me your message:\n")
for character in message.upper():
    encrypted_message += rotor_c.step(rotor_b.step(rotor_a.step(character,True), rotor_a.rollFlag),rotor_b.rollFlag)
    current_shift = (rotor_a.position,rotor_b.position,rotor_c.position)
print(f"\nHere's your encrypted Message:\n{encrypted_message}")
print(f"\nHere's the final position of the rotors: {current_shift}")
