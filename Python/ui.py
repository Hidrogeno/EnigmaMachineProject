import os
def welcome_message():
    os.system("clear")
    print("Welcome to the Enigma Machine Emulator!")
def set_shift():
    shiftA = int(input("Give me the initial shift for rotor I :"))
    shiftB = int(input("Give me the initial shift for rotor II :"))
    shiftC = int(input("Give me the initial shift for rotor III :"))
    return (shiftA,shiftB,shiftC)
def setup():
    welcome_message()
    shift = set_shift()
    return shift