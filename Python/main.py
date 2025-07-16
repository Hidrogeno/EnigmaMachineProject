import string
import ui
ALPHABET = string.ascii_uppercase #Here we got a copy of the alphabet
currentShift = 0
def shift_rotor(shift):
    shifted = ALPHABET[shift:] + ALPHABET[:shift]
    return dict(zip(ALPHABET, shifted))

def encrypt_message(message, shift):
    _shift = shift
    result = ""

    for character in message.upper():
        if _shift >= len(ALPHABET):
            _shift = 0
        _shift += 1
        translationTable = shift_rotor(_shift)
        if character in translationTable:
            result += translationTable[character]
        else:
            result += character
            
    return result

currentShift = ui.setup(currentShift)
message = input ("Give me your message: ")
encryptedMessage = encrypt_message(message, currentShift)
print(encryptedMessage)