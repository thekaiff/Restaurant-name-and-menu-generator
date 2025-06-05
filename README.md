# 🍽️ AI Restaurant Name & Menu Generator

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-orange)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/Powered%20By-LangChain-blueviolet)](https://www.langchain.com/)
[![Together AI](https://img.shields.io/badge/LLM-Together.ai-brightgreen)](https://www.together.ai/)

Generate catchy restaurant names and authentic cuisine-based menu items using LLMs via Together AI. Built with Streamlit & LangChain.

---

## 🚀 Features

- 🏷️ Generate restaurant names based on selected cuisine
- 🍜 Suggest 5 authentic menu items for each generated restaurant
- 🧠 Uses `LangChain` with `Together.ai`'s DeepSeek LLM
- 🌐 Clean, interactive Streamlit UI

---

## 🖥️ Demo

> Select a cuisine from the sidebar and get a restaurant name + 5-item menu instantly!

---

## 📂 File Structure

```bash
📁 Restaurant-name-and-menu-generator/
├── streamlit_app.py              # Streamlit UI code
├── langchain_helper.py          # LLM logic using LangChain
├── learning_langchain.ipynb 
├── secret_key.py                # Contains Together API key
└── README.md
```

---

# ⚙️ Setup
``` bash
git clone https://github.com/yourusername/restaurant-generator.git
cd restaurant-generator
pip install -r requirements.txt
```

---

Make sure your secret_key.py file contains:

api_key = "your_together_ai_key"
Then run:

```bash
streamlit run streamlit_app.py
```

# 🧠 Tech Stack
- Python 3.10+
- Streamlit
- LangChain
- Together AI LLMs (DeepSeek)
- Prompt Engineering + Sequential Chains

---

Created for fun and exploration of LLMs in creative, real-world use cases ✨
