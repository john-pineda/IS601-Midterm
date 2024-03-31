import pytest
from app import App
import logging
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand

def test_app_start_exit_command(capfd: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit


def test_app_start_add_command(capfd: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch):
    """Test that the REPL exits correctly after 'add' command."""
    inputs = iter(['5', '3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    
    assert str(e.value) == "Exiting..."


def test_app_start_unknown_command(capfd: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    
    with pytest.raises(SystemExit) as excinfo:
        app.start()
    
    # Verify that the unknown command was handled as expected
    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    pytest.main([__file__])
