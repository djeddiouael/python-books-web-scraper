
import requests
import csv
import time

from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Website configuration
BASE_URL = "https://books.toscrape.com/"
OUTPUT_FILE = Path("data/books.csv")

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

# Store extracted books
books = []


def scrape_page(url):
    """Download and extract books from one page."""

    print(f"Scraping: {url}")

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=20
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    products = soup.find_all(
        "article",
        class_="product_pod"
    )

    for product in products:

        title = product.h3.a["title"]

        price = product.find(
            "p",
            class_="price_color"
        ).text.strip()

        rating = product.find(
            "p",
            class_="star-rating"
        )["class"][1]

        availability = product.find(
            "p",
            class_="availability"
        ).text.strip()

        book = {
            "title": title,
            "price": price,
            "rating": rating,
            "availability": availability
        }

        books.append(book)

    # Find next page
    next_page = soup.find(
        "li",
        class_="next"
    )

    if next_page:
        next_link = next_page.a["href"]
        return urljoin(url, next_link)

    return None


def save_to_csv():
    """Save extracted books into CSV."""

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    fieldnames = [
        "title",
        "price",
        "rating",
        "availability"
    ]

    with open(
        OUTPUT_FILE,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(books)

    print(f"\nData saved to: {OUTPUT_FILE}")


def main():

    current_url = BASE_URL

    try:
        while current_url:

            current_url = scrape_page(current_url)

            # Avoid sending requests too quickly
            if current_url:
                time.sleep(1)

        save_to_csv()

        print(f"Total books extracted: {len(books)}")

    except requests.RequestException as error:
        print(f"Network error: {error}")

    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
