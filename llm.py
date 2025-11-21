
import chromadb
import streamlit as st
from llama_index.core import VectorStoreIndex, StorageContext, Settings
from llama_index.core.postprocessor import SentenceTransformerRerank
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.openai_like import OpenAILike

from utils.config import Config


@st.cache_resource(show_spinner="初始化模型中...")
def init_models():
    """Initialize embedding model, LLM and reranker and attach to Settings."""
    embed_model = HuggingFaceEmbedding(
        model_name=Config.EMBED_MODEL_PATH,
    )

    llm = OpenAILike(
        model="qwen-max",
        api_base=Config.LLM_MODEL_PATH,
        api_key=Config.LLM_API_KEY,
        context_window=128000,
        is_chat_model=True,
        is_function_calling_model=False,
        max_tokens=1024,
        temperature=0.3,
        top_p=0.7,
    )

    reranker = SentenceTransformerRerank(
        model=Config.RERANK_MODEL_PATH,
        top_n=Config.RERANK_TOP_K,
    )

    Settings.embed_model = embed_model
    Settings.llm = llm

    return embed_model, llm, reranker


@st.cache_resource(show_spinner="加载知识库中...")
def init_vector_store(_nodes):
    """Create / load Chroma persistent collection and build / load index."""
    chroma_client = chromadb.PersistentClient(path=Config.VECTOR_DB_DIR)
    chroma_collection = chroma_client.get_or_create_collection(
        name=Config.COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"}
    )

    storage_context = StorageContext.from_defaults(
        vector_store=ChromaVectorStore(chroma_collection=chroma_collection)
    )

    if chroma_collection.count() == 0 and _nodes is not None:
        storage_context.docstore.add_documents(_nodes)
        index = VectorStoreIndex(
            _nodes,
            storage_context=storage_context,
            show_progress=True
        )
        storage_context.persist(persist_dir=Config.PERSIST_DIR)
        index.storage_context.persist(persist_dir=Config.PERSIST_DIR)
    else:
        storage_context = StorageContext.from_defaults(
            persist_dir=Config.PERSIST_DIR,
            vector_store=ChromaVectorStore(chroma_collection=chroma_collection)
        )
        index = VectorStoreIndex.from_vector_store(
            storage_context.vector_store,
            storage_context=storage_context,
            embed_model=Settings.embed_model
        )

    return index
