import json
from utils.web_crawler import fetch_and_parse
from utils.data_cleaner import clean_data
from tavily import TavilyClient  # Import Tavily at the beginning

class ResearchAgent:
    def __init__(self, query):
        self.query = query
        self.crawled_data = []

    def crawl_websites(self):
        print(f"[🔍] Starting research for: {self.query}")

        # Using Tavily for searching
        client = TavilyClient(api_key="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")  # Replace with your actual API key

        try:
            results = client.search(query=self.query, search_depth="advanced")
            urls = [res["url"] for res in results["results"]]
        except Exception as e:
            print(f"[❌] Tavily search failed: {e}")
            urls = []

        # Crawling each URL to fetch and clean data
        for url in urls:
            page_content = fetch_and_parse(url)  # Corrected here: `url` should be passed, not the string "url"
            cleaned_data = clean_data([page_content])
            self.crawled_data.extend(cleaned_data)

        self.save_data()

    def save_data(self):
        with open('data/crawled_data.json', 'w', encoding='utf-8') as f:
            json.dump(self.crawled_data, f, indent=4, ensure_ascii=False)
        print(f"[✅] Data saved to data/crawled_data.json")
