import hardware.machine as em
import ui

enigma = em.Enigma(ui.setup())
result = enigma.encrypt(ui.request_message())
ui.exit_message(result, enigma.get_shift())