

# https://datamahadev.com/10-amazing-python-hacks-with-cool-libraries/


import datetime
import speech_recognition as speech
import pyttsx3
import pywhatkit
import pyautogui

import os
import subprocess as sp


# Import module
import wmi
  


os_paths = {
    'vsCode': "C:\\Users\\godsw\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    'brave': "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe",
    'ps': "C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\Photoshop.exe"
}

listener = speech.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# engine.setProperty('rate', 190)


def speak(command):
    engine.say(command)
    engine.runAndWait()

def takeCommand():

    try:
        with speech.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            print("listening...")
            speak("Hi, How can i help you?")
            
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "dude" in command:
                command = command.replace("dude", "")
                run(command)
                # print(command)

            # if 'ogbeni'
            else:
                speak("Sorry i didn't understand that.")

    except:
        speak("i encountered an error, please check my logs")
        pass
    # return command

def run(command):
    # command = takeCommand()
    print(command)
    if 'play' in command:
        playSongOnYt(command)

    if 'photoshop' in command:
        openPhotoshop()

    if 'vs code' in command:
        openVSCode()

    if 'browser' in command:
        openBraveBrowser()

    if 'remote control' in command:
        startMobileRemoteAcess()

    if 'the time' in command:
        tellTime()

    if 'hibernate' in command:
        hibernatePc()

def tellTime():
    time = datetime.datetime.now().strftime('%I:%M:%p')
    speak('current time is '+time)

def startMobileRemoteAcess():
    pywhatkit.start_server()
    # run ipconfig in cmd to get the local ip of your pc and then visit local_ip:8000 in 
    # your phone. ensure your pc and phone is connected to the same network.

def openBraveBrowser():
    os.startfile(os_paths["brave"])

def openVSCode():
    os.startfile(os_paths["vsCode"])

def openPhotoshop():
    os.startfile(os_paths["ps"])

def playSongOnYt(command):
    song = command.replace("play", "")
    speak('playing '+song)
    pywhatkit.playonyt(song)

def hibernatePc():
    speak('hibernating in 1 minute')
    os.system("shutdown /h")
        
while True:
    takeCommand()
