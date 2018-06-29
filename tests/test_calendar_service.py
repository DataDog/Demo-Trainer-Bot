import os
import pytest

from utils.test_inject import auto_inject_fixtures
from expects import expect, equal, be_above


@auto_inject_fixtures('google_calendar')
class TestCalendar:
    def test_calendar_service_can_see_calendars(self):
        service = self.google_calendar.service
        calendar_list = service.calendarList().list().execute()

        # I have shared my calendar with demo-trainer@datadog-demodog.iam.gserviceaccount.com
        expect(len(calendar_list['items'])).to(be_above(0))

    def test_calendar_service_can_make_and_delete_event(self):
        SHARED_CALENDAR_ID = os.environ['SHARED_CALENDAR_ID']
        GMT_OFF = '-04:00'  # Eastern Time
        evt = {
            'summary': 'Dinner with friends',
            'start':   {'dateTime': '2024-05-28T19:00:00%s' % GMT_OFF},
            'end':     {'dateTime': '2025-05-28T22:00:00%s' % GMT_OFF},
        }
        result = self.google_calendar.create_event(
            evt, calendarId=SHARED_CALENDAR_ID)

        expect(str(result['status'])).to(equal('confirmed'))
        expect(str(result['summary'])).to(equal('Dinner with friends'))
        expect(str(result['kind'])).to(equal('calendar#event'))

        del_result = self.google_calendar.delete_event(
            result['id'], calendarId=SHARED_CALENDAR_ID)
        expect(del_result).to(equal(''))
