from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

# Load the local LLM
model = OllamaLLM(model="llama3.2")

# Define the AI assistant prompt
template = """
You are an expert in recommending books based on user preferences.
You have the following context from the user:

{chat_history}

Here are some relevant book descriptions: {book_info}

Here is the user's question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Initialize conversation history
chat_history = ""

# Start the chat session
while True:
    print("\n----------------------------------------")
    question = input("Ask about book recommendations (press 'q' to quit): ")
    print("\n")
    if question.lower() == "q":
        break

    # Retrieve book info related to the user's query
    book_info = retriever.invoke(question)

    # Add the new question to the chat history
    chat_history += f"User: {question}\n"

    # Use the chain to invoke the model with the chat history and question
    result = chain.invoke({"chat_history": chat_history, "book_info": book_info, "question": question})

    # Add the model's answer to the chat history
    chat_history += f"AI: {result}\n"

    # Print the model's response
    print(result)