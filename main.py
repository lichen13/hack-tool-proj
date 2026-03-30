import os
import requests

def startup():
    if os.name == "posix":
        os.system("clear")
    else:
        print("HackToolProj only works on a Linux based system.")
        exit()

    os.makedirs("Tools", exist_ok=True) # Skip if already created.
    
    print("HackToolProj - By: Lichen")

    while True:
        print("\nMenu:")
        print("0. Exit")
        print("1. Port Scanner ( not working yet )")
        optionTaken = input("\nOption taken: ").strip()

        if optionTaken == "0":
            os.system("clear")
            print("\nSee you soon.\n")
            exit()
        elif optionTaken == "1":
            os.system("clear")
            print("\nPort Scanner is not accessible yet.")
        else:
            os.system("clear")
            print("\nInvalid option, Please try again.")

startup()