import webbrowser
import pyttsx3      # pip3 install pyttsx3
import datetime
import speech_recognition as sr  # pip3 install speechRecognition
import wikipedia  # pip3 install wikipedia
import time
import os
from pygame import mixer
import random

engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
# --- 29(Hindi), 13(English-north) and 11(English)
engine.setProperty('voice', voices[16].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour>=12 and hour<4:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Jarvis Sir.Please tell me how may i help you")


def take_command():
    """ It takes microphone input from the user and string output """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said : {query}")

        except Exception as e:
            # print(e)
            print("Please say that again")
            return "None"

        return query

if __name__ == '__main__':
    wishMe()
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            print("Searching...")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak(results)
            print(results)

        elif 'open youtube' in query:
            webbrowser.open_new_tab("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open_new_tab("https://www.google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open_new_tab("https://stackoverflow.com")

        elif 'play music' in query:
            path_of_song = "/home/mohit/Desktop/Python-program/songs"
            songs = os.listdir(path_of_song)
            # print(songs)
            play_random_songs = random.choice(songs)
            os.chdir(path_of_song)
            mixer.init()
            mixer.music.load(play_random_songs)
            mixer.music.play()
            print("Please say stop to stop the song")
            stop_song = ""
            while stop_song != 'stop':
                stop_song = take_command().lower()
                if 'stop' in stop_song:
                    mixer.music.stop()

        elif 'open visual studio' in query:
            os.system('code .')

        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {str_time}")

        elif 'exit' in query:
            speak("Good bye sir ")
            print("Quiting...Thank you")
            time.sleep(3)
            exit()

