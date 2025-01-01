
# Website Summariser

A Streamlit app that generates concise summaries from web page content using LangChain and OpenAI’s GPT-3.5-turbo.

## Features
- **Load Web Content**: Extracts text from a given URL.
- **Text Processing**: Splits text into smaller chunks for efficient analysis.
- **Vector Embeddings**: Stores and retrieves text using OpenAI embeddings and Chroma.
- **Question Answering**: Summarizes content based on relevant text chunks.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/waihin26/Website-Summariser.git
   cd Website-Summariser
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your OpenAI API key to a `.env` file:
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

1. Run the app:
   ```bash
   streamlit run summariser_app.py
   ```
2. Open your browser and enter a URL to summarize its content.

---

## Tech Stack
- **LangChain** for text processing and retrieval-based QA.
- **OpenAI** GPT-3.5-turbo for generating summaries.
- **Streamlit** for the user interface.

## License
Licensed under [MIT](LICENSE).
