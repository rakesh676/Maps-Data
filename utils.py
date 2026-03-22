import pandas as pd
import logging

# Initialize logging
logging.basicConfig(level=logging.DEBUG)

def save_excel(data, file_name):
    """Save data to an Excel file with error handling and logging."""
    try:
        data.to_excel(file_name)
        logging.info(f"Excel file saved: {file_name}")
    except Exception as e:
        logging.error(f"Error saving Excel file: {e}")

