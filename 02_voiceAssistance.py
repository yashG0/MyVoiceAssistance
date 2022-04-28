
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

def speech2text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recogninzing...")
            data = recognizer.recognize_google(audio)
            print(data)
        except sr.UnknownValueError:
            print("Not Understanding")
            # raise e

def text2speech(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')  
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()


if __name__ == '__main__':
    # speech2text()
    text2speech("Hey guys, this is john let me know your job profile")