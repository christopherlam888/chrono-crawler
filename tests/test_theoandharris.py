from chrono_crawler.theoandharris import scrape_theoandharris
from chrono_crawler.listing import Listing

from unittest.mock import Mock, patch


def test_scrape_theoandharris():
    mock_listing = Listing(
        "Rolex GMT Master",
        14995,
        "https://theoandharris.com/wp-content/uploads/Rolex-GMT-02-23-23-1-600x600.jpg",
        "https://theoandharris.com/shop/vintage-watches/rolex-gmt-master-3/",
        "Theo and Harris",
    )
    mock_response = Mock()
    mock_response.text = """
        <html>
            <body>
                <ul class="columns-4">
                    <li class="product type-product post-87582 status-publish first instock product_cat-vintage-watches has-post-thumbnail taxable shipping-taxable purchasable product-type-simple et_pb_shop_item_0_0">
                        <a href="https://theoandharris.com/shop/vintage-watches/rolex-gmt-master-3/" class="woocommerce-LoopProduct-link woocommerce-loop-product__link">
                            <div class="tp-image-wrapper"><noscript><img decoding="async" class="tp-image" src="https://theoandharris.com/wp-content/uploads/Rolex-GMT-02-23-23-1-600x600.jpg" srcset="" sizes="(max-width: 360px) 100vw, 360px" alt="Rolex GMT Master"></noscript><img decoding="async" class="tp-image ls-is-cached lazyloaded" src="https://theoandharris.com/wp-content/uploads/Rolex-GMT-02-23-23-1-600x600.jpg" data-src="https://theoandharris.com/wp-content/uploads/Rolex-GMT-02-23-23-1-600x600.jpg" data-srcset="" data-sizes="(max-width: 360px) 100vw, 360px" alt="Rolex GMT Master" sizes="(max-width: 360px) 100vw, 360px"><noscript><img decoding="async" class="tp-image-hover" src="https://theoandharris.com/wp-content/uploads/Rolex-GMT-02-23-23-2-600x600.png" srcset="" sizes="(max-width: 360px) 100vw, 360px" alt="Rolex GMT Master"></noscript><img decoding="async" class="tp-image-hover ls-is-cached lazyloaded" src="https://theoandharris.com/wp-content/uploads/Rolex-GMT-02-23-23-2-600x600.png" data-src="https://theoandharris.com/wp-content/uploads/Rolex-GMT-02-23-23-2-600x600.png" data-srcset="" data-sizes="(max-width: 360px) 100vw, 360px" alt="Rolex GMT Master" sizes="(max-width: 360px) 100vw, 360px"></div>
                            <h2 class="woocommerce-loop-product__title">Rolex GMT Master</h2> <span class="price"><span class="woocommerce-Price-amount amount"><bdi><span class="woocommerce-Price-currencySymbol">$</span>14,995&nbsp;USD</bdi>
                            </span>
                            </span>
                        </a>
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
