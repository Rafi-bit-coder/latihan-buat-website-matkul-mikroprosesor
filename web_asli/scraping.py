
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_website(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Open output file
        with open("scraped_data.txt", "w", encoding="utf-8") as file:

            # Website title
            title = soup.title.string.strip() if soup.title and soup.title.string else "No title"

            file.write("===== WEBSITE SCRAPER =====\n\n")
            file.write(f"Website Title: {title}\n\n")

            # Headings
            file.write("===== HEADINGS =====\n\n")

            for heading in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
                file.write(f"{heading.name}: {heading.get_text(strip=True)}\n")

            # Paragraphs
            file.write("\n===== PARAGRAPHS =====\n\n")

            for paragraph in soup.find_all("p"):
                text = paragraph.get_text(strip=True)

                if text:
                    file.write(text + "\n")

            # Links
            file.write("\n===== LINKS =====\n\n")

            for link in soup.find_all("a", href=True):
                href = urljoin(url, link["href"])
                text = link.get_text(strip=True)

                file.write(f"{text} -> {href}\n")

            # Images
            file.write("\n===== IMAGES =====\n\n")

            for img in soup.find_all("img"):
                src = img.get("src") or img.get("data-src")

                if src:
                    file.write(urljoin(url, src) + "\n")

        print("Scraping completed!")
        print("Output saved to scraped_data.txt")

    except requests.RequestException as error:
        print("Scraping Error:", error)


website_url = input("Enter website URL: ")

scrape_website(website_url)
