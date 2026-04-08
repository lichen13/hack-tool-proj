from concurrent.futures import ThreadPoolExecutor
import socket
import os

def scan_single_port(target_host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        result = s.connect_ex((target_host, port))

        if result == 0:
            print(f"Port {port} is open")

def full_scan(target_host):
    p = []

    list_path = os.path.join(os.path.dirname(__file__), "lists", "full_scan.list")

    with open(list_path, "r") as f:
        for line in f:
            line = line.strip()
            if line.isdigit():
                p.append(int(line))
    
    with ThreadPoolExecutor(max_workers=2000) as executor:
        for port in p:
            executor.submit(scan_single_port, target_host, port)

    print("Note: Other ports scanned are closed or filtered.")

def quick_scan(target_host):
    p = []

    list_path = os.path.join(os.path.dirname(__file__), "lists", "quick_scan.list")
    
    with open(list_path, "r") as f:
        for line in f:
            line = line.strip()
            if line.isdigit():
                p.append(int(line))

    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in p:
            executor.submit(scan_single_port, target_host, port)

    print("Note: Other ports scanned are closed or filtered.")

def main():
    os.system("clear")

    print("Port Scanner - By: Lichen")
    print("\nMenu:")
    print("0. Exit")
    print("1. Quick scan")
    print("2. Full scan")

    choice = input("\nOption taken: ").strip()

    if choice == "0":
        os.system("clear")
        print("\nSee you soon.\n")
        exit()
    elif choice == "1":
        target = input("Enter target host: ")
        quick_scan(target)
    elif choice == "2":
        target = input("Enter target host: ")
        full_scan(target)
    else:
        os.system("clear")
        print("\nInvalid option, Please try again.")

main()