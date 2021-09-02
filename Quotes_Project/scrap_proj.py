# https://quotes.toscrape.com/
import requests
from random import choice
# from csv import writer
from bs4 import BeautifulSoup

response = requests.get("https://quotes.toscrape.com")

# add author facts - from each author's about page
# create game logic and interface

all_quotes = []
pagenum = 1

while True:
    soup = BeautifulSoup(response.text, "html.parser")
    quote_divs = soup.select(".quote")
    if len(quote_divs) == 0:
        break
    for div in quote_divs:
        quote = div.select(".text")[0].get_text()
        author = div.select(".author")[0].get_text()
        all_quotes.append([quote, author])
    pagenum += 1
    response = requests.get(f"https://quotes.toscrape.com/page/{pagenum}")

# with open("quotes_data.csv", "w", newline="", encoding="utf-8") as csv_file:
#     csv_writer = writer(csv_file)
#     csv_writer.writerow(["quote", "author"])
#     for quote in all_quotes:
#         # Text
#         text = quote[0]
#         # Author
#         author = quote[1]
#         csv_writer.writerow([text, author])

selected_quote_div = choice(all_quotes)
selected_quote = selected_quote_div[0]
selected_author = selected_quote_div[1]





