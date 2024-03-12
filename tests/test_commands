import pytest
from app import App
from app.commands import CommandHandler
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.goodbye import GoodbyeCommand
from app.plugins.greet import GreetCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand


def test_add_command(capfd, monkeypatch):
    inputs = iter(['5', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    command = AddCommand()
    command.execute()
    
    out, err = capfd.readouterr()
    assert "Result of 5.0 + 3.0 = 8.0" in out

def test_subtract_command(capfd, monkeypatch):
    inputs = iter(['5', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    command = SubtractCommand()
    command.execute()
    
    out, err = capfd.readouterr()
    assert "Result of 5.0 - 3.0 = 2.0" in out

def test_multiply_command(capfd, monkeypatch):
    inputs = iter(['5', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    command = MultiplyCommand()
    command.execute()
    
    out, err = capfd.readouterr()
    assert "Result of 5.0 * 3.0 = 15.0" in out

def test_divide_command(capfd, monkeypatch):
    inputs = iter(['5', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    command = DivideCommand()
    command.execute()
    
    out, err = capfd.readouterr()
    assert "Result of 5.0 / 2.0 = 2.5" in out

def test_greet_command(capfd):
    command = GreetCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert out == "Hello, World!\n", "The GreetCommand should print 'Hello, World!'"

def test_goodbye_command(capfd):
    command = GoodbyeCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert out == "Goodbye\n", "The GoodbyeCommand should print 'Goodbye'"
