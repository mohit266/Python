import pyttsx3
import requests
import json


engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[16].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


if __name__ == '__main__':
    speak('hello mohit')
    url = "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey= Enter your api key"
    news = requests.get(url).text
    news = json.loads(news)
    # print(news["articles"])
    arts = news["articles"]
    for headline in arts:
        speak(headline['title'])
        print(headline['title'])
    speak("Thanks for listening")