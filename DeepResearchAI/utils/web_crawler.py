import requests
from bs4 import BeautifulSoup

def fetch_and_parse(url):
    try:
        print(f"[🌐] Fetching: {url}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text = "\n".join(p.get_text() for p in paragraphs if p.get_text().strip())
        return text.strip()

    except Exception as e:
        print(f"[❌] Error fetching {url}: {e}")
        return ""
