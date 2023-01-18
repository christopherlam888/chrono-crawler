from listing import Listing

import argparse

import requests
from requests import get
from bs4 import BeautifulSoup

import multiprocessing
import tqdm
import sys
sys.setrecursionlimit(10000)

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
    parser.add_argument('-t', '--theoandharris', dest='theoandharris', action='store_true')
    parser.add_argument('-d', '--delraywatch', dest='delraywatch', action='store_true')
    parser.add_argument('-o', '--omegaenthusiast', dest='omegaenthusiast', action='store_true')
    parser.add_argument('-s', '--search', dest='search')
    parser.add_argument('-p', '--price', dest='price', action='store_true')
    args = vars(parser.parse_args())
    return args

headers = {"Accept-Language": "en-US, en;q=0.5"}

def scrape_delraywatch(page):
    listings_delraywatch = []
    delraywatch_results = requests.get(page, headers = headers)
    delraywatch_soup = BeautifulSoup(delraywatch_results.text, "html.parser")
    delraywatch_products = delraywatch_soup.find_all('li', class_='product')
    for li in delraywatch_products:
        title = li.find('h4', class_='card-title').a.text
        if "Inventory" in title:
            title = title[:-17]
        price = int(li.find('span', class_='price price--withoutTax').text[1:-3].replace(",",""))
        photohtml = li.find('img')
        urlhtml = li.find('a')
        listings_delraywatch.append(Listing(title, price, photohtml['src'], urlhtml['href'], "Delray Watch"))
    return listings_delraywatch

def omegaenthusiast_check_page(omegaenthusiast, counter):
    omegaenthusiast_results = requests.get(omegaenthusiast+str(counter), headers = headers)
    omegaenthusiast_soup = BeautifulSoup(omegaenthusiast_results.text, "html.parser")
    omegaenthusiast_list = omegaenthusiast_soup.find('ul', class_='S4WbK_ c2Zj9x')
    return bool(omegaenthusiast_list.find('li'))

def scrape_omegaenthusiast(page):
    listings_omegaenthusiast = []
    omegaenthusiast_results = requests.get(page, headers = headers)
    omegaenthusiast_soup = BeautifulSoup(omegaenthusiast_results.text, "html.parser")
    omegaenthusiast_list = omegaenthusiast_soup.find('ul', class_='S4WbK_ c2Zj9x')
    omegaenthusiast_products = omegaenthusiast_list.find_all('li')
    for li in omegaenthusiast_products:
        if li.find('span', class_='cfpn1d'):
            title = li.find('h3', class_='syQOIUy okvj6QX---typography-11-runningText okvj6QX---priority-7-primary syHtuvM FzO_a9').text
            price = int(li.find('span', class_='cfpn1d').text[1:-3].replace(",",""))
            photohtml_wrapper = li.find('div', class_='naMHY_ vALCqq')
            photohtml = photohtml_wrapper.find('img')
            urlhtml = li.find('a')
            listings_omegaenthusiast.append(Listing(title, price, photohtml['src'].replace("blur_2,","").replace("w_110,h_107","w_155,h_155"), urlhtml['href'], "Omega Enthusiast"))
    return listings_omegaenthusiast

def main():

    # draw text
    draw_text()

    theoandharris_selected = False
    delraywatch_selected = False
    omegaenthusiast_selected = False

    # parse arguments
    args = parse_args()
    if args['theoandharris']:
        theoandharris_selected = True
    if args['delraywatch']:
        delraywatch_selected = True
    if args['omegaenthusiast']:
        omegaenthusiast_selected = True
    if not args['theoandharris'] and not args['delraywatch'] and not args['omegaenthusiast']:
        theoandharris_selected = True
        delraywatch_selected = True
        omegaenthusiast_selected = True

    listings = []

    # scrape theoandharris
    if theoandharris_selected:
        print("Scraping Theo and Harris...")
        theoandharris = "https://theoandharris.com/vintage-watches/"
        theoandharris_results = requests.get(theoandharris, headers=headers)
        theoandharris_soup = BeautifulSoup(theoandharris_results.text, "html.parser")
        theoandharris_list = theoandharris_soup.find('ul', class_='columns-4')
        theoandharris_products = theoandharris_list.find_all('li', class_='product')
        for li in theoandharris_products:
            title = li.find('h2', class_='woocommerce-loop-product__title').text
            price = int(li.find('bdi').text[1:-4].replace(",",""))
            photohtml = li.find('img')
            urlhtml = li.find('a')
            listings.append(Listing(title, price, photohtml['src'], urlhtml['href'], "Theo and Harris"))
        print("Theo and Harris scraped.")

    # scrape delraywatch
    if delraywatch_selected:
        print("Scraping Delray Watch...")
        delraywatch = "https://delraywatch.com/pre-owned-watches/"
        delraywatch_results = requests.get(delraywatch, headers = headers)
        delraywatch_soup = BeautifulSoup(delraywatch_results.text, "html.parser")
        delraywatch_anchors = delraywatch_soup.find_all('a', class_='pagination-link')
        delraywatch_pages = []
        for a in delraywatch_anchors:
            delraywatch_pages.append(delraywatch + a['href'][19:])
        with multiprocessing.Pool() as pool, tqdm.tqdm(total=len(delraywatch_pages)) as pbar:
            for listings_delraywatch in pool.imap_unordered(scrape_delraywatch, delraywatch_pages):
                listings.extend(listings_delraywatch)
                pbar.update()
        print("Delray Watch scraped.")

    # scrape omegaenthusiast
    if omegaenthusiast_selected:
        print("Scraping Omega Enthusiast...")
        omegaenthusiast = "https://www.omegaenthusiastltd.com/shop-all?page="
        
        # check pages
        omegaenthusiast_pages = []
        with multiprocessing.Pool(8) as pool:
            INTERVAL = 8
            counter = 1
            while True:
                params = [(omegaenthusiast, counter) for counter in range(counter, counter+INTERVAL)]
                res = pool.starmap(omegaenthusiast_check_page, params)
                for i, output in enumerate(res):
                    if output:
                        omegaenthusiast_pages.append(f"{omegaenthusiast}{counter+i}")
                if not all(res):
                    break
                counter += INTERVAL
        
        # scrape pages
        with multiprocessing.Pool(8) as pool, tqdm.tqdm(total=len(omegaenthusiast_pages)) as pbar:
            for listings_omegaenthusiast in pool.imap_unordered(scrape_omegaenthusiast, omegaenthusiast_pages):
                listings.extend(listings_omegaenthusiast)
                pbar.update()
        print("Omega Enthusiast scraped.")

    # search
    if args['search']:
        search = args['search'].strip().lower()
        listings = list(filter(lambda listing: search in listing.title.lower(), listings))

    # price sort
    if args['price']:
        listings.sort(key=lambda listing: listing.price)

    # print table
    print()
    print("{:<5} {:<120} {:<10} {:<20}".format("Item", "Title", "Price", "Store"))
    for i in range(len(listings)):
        print("{:<5} {:<120} {:<10} {:<20}".format(i, listings[i].title, "$" + '{:,}'.format(listings[i].price), listings[i].store))

    # browsing
    browsing = True
    while browsing:
        selection = input("Browsing...Enter an item number: ")
        if selection.isdigit() and int(selection) >= 0 and int(selection) < len(listings):
            print(f"Photo:\n{listings[int(selection)].photo}")
            print(f"URL:\n{listings[int(selection)].url}")
        else:
            browsing = False

if __name__ == "__main__":
    main()
