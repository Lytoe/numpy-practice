import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re
import time

BASE_URL = "https://pages.llf-paris.fr/~gwisniewski/"
DOWNLOAD_DIR = "./gwisniewski_courses"
VISITED_PAGES = set()


def sanitize_name(name):
    """Removes invalid characters for folder creation."""
    return re.sub(r'[\\/*?:"<>|]', "", name).strip()


def get_page_title(soup, url):
    """Extracts a clean title for folder naming."""
    if soup.title and soup.title.string:
        return sanitize_name(soup.title.string)
    return sanitize_name(os.path.basename(urlparse(url).path) or "General")


def crawl_and_download(url, base_domain):
    """Recursively crawls internal pages and downloads PDFs."""
    if url in VISITED_PAGES:
        return
    VISITED_PAGES.add(url)

    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200 or 'text/html' not in response.headers.get('Content-Type', ''):
            return
    except requests.RequestException:
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    page_title = get_page_title(soup, url)

    # 1. Extract and download PDFs on this page
    pdf_links = {urljoin(url, a.get('href')) for a in soup.find_all('a')
                 if a.get('href') and a.get('href').lower().endswith('.pdf')}

    if pdf_links:
        print(f"\nFound {len(pdf_links)} PDFs on: {page_title} ({url})")
        folder_path = os.path.join(DOWNLOAD_DIR, page_title)
        os.makedirs(folder_path, exist_ok=True)

        for pdf_url in pdf_links:
            filename = os.path.basename(urlparse(pdf_url).path)
            file_path = os.path.join(folder_path, filename)

            if not os.path.exists(file_path):
                try:
                    with requests.get(pdf_url, stream=True, timeout=15) as r:
                        r.raise_for_status()
                        with open(file_path, 'wb') as f:
                            for chunk in r.iter_content(chunk_size=8192):
                                f.write(chunk)
                    print(f"  -> Saved: {filename}")
                except Exception as e:
                    print(f"  -> Failed to download {filename}: {e}")
            else:
                print(f"  -> Skipped (exists): {filename}")

    # 2. Find and crawl all internal links
    for link in soup.find_all('a'):
        href = link.get('href')
        if not href or href.startswith(('mailto:', 'tel:', '#')):
            continue

        full_url = urljoin(url, href)

        # Ensure we stay within his specific sub-directory to avoid crawling all of llf-paris.fr
        if full_url.startswith(base_domain) and full_url not in VISITED_PAGES and not full_url.lower().endswith('.pdf'):
            # Basic rate limiting to respect the server
            time.sleep(0.5)
            crawl_and_download(full_url, base_domain)


if __name__ == "__main__":
    print(f"Starting crawl at {BASE_URL}...")
    crawl_and_download(BASE_URL, BASE_URL)
    print("\nCrawl complete.")
