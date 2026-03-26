# /hacking_tool_proj/src/logger.py

import os
from datetime import datetime

# Set log directory & file

LOG_DIR = os.path.dirname(__file__)
LOG_FILE = os.path.join(LOG_DIR, "../logs/tool.log")

# Set the logger
# How a normal .log file should looks like:
#   File: '/src/main.py', line: 19, in show_menu() --> Invalid input field.

class Logger:
    def log(filepath, line, function, report):
        timestamp = datetime.now().strftime("[%b-%d-%Y] - %H:%M:%S")

        if filepath == None:
            filepath = "not specified"

        if line == None:
            line = "not specified"

        if function == None:
            function = "not specified"

        if report == None:
            report = "This report is empty."

        format = f"{timestamp} | Location: '{filepath}', line(s): {line}, in {function} ➜  {report}"

        with open(LOG_FILE, "a") as f:
            f.write(f"{format}\n")
