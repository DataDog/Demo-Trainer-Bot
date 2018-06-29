from googleapiclient import discovery
from google.oauth2.service_account import Credentials
from google.auth.transport.requests import AuthorizedSession


class Calendar:
    def __init__(self, credentials_file):
        self.SCOPES = ['https://www.googleapis.com/auth/calendar']
        self.credentials = credentials = Credentials.from_service_account_file(
            credentials_file,
            scopes=self.SCOPES
        )
        self.service = discovery.build('calendar', 'v3', credentials=credentials)

    def create_event(self, event_details):
        result = self.service.events().insert(calendarId='primary', body=event_details).execute()
        print('Event Created: {}'.format(result.get('htmlLink')))
        return result
        

    def delete_event(self, eventId, calendarId='primary'):
        result = self.service.events().delete(calendarId=calendarId, eventId=eventId).execute()
        print('Event {} deleted'.format(eventId))
        return result