import logging
import os
from datetime import datetime

# Name of the log file
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# Create logs folder correctly
logs_folder = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_folder, exist_ok=True)

# Full log file path
LOG_FILE_PATH = os.path.join(logs_folder, LOG_FILE)

# Configure logger
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
