import pyttsx3
import speech_recognition as sr

def speak(text):
    speaker = pyttsx3.init()
    speaker.setProperty("rate",130)
    speaker.say(text)
    speaker.runAndWait()


def get_audio():
    print("Now recording")
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source,phrase_time_limit=7)
    try:
        test = (r.recognize_google(audio))
        return test.lower()
    except LookupError or Exception or sr.UnknownValueError:
        return ("I'm sorry. I could not understand you")
