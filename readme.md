# LawRag — 智能劳动法咨询助手

简要说明：本仓库实现了一个基于 Streamlit 的互动化劳动法问答助手，利用本地/远程 LLM（通过 `llama-index` 的 OpenAI-like 接口封装）与向量数据库（Chroma）构建问答系统。
# LawRag — 智能劳动法咨询助手

这是一个基于 Streamlit 的交互式劳动法问答系统模板（演示/本地部署版）。

功能概览
- 使用本地或远端 LLM（通过 llama-index 的 OpenAI-like 接口封装）生成回答。
- 使用 Chroma 向量数据库存储与检索法律条文向量。
- 支持本地 embedding 与 reranker 模型（HuggingFace 格式）。

快速开始（Windows + PowerShell）

1) 创建并激活 conda 环境（建议 Python 3.11）：

```powershell
conda create -n law-env python=3.11 -y
conda activate law-env
```

2) 安装运行所需依赖（示例）：

```powershell
pip install --upgrade pip
pip install streamlit chromadb "llama-index" sentence-transformers transformers huggingface-hub torch accelerate
```

可选加速库：

```powershell
pip install hnswlib faiss-cpu
```

4) 配置模型与 API：

编辑 `config.py` 中的常量或使用环境变量：

- `EMBED_MODEL_PATH`：embedding 模型，加载本地路径或在线模型
- `RERANK_MODEL_PATH`：reranker 模型，加载本地路径或在线模型
- `LLM_MODEL_PATH`, `LLM_API_KEY`：远端 OpenAI-like 接口配置，也可以加载本地模型（可以看test/test02.py 文件的HuggingFaceLLM使用）

5) 准备数据：

把法律条文 JSON 文件放到 `data/`，每个文件应包含一个 list，list 的每个元素为 dict（键为标题，值为条文字符串）。

示例格式：

```json
[
	{"劳动合同法 第一条": "这是条文内容..."},
	{"劳动法 第二条": "这是另外一条内容..."}
]
```

6) 启动应用（推荐）：

```powershell
streamlit run .\main.py
```

7) 数据来源
data数据来源：http://www.npc.gov.cn/npc/c2/c30834/201905/t20190521_296651.html


打开浏览器访问 http://localhost:8501 查看界面。

说明与注意事项
- 使用 `streamlit run` 启动以获得完整的运行时支持（ScriptRunContext）。直接用 `python main.py` 可能无法正常呈现交互界面。
- 首次运行若 `chroma_db` 目录不存在，系统会自动从 `data/` 构建向量库并持久化到 `chroma_db`。
- 本地使用 HuggingFace 模型时需安装 `torch`（CPU 或 GPU 版本），并确保有足够资源加载模型。

