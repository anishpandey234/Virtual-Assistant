import os
from speak import speak
from newsapi import NewsApiClient
from dotenv import load_dotenv  # to load env variable (API)

load_dotenv()
api=os.environ.get("api")
newsapi=NewsApiClient(api_key=api)

top_headlines = newsapi.get_top_headlines(sources="bbc-news,the-verge,cnn",language="en")

# print(top_headlines)
articles=top_headlines.get('articles')
def getTitles():
    speak("The top five articles from today are: ")
    for i in range(5):
        title=articles[i].get('title')
        print(title)
        speak(title)


