from calendarAPI import *
from basicFuncs import *
from neuralintents import GenericAssistant

def calendarEvents():
    speakEvents(command)

mappings={"get_calendar":calendarEvents,"greetings":greet,"end":end}  # Format: "intent" : function
assistant=GenericAssistant("intents.json",intent_methods=mappings)
assistant.load_model()

while True:
    try: 
        command=get_audio()
    except sr.UnknownValueError:
        command=get_audio()
    if command.count("Goodbye")>1:
        end()
    assistant.request(command)


    
    

