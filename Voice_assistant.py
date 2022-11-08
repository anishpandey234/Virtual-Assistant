from calendarAPI import *
from basicFuncs import *
from neuralintents import GenericAssistant

command=get_audio()
mappings={"get_calendar":speakEvents(command),"greetings":greet()}  # Format: "intent" : function
assistant=GenericAssistant("intents.json",intent_methods=mappings)
assistant.train_model()
assistant.save_model()


# assistant.request(command)

# calendarPrompts=["what do i have ", "what do i need to do on", "do i have anything on", "am I busy on",]

# for prompt in calendarPrompts:
#     if prompt in command.lower():
#         date=get_date(command)
#         if date:
#             get_events(date,service)
#         else:
#             speak("Sorry. Please try again.")

    
    

