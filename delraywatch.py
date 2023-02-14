from listing import Listing
from sites import *
from selenium_options import *

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import itertools
import threading
import time
import sys

done = True


def animate_loading():
    for c in itertools.cycle(["|", "/", "-", "\\"]):
        if done:
            break
        sys.stdout.write(f"\r {c} ")
        sys.stdout.flush()
        time.sleep(0.1)


def get_element(xpath):
    try:
        return driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return None


def scrape_delraywatch():
    listings_delraywatch = []
    global done
    done = False
    t = threading.Thread(target=animate_loading)
    t.daemon = True
    t.start()
    driver.get(SITES["delraywatch"])
    while True:
        delraywatch_products = driver.find_elements(By.XPATH, "//li[@class='product']")
        for li in delraywatch_products:
            title = li.find_element(By.XPATH, ".//h4[@class='card-title']//a").text
            if "Inventory" in title:
                title = title[:-17]
            price = int(
                li.find_element(By.XPATH, ".//span[@class='price price--withoutTax']")
                .text[1:-3]
                .replace(",", "")
            )
            photo = li.find_element(By.TAG_NAME, "img").get_attribute("src")
            url = li.find_element(By.TAG_NAME, "a").get_attribute("href")
            listings_delraywatch.append(
                Listing(title, price, photo, url, "Delray Watch")
            )
        next_link_xpath = "//li[@class='pagination-item pagination-item--next']//a"
        if next_link := get_element(next_link_xpath):
            next_link.click()
            driver.refresh()
        else:
            break
    driver.quit()
    done = True
    return listings_delraywatch
