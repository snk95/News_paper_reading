import json
import requests

def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("News for today")
    url="http://newsapi.org/v2/top-headlines?country=in&apiKey=db76addb8e384923bf1b31f0a9a0b81f"
    news=requests.get(url).text
    news_dict=json.loads(news)
    print(news_dict["articles"])
    arts= news_dict['articles']
    for article in arts:
        speak(article['title'])
        speak("Moving on to next news....Listen carefully")
    speak("Thanks for listening")
