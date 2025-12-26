import os
from pathlib import Path
plugboard_path = os.path.join(Path(__file__).resolve().parent, "plugboard_config.csv")

def welcome_message():
    os.system("clear")
    os.system("clear")
    print("Welcome to the Enigma Machine Emulator!")
    input("Press Enter to continue...")
    os.system("clear")

def set_shift():
    try:
        shift_a = int(input("Give me the initial shift for rotor A : "))
        shift_b = int(input("Give me the initial shift for rotor B : "))
        shift_c = int(input("Give me the initial shift for rotor C : "))
    except ValueError:
        print("Invalid input. Please enter an integer value.")
        input("Press Enter to try again...")
        os.system("clear")
        return set_shift()
    
    return (shift_a,shift_b,shift_c)

def setup():
    check_plugboard()
    welcome_message()
    shift = set_shift()
    return shift

def exit_message(message, current_shift):
    os.system("clear")
    print(f"Your encrypted message is {message}")
    print(f"The final gear configuration is (A,B,C) = {current_shift}")
    input("Press Enter to exit...")
    os.system("clear")

def request_message():
    os.system("clear")
    message = input ("Give me your message:\n")
    return message

def check_plugboard():
    #### NOT YET IN USE ####
    
    try:
        open(plugboard_path, "r")
    except:
        from utilities.plugboard_generator import generate_plugboard_config
        generate_plugboard_config()
    return