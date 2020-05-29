from gtts import gTTS # Google Text To Speech API
import requests

import os
#text = "With an aim to bring down the company’s debt, Reliance Industries Ltd (RIL) has come up with a rights issue offer, through which the conglomerate is planning to raise about ₹53,125 crore. RIL is not the first company to come with rights issue of shares. Read more to know what is a rights issue and should invest in the Reliance Industries’ offer?"
pageSize=5
req = 'http://newsapi.org/v2/top-headlines?pageSize=5&country=in&apiKey=518400c5f1cf4afbbe8097d784b8a8b3'
value = requests.get(url= req)
data = value.json()
language = 'en' # English
title_2 = 'Here is todays headlines.          '
for i in range(pageSize):
    article = data['articles'][i]
    title_1 = article['title']
    title_2 = title_2 + title_1 + '. Next News.         '

title_2 = title_2 + '. Thank you. Have a good day!'
print(title_2)

speech = gTTS(text = title_2, lang=language, slow= False)
speech.save('news_india_29052020.mp3')
os.system("start news_india_29052020.mp3")