import hardware.machine as em
import ui

current_shift = ui.setup()
enigma = em.Enigma(current_shift)
encrypted_message = ""
message = input ("\n\nGive me your message:\n")
selection = input("\n\nPress 1 for enctryption, 2 for decryption:\n")

if selection == "1" :
    enigma.encrypt(message)
if selection == "2" :
    enigma.decrypt(message)