import requests
from bs4 import BeautifulSoup

genres_urls = {"Philosophy": "https://books.toscrape.com/catalogue/category/books/philosophy_7/",
               "Music": "https://books.toscrape.com/catalogue/category/books/music_14/",
               "Autobiography": "https://books.toscrape.com/catalogue/category/books/autobiography_27/"}

books_dict = dict()
for genre in genres_urls:
    response = requests.get(genres_urls[genre])
    soup = BeautifulSoup(response.text, 'html.parser')
    books_dict[genre] = []

    all_books = soup.find_all("li", class_="col-xs-6")
    for book in all_books:
        book_href = book.find("a").attrs["href"]
        book_url = genres_urls[genre] + book_href

        response = requests.get(book_url)
        book_soup = BeautifulSoup(response.text, 'html.parser')

        title = book_soup.find("h1").text
        price = float(book_soup.find("p", class_="price_color").text.replace("£", "").replace("Â", ""))

        rating_raw = book_soup.find("p", class_="star-rating").attrs["class"][1]
        rating_dict = {"Five": 5, "Four": 4, "Three": 3, "Two": 2, "One": 1}
        rating = rating_dict[rating_raw]

        upc = book_soup.find("td").text

        books_dict[genre].append({"title": title, "price": price, "rating": rating, "UPC": upc})

print(books_dict)
