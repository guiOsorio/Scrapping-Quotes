# https://quotes.toscrape.com/
import requests
from random import choice
from bs4 import BeautifulSoup

response = requests.get("https://quotes.toscrape.com")

# for each author, create a dictionary with the author's name as the key, and within that, have 2 keys, "quotes" and "facts".
    # the value for "quotes" should be a list with all the quotes containes in it
    # the value for "facts" should be a list with all the facts about the author
# create game logic and interface

all_quotes = []
authors = []
pagenum = 1

while True:
    soup = BeautifulSoup(response.text, "html.parser")
    quote_divs = soup.select(".quote")
    if len(quote_divs) == 0:
        break
    for div in quote_divs:
        quote = div.select(".text")[0].get_text()
        author = div.select(".author")[0].get_text()
        all_quotes.append(quote)
        authors.append(author)
    pagenum += 1
    response = requests.get(f"https://quotes.toscrape.com/page/{pagenum}")
    break


selected_quote = choice(all_quotes)

print(authors)





