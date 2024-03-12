import pkgutil
import importlib
from app.commands import CommandHandler, Command

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
                                print(f"Available command: {plugin_name}")
                                self.command_handler.register_command(plugin_name, item())
                        except TypeError:
                            continue
            self.loaded_plugins = True

    def start(self):
        self.load_plugins()
        print("Type 'exit' to exit.")
        while True:
            user_input = input(">>> ").strip()
            print(f"User input: {user_input}")
            self.command_handler.execute_command(user_input)

if __name__ == "__main__":
    app = App()
    app.start()
