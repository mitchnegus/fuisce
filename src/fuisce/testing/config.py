"""
App configuration(s) for testing database interactions.
"""


class DefaultTestingConfig:
    """A Flask configuration designed for testing."""

    TESTING = True
    SECRET_KEY = "testing key"
    DATABASE_INTERFACE_ARGS = ()
    DATABASE_INTERFACE_KWARGS = {}

    def __init__(self, db_path=None):
        self.DATABASE = db_path
