import requests
from bs4 import BeautifulSoup
import json

url = "https://zerazza.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

cat_main = soup.find_all("ul", "ubermenu-row")
category_list = {}

for one_main_cat in cat_main:
    one_sub_cat = one_main_cat.find_all("li", "ubermenu-item")
    for cat in one_sub_cat:
        a = cat.find("a", "ubermenu-target")
        if a is None:
            continue
        cat_url = a.attrs["href"]
        cat_name = cat.find("span", "ubermenu-target-title").text
        category_list[cat_name] = cat_url

temp = {val: key for key, val in category_list.items()}
filter_cat_list = {val: key for key, val in temp.items()}

product_list = []

for i, value in enumerate(filter_cat_list.values()):
    print(f"{value}, {i+1}/{len(filter_cat_list)}")
    if value == '#':
        continue
    next_page = value
    while True:
        response = requests.get(next_page)
        prod_soup = BeautifulSoup(response.text, 'html.parser')
        for prod in prod_soup.find_all("div", "product-small"):
            prod_url = prod.find("a").attrs["href"]
            prod_img_url = prod.find("img").attrs["src"]
            b = prod.find("meta")
            if b is None:
                continue
            prod_id = b.attrs["data-id"]
            prod_name = prod.find("p", "name").text
            prod_price = prod.find("bdi").text.replace("\xa0kr", "")
            product_dict = {"name": prod_name,
                            "price": prod_price,
                            "url": prod_url,
                            "image": prod_img_url,
                            "id": prod_id}
            product_list.append(product_dict)

        c = prod_soup.find("a", "next")
        if c is None:
            break
        next_page = c.attrs["href"]
        print(next_page)

with open("json_file.json", "w", encoding="utf-8") as f:
    json.dump(product_list, f, indent=4, ensure_ascii=False)