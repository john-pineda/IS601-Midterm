from app.commands import Command

class MenuCommand(Command):
    def __init__(self, command_handler):
        super().__init__()  # Call the superclass constructor
        self.command_handler = command_handler

    def execute(self):
        print("Available Commands:")
        for command_name in self.command_handler.commands.keys():
            print(f"- {command_name}")
