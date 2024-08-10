# install Playwright: https://playwright.dev/python/docs/intro/

import csv 
import datetime
import urllib.parse
from playwright.sync_api import Playwright, sync_playwright, expect

timestamp = datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        geolocation={"latitude":51.509864,"longitude":-0.118093}, 
        locale="en-GB", 
        permissions=["geolocation"], 
        timezone_id="Europe/London", 
        viewport={"width": 1024, "height": 2800}
    )
    page = context.new_page()

    # Navigate to ASDA and accept cookie prompt to remove overlay on screenshots
    page.goto("https://wikipedia.com/")
    #page.get_by_role("button", name="I Accept").click()

    """search_terms = [
        "shampoo",
        "conditioner",
        # "body wash",
        # "nappies size 3",
    ]"""

    # pg_products = [
    #     "head & shoulders",
    #     "aussie",
    #     "pantene",
    # ]

    # for search_term in search_terms:
    #     search_term = urllib.parse.quote_plus(search_term)
    #     page.goto(f"https://groceries.asda.com/search/{search_term}")
    #     page.wait_for_load_state("networkidle")
    #     image_filename = f"asda-{search_term}.png"
    #     timestamp_filepath = f"{timestamp}/{image_filename}"
        
    #     page.screenshot(path=timestamp_filepath)

    #     top_ten_pg_product_count = 0

    #     csv_fields = ['Product Title', 'Product URL', 'ASDA Product Code', 'Sponsored', 'PG Product']
    #     csv_filename = f'{timestamp}/asda-{search_term}-{timestamp}.csv'

    #     product_rows = []
    #     products = page.locator('ul[class*="co-product-list"] > li[class*="co-item"]')

    #     # top 10 products in search results
    #     for index in range(10):
    #         product = products.nth(index)
    #         product_html = product.locator('div[class*="co-item__title"]')
    #         product_name = product_html.inner_text()
    #         product_url = product_html.locator('a').get_attribute('href')
    #         product_code = product_url.split('/')[-1]
    #         product_sponsored = "sponsored" in product.inner_text().lower()
    #         product_pg = any(pg_product in product_name.lower() for pg_product in pg_products)
    #         if product_pg:
    #             top_ten_pg_product_count += 1

    #         print(f"{product_name} | {product_code} | {product_url} | {product_sponsored} | {product_pg}")
    #         product_rows.append([product_name, product_url, product_code, product_sponsored, product_pg])
        
    #     with open(csv_filename, 'w') as csvfile: 
    #         csvwriter = csv.writer(csvfile) 
    #         csvwriter.writerow(csv_fields) 
    #         csvwriter.writerows(product_rows)
    #     print(f"Top ten {search_term} PG product count: {top_ten_pg_product_count}")

    page.pause()
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
    

# Additional retailer search result url format
# https://www.tesco.com/groceries/en-GB/search?query=shampoo
#"https://www.sainsburys.co.uk/gol-ui/SearchResults/shampoo"

# Playwright codegen example: playwright codegen --timezone="Europe/London" --geolocation="51.509864, -0.118093" --lang="en-GB" https://groceries.asda.com/search/shampoo