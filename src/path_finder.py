import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, os.pardir)) # os.pardir is the equivalent of ".." which means "go up one directory"

FILES = {
    "menu_template": os.path.join(ROOT, "src", "templates", "main_menu.txt"),
    "port_scanner_template": os.path.join(ROOT, "src", "templates", "port_scanner_menu.txt"),
    "full_scan_list": os.path.join(ROOT, "src", "scanner", "lists", "full_scan.txt"),
    "quick_scan_list": os.path.join(ROOT, "src", "scanner", "lists", "quick_scan.txt")
}