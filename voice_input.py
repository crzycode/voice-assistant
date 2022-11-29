import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
import pyaudio

engine = pyttsx3.init()
engine.setProperty('rate', 120)  # 120 words per minute
engine.setProperty('volume', 0.9)
engine.runAndWait()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
recognizer = sr.Recognizer()


def cmd():
    with sr.Microphone() as source:
        print("Clearing background noises...Pleasw wait")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('Ask me anything..')
        recordedaudio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(recordedaudio, language='en_US')
        text = text.lower()
        return text
        #print('Your message:', format(text))

    except Exception as ex:
        return ex


#while True:
    #cmd()
