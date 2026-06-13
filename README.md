# Chatbots using LangChain

Small examples showing how to use LangChain integrations (OpenAI, Anthropic, Google Generative AI, HF) to build chat and LLM demos.

Folders
- `ChatModels/` — small example using OpenAI chat model.
- `LLMs/` — simple LLM invocation demo.
- `Prompts/` — prompt template and a basic interactive chatbot example.

Requirements
- See `requirements.txt` for the Python dependencies. Use a virtual environment (recommended).

Quickstart

1. Create and activate a virtual environment (recommended):

```bash
cd "/Users/dm/Developer/langchain models"
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Create a `.env` file in the repo root and set any API keys required by the providers you want to use (OpenAI, Google, Anthropic, etc.):

```bash
# Example .env
OPENAI_API_KEY=sk-...
GOOGLE_API_KEY=...
# and so on
```

3. Examples

- Run the Chat Prompt example (creates a ChatPromptTemplate and prints the assembled prompt):

```bash
python3 Prompts/chat_prompt_model.py
```

- Run the interactive chatbot (uses `ChatOpenAI` and `langchain_core.messages`):

```bash
python3 Prompts/chatbot.py
```

- Run the OpenAI chat model demo:

```bash
python3 ChatModels/chatmodel_openai.py
```

- Run the LLM demo:

```bash
python3 LLMs/llm_demo.py
```

.gitignore and virtual environments
- This repository includes a `.gitignore` at the root that excludes `venv/` and `.venv/` so your local virtual environment is not pushed to GitHub.

Pushing to GitHub

- Initialize and push (if you haven't yet):

```bash
git init
git add .
git commit -m "Initial commit"
# create a GitHub repo (manually or using gh)
git remote add origin git@github.com:your-github-username/Chatbots-using-Langchain.git
git branch -M main
git push -u origin main
```

Notes
- If you accidentally committed the `venv/` folder before adding it to `.gitignore`, remove it from the index with:

```bash
git rm -r --cached venv .venv
git commit -m "Remove virtualenv from repository"
```

- Replace API keys and model names in the example scripts as needed. These examples assume you have installed the provider-specific LangChain integration packages listed in `requirements.txt`.

License
- Add your preferred license to the repo (e.g., MIT) if you plan to publish this publicly.
