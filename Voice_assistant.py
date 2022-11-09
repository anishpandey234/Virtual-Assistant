from calendar_maps_ import *
from basicFuncs import *
from newsAPI import *
from neuralintents import GenericAssistant

def calendarEvents():
    speakEvents(command)

mappings={"get_calendar":calendarEvents,"greetings":greet,"end":end,"news":getTitles,"map":findPlace}    # Format: "intent" : function
assistant=GenericAssistant("intents.json",intent_methods=mappings)
assistant.train_model()
assistant.save_model()
# assistant.load_model()

while True:
    try: 
        command=get_audio()
    except sr.UnknownValueError:
        command=get_audio()
    if command.count("Goodbye")>1:
        end()
    assistant.request(command)



    
    

