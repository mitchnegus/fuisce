import pytest

from fuisce.testing import AppTestManager

from testing_helpers import Entry, create_test_app


class FuisceAppTestManager(AppTestManager):
    """
    A test manager for Fuisce.

    Although Fuisce is not itself a Flask app, this test manager exists
    to test that Fuisce works properly when applied to other test apps.
    """

    def prepare_test_database(self, db):
        with db.session.begin():
            entries = [
                Entry(x=1, y="ten", user_id=1),
                Entry(x=2, y="eleven", user_id=1),
                Entry(x=3, y="twelve", user_id=1),
                Entry(x=4, y="twenty", user_id=2),
            ]
            db.session.add_all(entries)


# Instantiate the app manager to determine the correct app (persistent/ephemeral)
app_manager = FuisceAppTestManager(factory=create_test_app)


@pytest.fixture(scope="session")
def app_test_manager():
    # Provide access to the app test manager as a fixture
    return app_manager


@pytest.fixture
def app():
    yield app_manager.get_app()


@pytest.fixture
def client(app):
    yield app.test_client()


@pytest.fixture
def client_context(client):
    with client:
        # Context variables (e.g., `g`) may be accessed only after response
        client.get("/")
        yield
