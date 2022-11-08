from __future__ import print_function
from datetime import datetime, timedelta
import datefinder
from dateutil.parser import *
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os
import pytz
from speak import *

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def authenticate():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    
    service = build('calendar', 'v3', credentials=creds)
    return service

# service: service just passed in authenticate
def get_events(date,service):
        # Call the Calendar API
        utc=pytz.UTC
        date = date.astimezone(utc)
        tomorrow = date+timedelta(1)
        tomorrow = tomorrow.astimezone(utc)
        
        events_result = service.events().list(calendarId='primary', timeMin=date.isoformat(), timeMax=tomorrow.isoformat(),
                                               singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            speak('No events found on that day.')
            return
        else:
            speak(f'("You have {len(events)} events on this day.')
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                splitTime = str(start.split("T")[1])  # Splits 2022-11-01T10:00:00-04:00 into ['2022-11-01', '10:00:00-04:00'], goes to index 1: Time
                startTime = splitTime.split("-")[0][:-3] # Turns it into 10:00 
                if int(startTime.split(":")[0])<12:
                    startTime+=" am"
                else:
                    hour=str(int(startTime[:2])-12) 
                    startTime=(hour + startTime[2::] + "pm")
                speak((event['summary'] + " at " + startTime))


calendarPrompts=["what do i have ", "what do i need to do on", "do i have anything on", "am I busy on",]

def get_date(text):
    matches = list(datefinder.find_dates(text))

    if len(matches) > 0:
    # date returned will be a datetime.datetime object. here we are only using the first match.
        date = matches[0]
        return(date)
    
    # still have to implement edge case: NEXT sunday, THIS thursday
    # only works with specific dates (Sept 2nd, Dec 1st, etc)

service=authenticate()

def speakEvents(command):
    date=get_date(command)
    if date:
        get_events(date,service)
    else:
        speak("Sorry. Please try again.")




# for prompt in calendarPrompts:
#     if prompt in command.lower():
#         date=get_date(command)
#         if date:
#             get_events(date,service)
#         else:
#             speak("Sorry. Please try again.")