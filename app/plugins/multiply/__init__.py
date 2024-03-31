# /home/jpineda/is601/calculator_design/app/plugins/multiply/__init__.py

from app import App
import app
from app.commands import Command
import pandas as pd  # Import Pandas

from app.commands import Command
import app

class DivideCommand(Command):
    def execute(self):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if num2 == 0:
            print("Error: Division by zero!")
        else:
            result = num1 / num2
            print(f"Result of {num1} / {num2} = {result}")

            # Update calculation history
            app.App.history = app.App.history.append({'Expression': f"{num1} / {num2}", 'Result': result}, ignore_index=True)