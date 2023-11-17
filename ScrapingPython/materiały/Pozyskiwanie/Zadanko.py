import requests
from bs4 import BeautifulSoup
import time

quotes_url = "https://www.brainyquote.com/topics/page-quotes"
response = requests.get(quotes_url)
soup = BeautifulSoup(response.text, 'html.parser')

quotes_list = []
for i in range(2):
    for quote in soup.find_all("div", class_="bqQt"):
        time.sleep(0.5)

        single_quote = dict()

        single_quote["text"] = quote.find("a", class_="b-qt").text.strip()

        single_quote["author"] = quote.find("a", class_="bq-aut").text

        subpage_link = "https://www.brainyquote.com" + quote.find("a", "b-qt")["href"]

        subpage_soup = BeautifulSoup(requests.get(subpage_link).text, 'html.parser')
        tags_list = subpage_soup.find("div", "kw-box")
        tags_texts = [t.text for t in tags_list.find_all("a")]

        single_quote["tags"] = tags_texts

        quotes_list.append(single_quote)

    next_page_url = quotes_url + f"_{i + 2}"
    response = requests.get(next_page_url)
    soup = BeautifulSoup(response.text, 'html.parser')

print(quotes_list)
