# Chrono Crawler

A web scraper to get listings from popular vintage and pre-owned watch retailers.

![1](https://user-images.githubusercontent.com/85356197/212807279-354e0bec-8cd4-4609-823c-896772a4a365.png)

Currently supported websites:
- Theo and Harris
- Delray Watch
- Omega Enthusiast

Using argparse, requests, BeautifulSoup, multiprocessing, tqdm.

***

Usage:

To get listings from Theo and Harris, use the following command:

```python3 chrono-crawler.py -t```

To get listings from Delray Watch, use the following command:

```python3 chrono-crawler.py -d```

To get listings from Omega Enthusiast, use the following command:

```python3 chrono-crawler.py -o```

To search for a term like 'Universal Geneve', use the following command:

```python3 chrono-crawler.py -s 'Universal Geneve'```

You can also use the following command to see the help message of the script:

```python3 chrono-crawler.py -h```

***

Features to implement:
- Sorting by price
- Use Selenium for Delray Watch to accomodate a less-than-ideal website
- Add more websites

***

This project is licensed under the GNU General Public License v3.0.
