# 🚀 LinkedIn Post Generator

> **Turn raw thoughts into high-converting LinkedIn posts in seconds.** This tool automates content creation by transforming bullet points, articles, or rough ideas into engaging, professional LinkedIn posts—saving creators and professionals hours of writer's block every week.

---

## ✨ Key Features

- **💡 Instant Draft Generation:** Convert rough bullet points or topics into fully formatted LinkedIn posts.
- **🎯 Custom Tone Selection:** Adapt post style (e.g., Professional, Storytelling, Controversial, Educational, Humorous).
- **🪝 Hook & CTA Suggestions:** Automatically generates attention-grabbing headline hooks and engaging call-to-actions.
- **✨ Hashtag & Formatting Assistant:** Generates relevant hashtags and formats text with clean spacing and emojis.

---

## 🛠️ Prerequisites / Tech Stack

### Built With:
- **Language:** Python
- **Frontend:** Streamlit
- **Backend:** Langchain
- **LLM Provider:** OpenAI API

### Requirements:
- **Python:** `>= 3.10+`
- **Package Manager:** `uv`
- **API Key:** Active OpenAI API Key

---

## ⚙️ Environment Variables

Create a `.env` file in the root directory and populate it with your credentials:

```
# Server Config
PORT=5000

# AI Provider API Keys
OPENAI_API_KEY=your_openai_api_key_here
```

## 🚀 Installation & Quick Start
Follow these steps to set up and run the project locally.

### 1. Clone the Repository
```
git clone https://github.com/your-username/linkedin-post-generator.git
cd linkedin-post-generator
```

### 2. Install Dependencies
```
# If using Python
pip install -r requirements.txt
```

### 3. Run the Application
```
# Development Server
streamlit run app/streamlit.py
```