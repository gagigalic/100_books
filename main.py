import requests
from bs4 import BeautifulSoup


URL = "https://www.goodreads.com/list/show/2681.Time_Magazine_s_All_Time_100_Novels"

respone = requests.get(URL)
website = respone.text

soup = BeautifulSoup(website, "html.parser")

all_books = soup.find_all(name = "span", itemprop= "name")
print(all_books)

books = [book.getText() for book in all_books]
print(books)

with open("books.txt", mode = "w", encoding="utf8") as file:
        i = 0
        for book in  books:
            i +=1
            file.write(f"{i}. {book}\n")


