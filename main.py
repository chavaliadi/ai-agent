from dotenv import load_dotenv
from langchain_groq import ChatGroq
from tools import search_tool

load_dotenv()

# Simple LLM without agents
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7)

print("="*50)
print("RESEARCH AGENT")
print("="*50)
print("Type 'exit' to quit\n")

while True:
    try:
        query = input("Your question: ").strip()

        if query.lower() == "exit":
            print("\nThank you for using the Research Agent. Goodbye!")
            break

        if not query:
            print("Please enter a question.\n")
            continue

        print("\n🔍 Searching...\n")

        # Get search results
        search_results = search_tool.invoke(query)

        # Create prompt with search results
        prompt = f"""Based on these search results, answer the question briefly and clearly:

Search Results:
{search_results}

Question: {query}

Provide a concise answer (2-3 paragraphs max):"""

        # Get response from LLM
        response = llm.invoke(prompt)

        print("="*50)
        print(response.content)
        print("="*50 + "\n")

    except KeyboardInterrupt:
        print("\n\nGoodbye!")
        break
    except Exception as e:
        if "429" in str(e):
            print("⚠️ Rate limited. Please wait a moment and try again.\n")
        else:
            print(f"❌ Error: {str(e)}\n")
