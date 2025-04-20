import json

class AnswerDrafterAgent:
    def __init__(self, data_path='data/crawled_data.json'):
        self.data_path = data_path

    def generate_summary(self):
        try:
            with open(self.data_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            combined_text = " ".join(data)
            return f"Summary of research:\n\n{combined_text[:1000]}..."  # Show first 1000 chars

        except FileNotFoundError:
            return "[⚠️] No data found. Please run the ResearchAgent first."
