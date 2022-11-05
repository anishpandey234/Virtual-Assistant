from calendarAPI import *
import datefinder

# 
def get_date(text):
    # today=date.today()
    matches = list(datefinder.find_dates(text))

    if len(matches) > 0:
    # date returned will be a datetime.datetime object. here we are only using the first match.
        date = matches[0]
        return(date)
    
    # still have to implement edge case: NEXT sunday, THIS thursday
    # only works with specific dates (Sept 2nd, Dec 1st, etc)

calendarPrompts=["what do i have ", "what do i need to do on", "do i have anything on", "am I busy on",]

service=authenticate()
command=get_audio()

for prompt in calendarPrompts:
    if prompt in command.lower():
        date=get_date(command)
        if date:
            get_events(date,service)
        else:
            speak("Sorry. Please try again.")

    
    

