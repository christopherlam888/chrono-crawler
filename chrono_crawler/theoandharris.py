from .listing import Listing
from .sites import *
from .beautifulsoup_options import *

import requests
from bs4 import BeautifulSoup


def scrape_theoandharris():
    listings_theoandharris = []
    theoandharris_results = requests.get(SITES["theoandharris"], headers=headers)
    theoandharris_soup = BeautifulSoup(theoandharris_results.text, "html.parser")
    theoandharris_list = theoandharris_soup.find("ul", class_="columns-4")
    theoandharris_products = theoandharris_list.find_all("li", class_="product")
    for li in theoandharris_products:
        title = li.find("h2", class_="woocommerce-loop-product__title").text
        price = int(li.find("bdi").text[1:-4].replace(",", ""))
        photohtml = li.find("img")
        urlhtml = li.find("a")
        listings_theoandharris.append(
            Listing(title, price, photohtml["src"], urlhtml["href"], "Theo and Harris")
        )
    return listings_theoandharris
