from chrono_crawler.omegaenthusiast import scrape_omegaenthusiast
from chrono_crawler.listing import Listing

from unittest.mock import Mock, patch


def test_scrape_omegaenthusiast():
    mock_listing = Listing(
        "1975 OMEGA GENEVE WATCH",
        1650,
        "https://static.wixstatic.com/media/dea6ce_ee2b05ade7234a14bfe4d4ab6d34e9e3~mv2.jpg/v1/fill/w_154,h_154,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/dea6ce_ee2b05ade7234a14bfe4d4ab6d34e9e3~mv2.jpg",
        "https://www.omegaenthusiastltd.com/product-page/1975-omega-geneve-watch-3",
        "Omega Enthusiast",
    )
    mock_response = Mock()
    mock_response.text = """
        <html>
            <body>
                <ul class="S4WbK_ uQ5Uah c2Zj9x H1ux6p">
                    <li data-hook="product-list-grid-item">
                        <div data-slug="1975-omega-geneve-watch-3" role="group" aria-label="1975 OMEGA GENEVE WATCH. New Arrival gallery" data-hook="product-item-root" class="ETPbIy nvdiI6">
                            <a href="https://www.omegaenthusiastltd.com/product-page/1975-omega-geneve-watch-3" tabindex="-1" class="oQUvqL x5qIv3" data-hook="product-item-container">
                                <div class="mS0yET heightByImageRatio heightByImageRatio2" aria-live="assertive" data-hook="ProductMediaDataHook.Images">
                                    <div class="naMHY_ vALCqq" data-hook="ImageUiTpaWrapperDataHook.Wrapper_0">
                                        <div data-source-width="611" data-source-height="595" data-resize="cover" data-use-lqip="true" data-is-seo-bot="false" class="sWazHlK oCVhrpB---resize-5-cover oCVhrpB--fluid oCVhrpB--stretchImage oCVhrpB--verticalContainer s__65YAB3 v_lwe5" data-hook="ImageUiTpaWrapperDataHook.Media_0">
                                            <wow-image class="zTx3Xx sbGsCag" data-image-info="{&quot;displayMode&quot;:&quot;fill&quot;,&quot;isLQIP&quot;:true,&quot;isSEOBot&quot;:false,&quot;lqipTransition&quot;:null,&quot;imageData&quot;:{&quot;width&quot;:611,&quot;height&quot;:595,&quot;uri&quot;:&quot;dea6ce_ee2b05ade7234a14bfe4d4ab6d34e9e3~mv2.jpg&quot;,&quot;name&quot;:&quot;dea6ce_ee2b05ade7234a14bfe4d4ab6d34e9e3~mv2.jpg&quot;,&quot;displayMode&quot;:&quot;fill&quot;}}" data-bg-effect-name="" data-has-ssr-src="" data-src="https://static.wixstatic.com/media/dea6ce_ee2b05ade7234a14bfe4d4ab6d34e9e3~mv2.jpg/v1/fill/w_154,h_154,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/dea6ce_ee2b05ade7234a14bfe4d4ab6d34e9e3~mv2.jpg"><img src="https://static.wixstatic.com/media/dea6ce_ee2b05ade7234a14bfe4d4ab6d34e9e3~mv2.jpg/v1/fill/w_154,h_154,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/dea6ce_ee2b05ade7234a14bfe4d4ab6d34e9e3~mv2.jpg" alt="1975 OMEGA GENEVE WATCH" style="width: 154px; height: 154px; object-fit: cover; object-position: 50% 50%;" fetchpriority="high"></wow-image>
                                        </div>
                                    </div>
                                    <div class="naMHY_ vALCqq" data-hook="ImageUiTpaWrapperDataHook.Wrapper_1">
                                        <div data-source-width="980" data-source-height="1307" data-resize="cover" data-use-lqip="true" data-is-seo-bot="false" class="sWazHlK oCVhrpB---resize-5-cover oCVhrpB--fluid oCVhrpB--stretchImage oCVhrpB--verticalContainer s__65YAB3 v_lwe5" data-hook="ImageUiTpaWrapperDataHook.Media_1">
                                            <wow-image class="zTx3Xx sbGsCag" data-image-info="{&quot;displayMode&quot;:&quot;fill&quot;,&quot;isLQIP&quot;:true,&quot;isSEOBot&quot;:false,&quot;lqipTransition&quot;:null,&quot;imageData&quot;:{&quot;width&quot;:980,&quot;height&quot;:1307,&quot;uri&quot;:&quot;dea6ce_1db214b86c85489888ebd5d1290caaae~mv2.jpg&quot;,&quot;name&quot;:&quot;dea6ce_1db214b86c85489888ebd5d1290caaae~mv2.jpg&quot;,&quot;displayMode&quot;:&quot;fill&quot;}}" data-bg-effect-name="" data-has-ssr-src="" data-src="https://static.wixstatic.com/media/dea6ce_1db214b86c85489888ebd5d1290caaae~mv2.jpg/v1/fill/w_154,h_154,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/dea6ce_1db214b86c85489888ebd5d1290caaae~mv2.jpg"><img src="https://static.wixstatic.com/media/dea6ce_1db214b86c85489888ebd5d1290caaae~mv2.jpg/v1/fill/w_154,h_154,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/dea6ce_1db214b86c85489888ebd5d1290caaae~mv2.jpg" alt="1975 OMEGA GENEVE WATCH" style="width: 154px; height: 154px; object-fit: cover; object-position: 50% 50%;" fetchpriority="high"></wow-image>
                                        </div>
                                    </div><span class="INg0tB FbHYze oOOCOE" data-hook="product-item-ribbon">New Arrival</span><button class="TUWFt6" data-hook="product-item-quick-view-button" tabindex="-1" aria-hidden="true">Quick View</button></div>
                            </a>
                            <div data-hook="not-image-container" class="CZ0KIs">
                                <a href="https://www.omegaenthusiastltd.com/product-page/1975-omega-geneve-watch-3" class="JPDEZd" data-hook="product-item-product-details-link">
                                    <div class="t2u_rw PbZno5" data-hook="product-item-product-details">
                                        <h3 class="sFLgyi1 oF9mV84---typography-11-runningText oF9mV84---priority-7-primary syHtuvM FzO_a9" aria-hidden="false" data-hook="product-item-name">1975 OMEGA GENEVE WATCH</h3>
                                        <div class="ZMQj6C">
                                            <hr data-hook="product-item-line-between-name-and-price" class="MInUcJ" aria-hidden="true">
                                        </div>
                                        <div class="UqnnNN"><span class="ruX1QG" data-hook="sr-product-item-price-to-pay">Price</span><span data-hook="product-item-price-to-pay" class="cfpn1d">$1,650.00</span></div>
                                    </div>
                                </a>
                                <div data-hook="slot-placeholder-TPASection_iz86jgqi.gallery-rating-summary-slot" id="TPASection_iz86jgqi.gallery-rating-summary-slot" class=""></div>
                            </div>
                        </div>
                    </li>
                </ul>
            </body>
        </html>
    """
    with patch("requests.get", return_value=mock_response):
        listings = scrape_omegaenthusiast('')
        assert len(listings) == 1
        assert listings[0].title == mock_listing.title
        assert listings[0].price == mock_listing.price
        assert listings[0].photo == mock_listing.photo
        assert listings[0].url == mock_listing.url
        assert listings[0].store == mock_listing.store
