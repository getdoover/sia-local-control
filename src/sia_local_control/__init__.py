from pydoover.docker import run_app

from .application import SiaLocalControlApplication
from .app_config import SiaLocalControlConfig

def main():
    """
    Run the application.
    """
    run_app(SiaLocalControlApplication(config=SiaLocalControlConfig()))
