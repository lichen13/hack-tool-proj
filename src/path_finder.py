import os

HOME_PATH = os.path.expanduser("~")

FILES = {
    "menu_template": os.path.join(HOME_PATH, "hack_tool_proj", "src", "templates", "main_menu.txt"),
    "port_scanner_template": os.path.join(HOME_PATH, "hack_tool_proj", "src", "templates", "port_scanner_menu.txt"),
    "full_scan_list": os.path.join(HOME_PATH, "hack_tool_proj", "src", "scanner", "lists", "full_scan.txt"),
    "quick_scan_list": os.path.join(HOME_PATH, "hack_tool_proj", "src", "scanner", "lists", "quick_scan.txt")
}
