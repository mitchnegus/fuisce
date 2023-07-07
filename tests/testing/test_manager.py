"""Tests for the test manager."""
import pytest

from fuisce.testing import transaction_lifetime


class TestAppTestManager:
    ephemeral_app_ids = []

    def test_nontransaction(self, app_test_manager, app):
        assert app is app_test_manager.persistent_app
        assert app is not app_test_manager.ephemeral_app

    @pytest.mark.parametrize("execution_count", range(3))
    @transaction_lifetime
    def test_transaction(self, app_test_manager, app, execution_count):
        assert app is not app_test_manager.persistent_app
        assert app is app_test_manager.ephemeral_app
        assert id(app) not in self.ephemeral_app_ids
        self.ephemeral_app_ids.append(id(app))
