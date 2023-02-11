# Chrono Crawler

<p align="left">
<img src="https://img.shields.io/github/languages/top/christopherlam888/chrono-crawler.svg" >
<a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://www.gnu.org/licenses/gpl-3.0" alt="License: GPLv3"><img src="https://img.shields.io/badge/License-GPL%20v3-blue.svg"></a>
</p>

A web scraper to get listings from popular vintage and pre-owned watch retailers.

## Features

- Scrape hundreds of listings from different vintage and pre-owned watch retail sites
- Faster scraping with multithreading
- Get listings by site
- Search for listings contatining a search term
- Sort listings by price (low to high)
- Open listings in-browser

## Supported Sites

- Theo and Harris: <https://theoandharris.com/vintage-watches/>
- Delray Watch: <https://www.delraywatch.com/collections/pre-owned-watches/>
- Omega Enthusiast: <https://www.omegaenthusiastltd.com/shop-all/>

## Installation

Clone/Download the GitHub repository:

```git clone https://github.com/christopherlam888/chrono-crawler.git```

Navigate to the directory:

```cd chrono-crawler```

Install requirements:

```pip3 install -r requirements.txt```

Chrono Crawler uses Selenium with the Chrome WebDriver. Install Chrome/Chromium before using.

## Usage

| **Command**                                   | **Description**                                                |
| :-------------------------------------------- | :------------------------------------------------------------- |
| `python3  chrono_crawler.py`                  | Run Chrono Crawler with defaults (all sites)                   |
| `python3  chrono_crawler.py -t`               | Get listings from Theo and Harris                              |
| `python3  chrono_crawler.py -d`               | Get listings from Delray Watch                                 |
| `python3  chrono_crawler.py -o`               | Get listings from Omega Enthusiast                             |
| `python3  chrono_crawler.py -s [search]`      | Search for listings containing a search term                   |
| `python3  chrono_crawler.py -p`               | Sort listings by price (low to high)                           |
| `python3  chrono_crawler.py -h`               | Show help message.                                             |

## Screenshots

![1](https://user-images.githubusercontent.com/85356197/218275115-304fc5f7-e13b-4312-846a-509c296b63ab.png)
![2](https://user-images.githubusercontent.com/85356197/218275144-73d28850-6e21-4f13-a351-47971e253a40.png)

## Features To Implement

- Add more websites

## License
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](https://www.gnu.org/licenses/gpl-3.0.en.html)  

This project is licensed under the GNU General Public License v3.0.
