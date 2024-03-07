from app.commands import Command


class DivideCommand(Command):
    def execute(self):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"Result of {num1} / {num2} = {result}")
