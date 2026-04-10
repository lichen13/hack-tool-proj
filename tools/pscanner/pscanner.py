from concurrent.futures import ThreadPoolExecutor
import socket
import os

LISTS_DIR = os.path.join(os.path.dirname(__file__), "lists")

def load_ports(filename: str) -> list[int]:
    path = os.path.join(LISTS_DIR, filename)

    with open(path, "r") as f:
        try:
            return [int(line.strip()) for line in f if line.strip().isdigit()]

        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return []
        
def run_scanner(target: str, list_name: str, threads: int):
    ports = load_ports(list_name)

    with ThreadPoolExecutor(max_workers=threads) as executor:
        for port in ports:
            executor.submit(scan_single_port, target, port)

def scan_single_port(target_host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        result = s.connect_ex((target_host, port))

        if result == 0:
            print(f"Port {port} is open")

def main():
    os.system("clear")
    print("Port Scanner - By: Lichen")
    print("0. Exit\n1. Quick scan\n2. Full scan")
    
    choice = input("\nOption taken: ").strip()

    if choice == "0":
        os.system("clear")
        print("\nSee you soon.\n")
        return
    
    if choice in ("1", "2"):
        target = input("Enter target host: ")

        if choice == "1":
            run_scanner(target, "quick_scan.list", 100)
        else:
            run_scanner(target, "full_scan.list", 2000)

    else:
        os.system("clear")
        print("\nInvalid option, Please try again.")