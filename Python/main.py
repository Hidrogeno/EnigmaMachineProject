import hardware.machine as em
import ui

current_shift = ui.setup()
enigma = em.Enigma(current_shift)
encrypted_message = ""
message = input ("\n\nGive me your message:\n")
selection = input("\n\nPress 1 for enctryption, 2 for decryption:\n")

if selection == "1" :
    encrypt = True
    result = enigma.encrypt(message)
elif selection == "2" :
    encrypt = False
    result = enigma.decrypt(message)

current_shift = enigma.current_shift
ui.exit_message(encrypt, result, current_shift)