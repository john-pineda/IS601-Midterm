import pytest
from app import App
import logging

@pytest.fixture
def app_instance():
    return App('history.csv')  # Pass history_file to App constructor

def test_app_start_exit_command(capfd, monkeypatch, app_instance):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    with pytest.raises(SystemExit):
        app_instance.start()

def test_app_start_add_command(capfd, monkeypatch, app_instance):
    inputs = iter(['5', '3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    with pytest.raises(SystemExit):
        app_instance.start()

def test_app_start_unknown_command(capfd, monkeypatch, app_instance):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    with pytest.raises(SystemExit):
        app_instance.start()

    # Verify that the unknown command was handled as expected
    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    pytest.main([__file__])
