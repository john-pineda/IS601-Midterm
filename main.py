import os
import logging
from dotenv import load_dotenv
from app import App

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.info("Logging configured.")

    # Load environment variables
    load_dotenv()
    logging.info("Environment variables loaded.")

    # Create an instance of the App and start it
    app = App('history.csv')
    app.start()
