# Lokales LLM mit Chat-UI und Markdown-Daten

Dieses Projekt zeigt, wie man ein lokales Large Language Model (LLM) mit Ollama und LlamaIndex betreibt, um Fragen zu eigenen Markdown-Dokumenten zu beantworten – **ohne OpenAI-API**.

## Voraussetzungen
- Python 3.10+
- [Ollama](https://ollama.com/) installiert
- Modell lokal geladen, z. B. `ollama run mistral`

## Setup
```bash
pip install llama-index gradio chromadb llama-index-embeddings-huggingface
python main.py
```

## Nutzung
Im Browser öffnen: http://127.0.0.1:7860
