
from app import App
import app
from app.commands import Command
import pandas as pd  # Import Pandas
from app.commands.add import AddCommand


class AddCommand(Command):
    def execute(self):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 + num2
        print(f"Result of {num1} + {num2} = {result}")

        # Update calculation history
        app.App.history = app.App.history.append({'Expression': f"{num1} + {num2}", 'Result': result}, ignore_index=True)