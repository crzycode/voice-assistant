from input_module import take_input
from process_module import process
from output_module import output
import welcome
import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
import pyaudio

welcome.greats()

while (True):
    i = take_input()
    o = process(i)
    output(o)
