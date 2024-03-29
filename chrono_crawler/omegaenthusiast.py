from .listing import Listing
from .sites import *
from .beautifulsoup_options import *

import requests
from bs4 import BeautifulSoup


def omegaenthusiast_check_page(counter):
    omegaenthusiast_results = requests.get(
        SITES["omegaenthusiast"] + str(counter), headers=headers
    )
    omegaenthusiast_soup = BeautifulSoup(omegaenthusiast_results.text, "html.parser")
    omegaenthusiast_list = omegaenthusiast_soup.find(
        "ul", attrs={"data-hook": "product-list-wrapper"}
    )
    return bool(omegaenthusiast_list.find("li"))


def scrape_omegaenthusiast(page):
    listings_omegaenthusiast = []
    omegaenthusiast_results = requests.get(page, headers=headers)
    omegaenthusiast_soup = BeautifulSoup(omegaenthusiast_results.text, "html.parser")
    omegaenthusiast_list = omegaenthusiast_soup.find(
        "ul", attrs={"data-hook": "product-list-wrapper"}
    )
    omegaenthusiast_products = omegaenthusiast_list.find_all("li")
    for li in omegaenthusiast_products:
        if li.find("span", attrs={"data-hook": "product-item-price-to-pay"}):
            title = li.find(
                "h3",
                attrs={"data-hook": "product-item-name"},
            ).text
            price = int(
                li.find("span", attrs={"data-hook": "product-item-price-to-pay"})
                .text[1:-3]
                .replace(",", "")
            )
            photohtml_wrapper = li.find("div", class_="naMHY_ vALCqq")
            photohtml = photohtml_wrapper.find("img")
            urlhtml = li.find("a")
            listings_omegaenthusiast.append(
                Listing(
                    title,
                    price,
                    photohtml["src"]
                    .replace("blur_2,", "")
                    .replace("w_110,h_107", "w_154,h_154"),
                    urlhtml["href"],
                    "Omega Enthusiast",
                )
            )
    return listings_omegaenthusiast
