# Book Recommendation System using Llama 3.2

This system leverages a **local Large Language Model (LLM)**, **Llama 3.2**, to generate personalized book recommendations based on user preferences. The backend integrates **LangChain** for managing prompts and workflows, **Ollama** for running the LLM locally, and **Chroma** for efficient retrieval of book data.

## Features
- **Personalized Book Recommendations**: Generate book suggestions based on user queries using a local LLM.
- **Context-Aware Conversations**: Maintain chat history for a more natural, context-aware recommendation experience.
- **Efficient Data Retrieval**: Use a vector store (Chroma) to quickly retrieve relevant book information.

## Technologies
- **Llama 3.2**: A local LLM used for generating responses to user queries.
- **LangChain**: A framework for building language model applications.
- **Ollama**: A tool for running Llama models locally.
- **Chroma**: A vector store used for efficient document retrieval.
- **Python**: Backend development using Python.

## Folder Structure

## Directory Structure
```plaintext
Book-Recommendation-AI/
├── data/
│   └── goodreads_data.csv     # Dataset containing book information
│
├── main.py                    # Main Python file for handling user interactions
├── vector.py                  # Vector store and document retrieval logic
├── requirements.txt           # List of Python dependencies
|
|-- .gitignore                 # Gitignore file to exclude unnecessary files
|-- LICENSE                    # MIT License file
|-- README.md                  # Project documentation
```

## Setup Instructions

### 1. Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/your-username/Book-Recommendation-AI.git
cd Book-Recommendation-AI
```

### 2. Install Dependencies
Set up a virtual environment and install required packages:
```bash
conda create -p venv python==3.11 -y
conda activate venv/
pip install -r requirements.txt
```

### 3. Run the AI Assistant
Start the recommendation system by running:
```bash
python main.py
```
This will initiate the chat session in your terminal, where you can ask for book recommendations.

## Notes
- The recommendation system relies on Llama 3.2, which is run locally using Ollama.
- Ensure your system has sufficient resources (memory, CPU, etc.) to handle running the model locally, especially for larger datasets or models.
