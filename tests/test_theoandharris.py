from chrono_crawler.theoandharris import scrape_theoandharris
from chrono_crawler.listing import Listing

from unittest.mock import Mock, patch


def test_scrape_theoandharris():
    mock_listing = Listing(
        "Test Listing",
        10000,
        "https://example.com/image.jpg",
        "https://example.com/listing",
        "Theo and Harris",
    )
    mock_response = Mock()
    mock_response.text = """
        <html>
            <body>
                <ul class="columns-4">
                    <li class="product">
                        <h2 class="woocommerce-loop-product__title">Test Listing</h2>
                        <span class="price"><span class="woocommerce-Price-amount amount"><bdi><span class="woocommerce-Price-currencySymbol">$</span>10,000 USD</bdi></span></span>
                        <a href="https://example.com/listing"><img src="https://example.com/image.jpg"></a>
                    </li>
                </ul>
            </body>
        </html>
    """
    with patch("requests.get", return_value=mock_response):
        listings = scrape_theoandharris()
        assert len(listings) == 1
        assert listings[0].title == mock_listing.title
        assert listings[0].price == mock_listing.price
        assert listings[0].photo == mock_listing.photo
        assert listings[0].url == mock_listing.url
        assert listings[0].store == mock_listing.store
