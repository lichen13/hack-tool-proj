import os
from tools.pscanner.pscanner import main as pscanner_main

def main():
    if os.name != "posix":
        print("HackToolProj only works on Linux.")
        return

    os.system("clear")

    print("HackToolProj - By: Lichen")
    print("\n0. Exit\n1. Port Scanner\n2. Coming soon...\n3. Coming soon...\n4. Coming soon...")
    
    choice = input("\nSelect an option: ").strip()

    if choice == "0":
        os.system("clear")
        print("See you soon.")
        return
    elif choice == "1":

        if not os.path.exists("tools/pscanner"):
            os.system("clear")
            print("Directory 'tools/pscanner' not found.")
            return
        
        pscanner_main()

    else:
        os.system("clear")
        print("Invalid option. Please try again.")
        return
    
main()