from textblob import TextBlob
from newspaper import Article
from bs4 import BeautifulSoup

with open('storytime.txt', 'r') as f:
    text = f.read()

blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)