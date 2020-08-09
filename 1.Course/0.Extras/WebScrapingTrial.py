import requests
import bs4
import lxml
value = requests.get('http://www.example.com')

#print(value.text)

text_val = value.text

bs4_text = bs4.BeautifulSoup(text_val)

#print(bs4_text)

title = bs4_text.select('title')[0]

title.getText()

print(title.getText())