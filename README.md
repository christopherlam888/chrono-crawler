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
- Search for listings containing a search term
- Sort listings by price (low to high)
- Download images from listings
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
| `python3 -m chrono_crawler`                   | Run Chrono Crawler with defaults (all sites)                   |
| `python3 -m chrono_crawler -t`                | Get listings from Theo and Harris                              |
| `python3 -m chrono_crawler -d`                | Get listings from Delray Watch                                 |
| `python3 -m chrono_crawler -o`                | Get listings from Omega Enthusiast                             |
| `python3 -m chrono_crawler -s [search]`       | Search for listings containing a search term                   |
| `python3 -m chrono_crawler -p`                | Sort listings by price (low to high)                           |
| `python3 -m chrono_crawler -i`                | Download images from listings                                  |
| `python3 -m chrono_crawler -h`                | Show help message                                              |

## Screenshots

![1](https://user-images.githubusercontent.com/85356197/218775400-4f1a8065-8cbd-43b2-be1e-ca132a31a02b.png)
![2](https://user-images.githubusercontent.com/85356197/218775410-039febd4-a1bd-49bb-a9b8-7e5a260d2a44.png)

## Features To Implement

- Code cleanup
- Add more websites
- Add more tests

## License
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](https://www.gnu.org/licenses/gpl-3.0.en.html)  

This project is licensed under the GNU General Public License v3.0.
