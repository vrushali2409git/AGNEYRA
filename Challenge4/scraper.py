import requests
from bs4 import BeautifulSoup
import csv

print("Starting Web Scraper...")

url = "https://quotes.toscrape.com"

response = requests.get(url)

if response.status_code == 200:
    print("Website connected successfully")
else:
    print("Failed to connect")

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

data = []

for q, a in zip(quotes, authors):
    quote = q.text
    author = a.text
    data.append([quote, author])
    print("Quote:", quote)
    print("Author:", author)
    print()

with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])

    for row in data:
        writer.writerow(row)

print("Data saved to quotes.csv successfully")
