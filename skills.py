import os
import webbrowser
import sys
import subprocess
import pyttsx3





def browser():
    webbrowser.open("C:\Program Files\Google\Chrome\Application\chrome.exe", new = 2)

def pcoff():
    os.system("shutdown /s")

def weather():
    webbrowser.open_new_tab("www.google.com/search?q=weather&oq=weather&aqs=chrome.0.69i59l3j0i131i433i512j0i512l6.4555j1j7&sourceid=chrome&ie=UTF-8")

def botoff():
    sys.exit()

def passive():
    pass

def youtube():
    webbrowser.open_new_tab("www.youtube.com")

