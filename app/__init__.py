import os
import pkgutil
import importlib
from app.commands import CommandHandler, Command
import logging
from app.plugins.menu import MenuCommand  # Import MenuCommand
import pandas as pd

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        self.loaded_plugins = False
        self.history = pd.DataFrame(columns=['Operation', 'Result'])  # Initialize calculation history DataFrame

    def load_history(self, filename):
        if os.path.exists(filename):
            self.history = pd.read_csv(filename)

    def save_history(self, filename):
        self.history.to_csv(filename, index=False)

    def clear_history(self):
        self.history = pd.DataFrame(columns=['Operation', 'Result'])

    def delete_history_record(self, index):
        self.history.drop(index, inplace=True)

    def load_plugins(self):
        if not self.loaded_plugins:
            plugins_package = 'app.plugins'
            for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
                if is_pkg:
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    for item_name in dir(plugin_module):
                        item = getattr(plugin_module, item_name)
                        try:
                            if issubclass(item, (Command)) and item != Command:
                                self.command_handler.register_command(plugin_name, item())
                        except TypeError:
                            continue
            self.loaded_plugins = True

        # Register MenuCommand
        self.command_handler.register_command("menu", MenuCommand(self.command_handler))  # Register MenuCommand

    def start(self):
        self.load_plugins()
        logging.info("Application started. Type 'exit' to exit.")
        while True:
            user_input = input(">>> ").strip()
            logging.info(f"User input: {user_input}")
            if user_input.lower() == 'exit':
                break
            elif user_input.lower() == 'load':
                filename = input("Enter filename to load history: ")
                self.load_history(filename)
            elif user_input.lower() == 'save':
                filename = input("Enter filename to save history: ")
                self.save_history(filename)
            elif user_input.lower() == 'clear':
                self.clear_history()
                print("Calculation history cleared.")
            elif user_input.lower() == 'delete':
                index = int(input("Enter index of record to delete: "))
                self.delete_history_record(index)
                print("Record deleted.")
            else:
                # Execute command and update history
                result = self.command_handler.execute_command(user_input)
                if result is not None:
                    self.history = self.history.append({'Operation': user_input, 'Result': result}, ignore_index=True)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    app = App()
    app.start()
