import os

def welcome_message():
    os.system("clear")
    print("Welcome to the Enigma Machine Emulator!")
    input()
    os.system("clear")

def set_shift():
    shift_a = int(input("Give me the initial shift for rotor I :"))
    shift_b = int(input("Give me the initial shift for rotor II :"))
    shift_c = int(input("Give me the initial shift for rotor III :"))
    return (shift_a,shift_b,shift_c)

def setup():
    welcome_message()
    shift = set_shift()
    return shift

def exit_message(encrypt, message, current_shift):
    mode = "encrypted" if encrypt else "decrypted"
    print(f"Your {mode} message is {message}")
    print(f"The current gear configuration is {current_shift}")