import os
import json
import mock
import pytest
from pytest_mock import mocker
from expects import expect, equal, contain

from src.app import app, pyBot, _event_handler

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

    def test_event_handler_understands_mentions(self):
        with app.app_context() as c:
            event = {
                    "type": "app_mention",
                    "user": "U061F7AUR",
                    "text": "<@U0LAN0Z89> is it everything a river should be?",
                    "ts": "1515449522.000016",
                    "channel": "C0LAN2Q65",
                    "event_ts": "1515449522000016"
                }

            data = {
                "token": os.environ.get("VERIFICATION_TOKEN"),
                "event": event
            }

            response = _event_handler("app_mention", data)
            expect(response.status_code).to(equal(200))
            expect(response.data.decode('utf-8')).to(contain("Parse"))

    def test_user_can_mention_bot(self, mocker):
        with app.app_context():
            with app.test_client() as c:
                event = {
                    "type": "app_mention",
                    "user": "U061F7AUR",
                    "text": "<@U0LAN0Z89> is it everything a river should be?",
                    "ts": "1515449522.000016",
                    "channel": "C0LAN2Q65",
                    "event_ts": "1515449522000016"
                }

                data = {
                    "token": os.environ.get("VERIFICATION_TOKEN"),
                    "event": event
                }

                response = c.post('/listening', data=json.dumps(data), content_type='application/json')
                expect(response.status_code).to(equal(200))
                
