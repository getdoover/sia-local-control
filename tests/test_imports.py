"""
Basic tests for an application.

This ensures all modules are importable and that the config is valid.
"""

def test_import_app():
    from sia_local_control.application import SiaLocalControlApplication
    assert SiaLocalControlApplication

def test_config():
    from sia_local_control.app_config import SiaLocalControlConfig

    config = SiaLocalControlConfig()
    assert isinstance(config.to_dict(), dict)

def test_ui():
    from sia_local_control.app_ui import SiaLocalControlUI
    assert SiaLocalControlUI

def test_state():
    from sia_local_control.app_state import SiaLocalControlState
    assert SiaLocalControlState