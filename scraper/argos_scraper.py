import requests
from bs4 import BeautifulSoup

def get_argos_deals(search_term):
    url = f"https://www.argos.co.uk/search/{search_term.replace(' ', '-')}/"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    products = []

    for item in soup.select('[data-test=component-product-card]'):
        title = item.select_one('[data-test=component-product-title]').text.strip()
        try:
            price = item.select_one('[data-test=product-card-price]').text.strip()
        except:
            price = "Not available"
        products.append({"title": title, "price": price})

    return products
