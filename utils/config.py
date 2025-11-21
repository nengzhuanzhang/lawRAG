from pathlib import Path
import os

class Config:
    # 模型路径与 API 配置（按需修改）
    EMBED_MODEL_PATH = r"D:\04_Learn\AI\models\sungw111\text2vec-base-chinese-sentence" # 调本地embedding模型
    RERANK_MODEL_PATH = r"D:\04_Learn\AI\models\BAAI\bge-reranker-large" # 调本地reranker模型
    LLM_MODEL_PATH = "https://dashscope.aliyuncs.com/compatible-mode/v1" # 阿里百炼
    LLM_API_KEY = os.getenv("DASHSCOPE_API_KEY")

    # 数据与持久化目录
    DATA_DIR = str(Path("./data"))
    VECTOR_DB_DIR = str(Path("./chroma_db"))
    PERSIST_DIR = str(Path("./storage"))

    COLLECTION_NAME = "chinese_labor_laws"
    TOP_K = 10
    RERANK_TOP_K = 3
