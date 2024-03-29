import pkgutil
import importlib
from app.commands import CommandHandler, Command
import logging
from app.plugins.menu import MenuCommand  # Import MenuCommand
from history_manager.history_manager import CalculationHistoryManager

class App:
    def __init__(self, history_file):  # Pass history_file as a parameter
        self.command_handler = CommandHandler()
        self.history_manager = CalculationHistoryManager(history_file)  # Pass history_file to CalculationHistoryManager
        self.loaded_plugins = False  

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
            if user_input == 'load_history':
                self.history_manager.load_history()
            elif user_input == 'save_history':
                self.history_manager.save_history()
            elif user_input == 'clear_history':
                self.history_manager.clear_history()
            elif user_input.startswith('delete_history'):
                index = int(user_input.split()[1])
                self.history_manager.delete_history_record(index)
            elif user_input == 'show_history':
                self.history_manager.show_history()
            else:
                self.command_handler.execute_command(user_input)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    app = App('history.csv')
    app.start()
