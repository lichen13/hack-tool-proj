# /hacking_tool_proj/src/scanner/main.py
# Imported module(s)

import socket
import os
from concurrent.futures import ThreadPoolExecutor
from logger import Logger
from path_finder import FILES



def scan_single_port(target_host, port):

    Logger.log("scanner/main.py", None, "scan_single_port", f"Scanning port {port}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        result = s.connect_ex((target_host, port))

        if result == 0:
            print(f"Port {port} is open")



def full_scan(target_host):

    ports = []

    with open(FILES["full_scan_list"], "r") as f:
        ports = [int(line.strip()) for line in f]

    # Start scanning
    # NOTE: Upgrade line below to adjust workers by the user device capacities
    with ThreadPoolExecutor(max_workers=2000) as executor:
        for port in ports:
            executor.submit(scan_single_port, target_host, port)

    print("Note: Other ports scanned are closed or filtered.")



def quick_scan(target_host):

    ports = []

    with open(FILES["quick_scan_list"], "r") as f:
        ports = [int(line.strip()) for line in f]

    # Start scanning
    # NOTE: Upgrade line below to adjust workers by the user device capacities
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in ports:
            executor.submit(scan_single_port, target_host, port)

    print("Note: Other ports scanned are closed or filtered.")



def show_scanner_menu():

    # Read and print data inside 'port_scanner_menu.txt'
    with open (FILES["port_scanner_template"], "r") as f:
        print(f.read())
    option_taken = input("[ ] Select an option : ")

    # Check option_taken
    if option_taken == "0":
        Logger.log("scanner/main.py", None, "show_scanner_menu", "option_taken==0. Exiting.")
        exit()

    elif option_taken == "1":
        Logger.log("scanner/main.py", None, "show_scanner_menu", "option_taken==1. Asking for target.")
        target_host = input("\nTarget: ")
        # NOTE: We should add a verif here to check if target host is actually a valid one.
        quick_scan(target_host)

    elif option_taken == "2":
        Logger.log("scanner/main.py", None, "show_scanner_menu", "option_taken==2. Asking for target.")
        target_host = input("\nTarget: ")
        # NOTE: We should add a verif here to check if target host is actually a valid one.
        full_scan(target_host)

    else:
        Logger.log("scanner/main.py", None, "show_scanner_menu", "Invalid input data. Exiting.")
        print("\nInvalid option.")
        exit()
