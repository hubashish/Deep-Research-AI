from agents.research_agent import ResearchAgent
from agents.answer_drafter_agent import AnswerDrafterAgent

def main():
    query = "Latest advancements in AI agent systems"
    researcher = ResearchAgent(query)
    researcher.crawl_websites()

    drafter = AnswerDrafterAgent()
    answer = drafter.generate_summary()

    print("\n📝 Final Drafted Answer:\n")
    print(answer)

if __name__ == "__main__":
    main()
