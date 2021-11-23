import pytest
import app
from controllers import cars

@pytest.fixture
def api(monkeypatch):
    test_cars = [
        {'id': 1, 'make': 'Test Car 1', 'year': 2003},
        {'id': 2, 'make': 'Test Car 2', 'year': 1999}
    ]
    monkeypatch.setattr(cars, "cars", test_cars)
    api = app.app.test_client()
    return api
    