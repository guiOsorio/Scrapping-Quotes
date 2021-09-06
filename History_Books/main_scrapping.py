import sqlite3
import requests
from bs4 import BeautifulSoup

# Request URL
response = requests.get("https://books.toscrape.com/catalogue/category/books/history_32/index.html")

# Initialize BS
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article")

# Extract data we want
all_books = []
for book in books:
    title = book.select("h3 > a")[0]["title"]
    price = book.select(".price_color")[0].get_text()
    price = float(price.replace("£","").replace("Â",""))
    ratings = {"Zero": 0, "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    paragraph = book.select(".star-rating")[0]
    rating = paragraph.get_attribute_list("class")[-1]
    int_rating = ratings[rating]
    new_book = (title, price, int_rating)
    all_books.append(new_book)

# Save data to database
connection = sqlite3.connect("books.db")
c = connection.cursor()
c.execute('''CREATE TABLE books
            (title TEXT, price REAL, rating INTEGER);''')
c.executemany("INSERT INTO books VALUES(?,?,?);", all_books)
connection.commit()
connection.close()