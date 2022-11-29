import assistant_details
from speak_module import speak
from database import speak_is_on


def output(o):
    if speak_is_on:
        speak(o)
    print(assistant_details.name + ":" + o)
    print()
