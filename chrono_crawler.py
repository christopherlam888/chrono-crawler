from listing import Listing

import argparse

import requests
from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import multiprocessing.dummy as multiprocessing
import tqdm
import sys

sys.setrecursionlimit(10000)
import webbrowser

SITES = {
    "theoandharris": "https://theoandharris.com/vintage-watches/",
    "delraywatch": "https://www.delraywatch.com/collections/pre-owned-watches",
    "omegaenthusiast": "https://www.omegaenthusiastltd.com/shop-all?page=",
}


def draw_text():
    print(" ____  ____  ____  ____  ____  ____ ")
    print("||C ||||H ||||R ||||O ||||N ||||O ||")
    print("||__||||__||||__||||__||||__||||__||")
    print("|/__\||/__\||/__\||/__\||/__\||/__\|")
    print(" ____  ____  ____  ____  ____  ____  ____ ")
    print("||C ||||R ||||A ||||W ||||L ||||E ||||R ||")
    print("||__||||__||||__||||__||||__||||__||||__||")
    print("|/__\||/__\||/__\||/__\||/__\||/__\||/__\|")
    print()


def parse_args():
    parser = argparse.ArgumentParser(description="Available Options")
    for key in SITES:
        parser.add_argument(f"-{key[0]}", f"--{key}", dest=key, action="store_true")
    parser.add_argument("-s", "--search", dest="search")
    parser.add_argument("-p", "--price", dest="price", action="store_true")
    args = vars(parser.parse_args())
    return args


headers = {"Accept-Language": "en-US, en;q=0.5"}
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)


def get_element(xpath):
    try:
        return driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return None


def omegaenthusiast_check_page(counter):
    omegaenthusiast_results = requests.get(
        SITES["omegaenthusiast"] + str(counter), headers=headers
    )
    omegaenthusiast_soup = BeautifulSoup(omegaenthusiast_results.text, "html.parser")
    omegaenthusiast_list = omegaenthusiast_soup.find("ul", class_="S4WbK_")
    return bool(omegaenthusiast_list.find("li"))


def scrape_omegaenthusiast(page):
    listings_omegaenthusiast = []
    omegaenthusiast_results = requests.get(page, headers=headers)
    omegaenthusiast_soup = BeautifulSoup(omegaenthusiast_results.text, "html.parser")
    omegaenthusiast_list = omegaenthusiast_soup.find("ul", class_="S4WbK_")
    omegaenthusiast_products = omegaenthusiast_list.find_all("li")
    for li in omegaenthusiast_products:
        if li.find("span", class_="cfpn1d"):
            title = li.find(
                "h3",
                class_="syQOIUy okvj6QX---typography-11-runningText okvj6QX---priority-7-primary syHtuvM FzO_a9",
            ).text
            price = int(li.find("span", class_="cfpn1d").text[1:-3].replace(",", ""))
            photohtml_wrapper = li.find("div", class_="naMHY_ vALCqq")
            photohtml = photohtml_wrapper.find("img")
            urlhtml = li.find("a")
            listings_omegaenthusiast.append(
                Listing(
                    title,
                    price,
                    photohtml["src"]
                    .replace("blur_2,", "")
                    .replace("w_110,h_107", "w_155,h_155"),
                    urlhtml["href"],
                    "Omega Enthusiast",
                )
            )
    return listings_omegaenthusiast


def main():
    # draw text
    draw_text()

    # parse arguments
    args = parse_args()
    all_selected = not any(args[key] for key in SITES)
    for key in SITES:
        args[key] = args[key] or all_selected

    listings = []

    # scrape theoandharris
    if args["theoandharris"]:
        print("Scraping Theo and Harris...")
        theoandharris_results = requests.get(SITES["theoandharris"], headers=headers)
        theoandharris_soup = BeautifulSoup(theoandharris_results.text, "html.parser")
        theoandharris_list = theoandharris_soup.find("ul", class_="columns-4")
        theoandharris_products = theoandharris_list.find_all("li", class_="product")
        for li in theoandharris_products:
            title = li.find("h2", class_="woocommerce-loop-product__title").text
            price = int(li.find("bdi").text[1:-4].replace(",", ""))
            photohtml = li.find("img")
            urlhtml = li.find("a")
            listings.append(
                Listing(
                    title, price, photohtml["src"], urlhtml["href"], "Theo and Harris"
                )
            )
        print("Theo and Harris scraped.")

    # scrape delraywatch
    if args["delraywatch"]:
        print("Scraping Delray Watch...")
        driver.get(SITES["delraywatch"])
        while True:
            delraywatch_products = driver.find_elements(
                By.XPATH, "//li[@class='product']"
            )
            for li in delraywatch_products:
                title = li.find_element(By.XPATH, ".//h4[@class='card-title']//a").text
                if "Inventory" in title:
                    title = title[:-17]
                price = int(
                    li.find_element(
                        By.XPATH, ".//span[@class='price price--withoutTax']"
                    )
                    .text[1:-3]
                    .replace(",", "")
                )
                photo = li.find_element(By.TAG_NAME, "img").get_attribute("src")
                url = li.find_element(By.TAG_NAME, "a").get_attribute("href")
                listings.append(Listing(title, price, photo, url, "Delray Watch"))
            next_link_xpath = "//li[@class='pagination-item pagination-item--next']//a"
            if next_link := get_element(next_link_xpath):
                next_link.click()
                driver.refresh()
            else:
                break
        driver.quit()
        print("Delray Watch scraped.")

    # scrape omegaenthusiast
    if args["omegaenthusiast"]:
        print("Scraping Omega Enthusiast...")

        # check pages
        omegaenthusiast_pages = []
        with multiprocessing.Pool(8) as pool:
            INTERVAL = 8
            counter = 1
            while True:
                params = [(counter,) for counter in range(counter, counter + INTERVAL)]
                res = pool.starmap(omegaenthusiast_check_page, params)
                for i, output in enumerate(res):
                    if output:
                        omegaenthusiast_pages.append(
                            f"{SITES['omegaenthusiast']}{counter+i}"
                        )
                if not all(res):
                    break
                counter += INTERVAL

        # scrape pages
        with multiprocessing.Pool(8) as pool, tqdm.tqdm(
            total=len(omegaenthusiast_pages)
        ) as pbar:
            for listings_omegaenthusiast in pool.imap_unordered(
                scrape_omegaenthusiast, omegaenthusiast_pages
            ):
                listings.extend(listings_omegaenthusiast)
                pbar.update()
        print("Omega Enthusiast scraped.")

    # search
    if args["search"]:
        search = args["search"].strip().lower()
        listings = [listing for listing in listings if search in listing.title.lower()]

    # price sort
    if args["price"]:
        listings.sort()

    # print table
    print()
    print("{:<5} {:<120} {:<10} {:<20}".format("Item", "Title", "Price", "Store"))
    for i, listing in enumerate(listings):
        print(
            "{:<5} {:<120} {:<10} {:<20}".format(
                i, listing.title, f"${listing.price:,}", listing.store
            )
        )

    # browsing
    while True:
        try:
            selection = int(input("Browsing...Enter an item number: "))
            if 0 <= selection < len(listings):
                print(f"Photo:\n{listings[selection].photo}")
                print(f"URL:\n{listings[selection].url}")
                webbrowser.open(listings[selection].url, new=2)
        except ValueError:
            break


if __name__ == "__main__":
    main()
