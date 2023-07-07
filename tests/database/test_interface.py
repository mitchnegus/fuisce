"""Tests for the database interface."""
from unittest.mock import patch

import pytest
from sqlalchemy import select
from sqlalchemy.sql.expression import func

from fuisce.database import SQLAlchemy, db_transaction
from fuisce.testing import DefaultTestingConfig, transaction_lifetime

from testing_helpers import Entry, create_test_app


@pytest.fixture
def default_interface():
    SQLAlchemy.create_default_interface()
    yield
    # Reset the default interface after the test
    SQLAlchemy.default_interface = None


class TestInterface:
    def test_interface_database(self, app):
        assert "entries" in app.db.tables.keys()

    def test_default_interface(self, app, default_interface):
        assert isinstance(app.db.default_interface, SQLAlchemy)

    def test_default_interface_unset(self, app):
        assert app.db.default_interface is None

    def test_production_default_interface(self, default_interface):
        with patch.object(DefaultTestingConfig, "TESTING", new=False):
            app = create_test_app(DefaultTestingConfig())
            assert isinstance(app.db.default_interface, SQLAlchemy)

    def test_production_default_interface_unset(self):
        with patch.object(DefaultTestingConfig, "TESTING", new=False):
            with pytest.raises(RuntimeError):
                app = create_test_app(DefaultTestingConfig())


# Define a function that uses the session transaction decorator to commit an action
def execute_database_transaction(app, x, y):
    entry = Entry(x=x, y=y, user_id=1)
    app.db.session.add(entry)


@pytest.mark.parametrize(
    "execution_function, expected_count",
    [
        [db_transaction(execute_database_transaction), 1],
        [execute_database_transaction, 0],
    ],
)
@transaction_lifetime
def test_transaction_decorator(client_context, app, execution_function, expected_count):
    x, y = 5, "fifty"
    execution_function(app, x, y)
    # Ensure that the entry was actually added
    query = select(func.count(Entry.x)).where(Entry.y == y)
    assert app.db.session.execute(query).scalar() == expected_count
