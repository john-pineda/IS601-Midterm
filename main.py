import os
import logging
from dotenv import load_dotenv
import pandas as pd  # Import Pandas
from app import App
from app.commands import CommandHandler

class App:
    def start(self):
        logging.info("Application started. Type 'exit' to exit.")
        while True:
            user_input = input(">>> ").strip()
            if user_input.lower() == 'load':
                filename = input("Enter filename to load history: ")
                try:
                    self.load_history(filename)
                    print("History loaded successfully.")
                except Exception as e:
                    print(f"Error loading history: {e}")
            elif user_input.lower() == 'save':
                filename = input("Enter filename to save history: ")
                try:
                    self.save_history(filename)
                    print("History saved successfully.")
                except Exception as e:
                    print(f"Error saving history: {e}")
            elif user_input.lower() == 'clear':
                self.clear_history()
                print("Calculation history cleared.")
            elif user_input.lower() == 'delete':
                index = int(input("Enter index of record to delete: "))
                try:
                    self.delete_history_record(index)
                    print("Record deleted.")
                except Exception as e:
                    print(f"Error deleting record: {e}")
            else:
                # Execute command and update history
                result = self.command_handler.execute_command(user_input)
                if result is not None:
                    self.history = self.history.append({'Operation': user_input, 'Result': result}, ignore_index=True)
