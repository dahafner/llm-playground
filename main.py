from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
import gradio as gr

# Daten laden
documents = SimpleDirectoryReader("Z:\data", recursive=True).load_data()

for doc in documents:
    print("✅ Eingelesen:", doc.metadata.get('file_path'))

# LLM & Embeddings lokal definieren
#llm = Ollama(model="gemma:2b", base_url="http://192.168.10.109:11434", system_prompt="Du bist ein hilfreicher Assistent und antwortest immer auf Deutsch.")
llm = Ollama(model="mistral", base_url="http://192.168.10.109:11434", system_prompt="Du bist ein hilfreicher Assistent und antwortest immer auf Deutsch.")
#embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/distiluse-base-multilingual-cased-v2")


# Index erstellen mit explizitem Embedding
index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)
query_engine = index.as_query_engine(llm=llm)

# Chat-UI
def chat(prompt):
    response = query_engine.query(prompt)
    return str(response)

gr.Interface(fn=chat, inputs="text", outputs="text", title="Chatbot").launch()