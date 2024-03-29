import pkgutil
import importlib
from app.commands import CommandHandler, Command
import logging
from app.plugins.menu import MenuCommand  # Import MenuCommand

class App:
    def __init__(self):  
        self.command_handler = CommandHandler()
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
            self.command_handler.execute_command(user_input)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    app = App()
    app.start()
