"""
TASK 1 - Web Scraping
Source: https://books.toscrape.com/
Purpose: scrape book title, price, availability and rating from public catalogue pages.

The website is a demo site specifically intended for web-scraping practice.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

def scrape_books(max_pages=50):
    rows = []
    for page in range(1, max_pages + 1):
        url = BASE_URL.format(page)
        response = requests.get(url, timeout=20)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        cards = soup.select("article.product_pod")
        if not cards:
            break

        for card in cards:
            title_tag = card.select_one("h3 a")
            price_tag = card.select_one(".price_color")
            availability_tag = card.select_one(".availability")
            rating_tag = card.select_one("p.star-rating")

            title = title_tag.get("title", "").strip()
            price_text = price_tag.get_text(strip=True).replace("£", "")
            availability = availability_tag.get_text(" ", strip=True) if availability_tag else ""
            rating = rating_tag.get("class", ["", "Unknown"])[1] if rating_tag else "Unknown"

            rows.append({
                "title": title,
                "price_gbp": float(price_text),
                "availability": availability,
                "rating": rating,
                "page": page
            })

    return pd.DataFrame(rows)

if __name__ == "__main__":
    data = scrape_books(max_pages=50)
    data.to_csv("../data/books_scraped_full.csv", index=False)
    print(f"Saved {len(data)} records.")
