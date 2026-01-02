import hardware.machine as em
import ui.cli as cli

enigma = em.Enigma(cli.setup())
result = enigma.encrypt(cli.request_message())
cli.exit_message(result, enigma.get_shift())