import os
def welcome_message():
    os.system("clear")
    print("Welcome to the Enigma Machine Emulator!")
def set_shift():
    shift_a = int(input("Give me the initial shift for rotor I :"))
    shift_b = int(input("Give me the initial shift for rotor II :"))
    shift_c = int(input("Give me the initial shift for rotor III :"))
    return (shift_a,shift_b,shift_c)
def setup():
    welcome_message()
    shift = set_shift()
    return shift
