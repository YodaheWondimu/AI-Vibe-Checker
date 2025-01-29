# You know it, you love it, or maybe you don't! This AI can tell the difference! Just by reading a given text, it can detect the sentiment involved and tell you waht it is - whether it's positive, negative or neutral.

How can a computer understand the general feeling of the text? The comptuer never felt feeling before. This is true, but what's also true is the fact that, it doesn't need to! Think of the word "happy." Maybe to you it's a bowl of ice cream or a relaxing day at the spa. Now think of the word "sad." You might think of dropping your ice cream or having a bad day. Each of these words have connotations - sentiments - to them, and the AI is able to understand these - and how you feel.

The program starts with importing necessary libraries - essential for making the program be what it is.
```
from textblob import TextBlob
from newspaper import Article
from bs4 import BeautifulSoup
```
These are used later when it's time to format the text and process its sentiment. No books, but still useful libraries.
```
with open('storytime.txt', 'r') as f:
    text = f.read()
```
'Tis code that lets the program read the text file - storytime.txt! In this text file, you may have a certain document where you explain how your day went or a newspaper article about a certain environmental topic. It is then able to take the text file and read it, a skim-through so that it knows what's inside.
```
blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)
```
This is the big idea of the code - it can save the code as a processable "blob" that is then run through a function that goes through tokenization (taking each word individually, studying its relationships with surrounding words, and using these combined to make a prediction) in order to study the feeling of the text. Now you know how it works - go check your vibe today!
- Yodahe Wondimu, Computer Scientist
