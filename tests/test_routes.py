import mock
import pytest
from pytest_mock import mocker
from expects import expect, equal, contain

from src.app import app, pyBot

class TestFlaskRoutes:
    def test_user_can_install(self):
        with app.test_client() as c:
            response = c.get('/install')
            expect(response.status_code).to(equal(200))
            html_string = response.data.decode("utf-8")
            expect(html_string).to(contain("Install"))
            expect(html_string).to(contain("button"))
    
    def test_user_can_be_thanked(self, mocker):
        with app.test_client() as c:
            mocker.patch.object(pyBot, 'auth') 
            pyBot.auth.return_value = True
            response = c.get('/thanks')

            expect(response.status_code).to(equal(200))

            html_string = response.data.decode('utf-8')
            expect(html_string).to(contain('Thanks for installing!'))