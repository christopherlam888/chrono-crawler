# Chrono Crawler

A web scraper to get listings from popular vintage and pre-owned watch retailers.

![1](https://user-images.githubusercontent.com/85356197/212807279-354e0bec-8cd4-4609-823c-896772a4a365.png)

![2](https://user-images.githubusercontent.com/85356197/212807582-aa150e7a-1670-47b6-aeb8-8e597198dc6c.png)

Currently supported websites:
- Theo and Harris
- Delray Watch
- Omega Enthusiast

Using argparse, requests, BeautifulSoup, Selenium, multiprocessing, tqdm, webbrowser.

***

Usage:

To get listings from Theo and Harris, use the following command:

```python3 chrono_crawler.py -t```

To get listings from Delray Watch, use the following command:

```python3 chrono_crawler.py -d```

To get listings from Omega Enthusiast, use the following command:

```python3 chrono_crawler.py -o```

To search for a term like 'Universal Geneve', use the following command:

```python3 chrono_crawler.py -s 'Universal Geneve'```

To sort by price (low to high), use the following command:

```python3 chrono_crawler.py -p```

You can also use the following command to see the help message of the script:

```python3 chrono_crawler.py -h```

***

Features to implement:
- Add more websites

***

This project is licensed under the GNU General Public License v3.0.
