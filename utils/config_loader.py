import importlib.util
import os
import sys

# Get the path to the directory where the .exe (or script) is running
if getattr(sys, 'frozen', False):  # If the app is run as a bundle
    base_path = os.path.dirname(sys.executable)
else:  # If the app is run as a script
    base_path = os.path.dirname(os.path.abspath(__file__))

# Load config.py from the same directory as the executable or script
config_path = os.path.join(base_path, '../config.py')

# Dynamically import config.py
spec = importlib.util.spec_from_file_location("config", config_path)
config = importlib.util.module_from_spec(spec)
spec.loader.exec_module(config)

COOKIE = config.COOKIE
SID = config.SID
TIME_TO_SLEEP_BETWEEN_DOWNLOADS = config.TIME_TO_SLEEP_BETWEEN_DOWNLOADS
PAGE_SIZE = config.PAGE_SIZE
SORTED_BY = config.SORTED_BY
DOWNLOADING_RECORDS_LIMIT = config.DOWNLOADING_RECORDS_LIMIT
