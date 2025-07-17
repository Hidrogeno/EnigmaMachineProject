import rotor
import ui

currentShift = ui.setup()
rotorA = rotor.Rotor(currentShift[0])
rotorB = rotor.Rotor(currentShift[1])
rotorC = rotor.Rotor(currentShift[2])
encryptedMessage = ""
message = input ("\n\nGive me your message:\n")
for character in message.upper():
    encryptedMessage += rotorC.step(rotorB.step(rotorA.step(character,True), rotorA.rollFlag),rotorB.rollFlag)
    #encryptedMessage += rotorA.step(character,True)
    currentShift = (rotorA.position,rotorB.position,rotorC.position)
print(f"\nHere's your encrypted Message:\n{encryptedMessage}")
print(f"\nHere's the final position of the rotors: {currentShift}")