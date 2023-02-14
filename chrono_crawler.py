from sites import *
from parse_args import *
from theoandharris import *
from delraywatch import *
from omegaenthusiast import *

import multiprocessing.dummy as multiprocessing
import tqdm
import sys
from tabulate import tabulate

sys.setrecursionlimit(10000)
import webbrowser


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
        listings.extend(scrape_theoandharris())
        print("Theo and Harris scraped.")

    # scrape delraywatch
    if args["delraywatch"]:
        print("Scraping Delray Watch...")
        listings.extend(scrape_delraywatch())
        print()
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
    listings_display = []
    for i, listing in enumerate(listings):
        listings_display.append(
            [i, listing.title, f"${listing.price:,}", listing.store]
        )
    print()
    print(
        tabulate(
            listings_display,
            headers=["Item", "Title", "Price", "Store"],
            tablefmt="fancy_grid",
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
