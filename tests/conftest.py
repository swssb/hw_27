# conftest.py
from pytest_factoryboy import register

from tests.factories import AdFactory, UserFactory, SelectionFactory

pytest_plugins = "tests.fixtures"

register(AdFactory)
register(UserFactory)
register(SelectionFactory)