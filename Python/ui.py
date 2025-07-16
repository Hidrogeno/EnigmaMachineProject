import os
def welcome_message():
    os.system("clear")
    print("Welcome to the Enigma Machine Emulator!")
def set_shift():
    shift = int(input("Give me the initial shift for rotor I :"))
    return shift
def setup(shift):
    welcome_message()
    shift = set_shift()
    return shift