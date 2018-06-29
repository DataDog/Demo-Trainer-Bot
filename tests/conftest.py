import pytest
from src.gcal.calendar import Calendar

@pytest.fixture(scope='session')
def google_calendar():
    return Calendar('service-account.json')