import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate",130)
    engine.say(text)
    engine.runAndWait()


def get_audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
    try:
        return (r.recognize_google(audio))
    except LookupError or Exception:
        return ("I'm sorry. I could not understand you")
