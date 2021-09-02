 # https://www.rithmschool.com/blog
import requests
from csv import writer
from bs4 import BeautifulSoup

response = requests.get("https://www.rithmschool.com/blog")

soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")

with open("blog_data.csv", "w", newline="") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title", "link", "date"])
    for article in articles:
        # Title
        title = article.find("a").get_text()
        # Date
        date = article.select(".card")[0].find("time")["datetime"][:10]
        # href
        url = article.select(".section-heading")[0].find("a")["href"]
        csv_writer.writerow([title, url, date])