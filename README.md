# ⚡ Fastest RAG Stack with Milvus and Groq

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![Beam](https://img.shields.io/badge/Beam-Cloud-purple.svg)](https://beam.cloud)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Build lightning-fast RAG applications with retrieval latency < 15ms** ⚡

</div>

---

## 🎯 Overview

This project delivers the **fastest possible RAG (Retrieval-Augmented Generation) stack** by combining cutting-edge technologies for optimal performance. Our architecture achieves sub-15ms retrieval latency through binary quantization and blazing-fast inference speeds.

### 🏗️ Architecture Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **🧠 Orchestration** | LlamaIndex | RAG application framework |
| **🗄️ Vector Database** | Milvus | Binary vector indexing & storage |
| **🚀 Inference Engine** | Groq (Kimi K2) | Ultra-fast LLM inference |
| **☁️ Deployment** | Beam Cloud | Serverless deployment platform |
| **🎨 Frontend** | Streamlit | Interactive web interface |

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.11+** installed on your system
- **Git** for cloning the repository

### 1️⃣ Project Setup

Install the lightning-fast **uv** package manager:

```bash
# 🍎 MacOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# 🪟 Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Create and configure your project:

```bash
# Create project directory
uv init fastest-rag
cd fastest-rag

# Setup virtual environment
uv venv
```

**Activate environment:**
```bash
# 🍎 MacOS/Linux
source .venv/bin/activate

# 🪟 Windows
.venv\Scripts\activate
```

### 2️⃣ Install Dependencies

```bash
uv add pymilvus llama-index llama-index-embeddings-huggingface llama-index-llms-groq streamlit beam-client
```

### 3️⃣ API Configuration

#### 🔑 Groq Setup
1. Get your API key from [Groq Console](https://console.groq.com/)
2. Create a `.env` file in your project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

#### ☁️ Beam Setup
1. Sign up at [Beam Cloud](https://www.beam.cloud/)
2. Configure your token:

```bash
beam configure default --token <YOUR_BEAM_TOKEN>
```

---

## 🚀 Deployment Options

### ☁️ Cloud Deployment (Recommended)

Deploy your application to Beam Cloud with a single command:

```bash
python start_server.py
```

✨ **That's it!** Your Streamlit app will be live on Beam Cloud. Copy the generated URL and access your RAG application directly from your browser.

### 🏠 Local Development

For local testing and development:

```bash
streamlit run app.py
```

Your app will be available at `http://localhost:8501`

---

## 🏎️ Performance Features

- **⚡ Sub-15ms Retrieval**: Binary quantization for lightning-fast vector search
- **🚀 Blazing Inference**: Groq's optimized inference engine
- **📈 Scalable Architecture**: Beam's serverless infrastructure
- **🔄 Real-time Updates**: Streamlit's reactive interface

---

## 📁 Project Structure

```
fastest-rag/
├── 📄 app.py              # Main Streamlit application
├── 🚀 start_server.py     # Beam deployment script
├── 🔧 requirements.txt    # Python dependencies
├── 🔐 .env               # Environment variables
└── 📖 README.md          # This file
```

---

## 🛠️ Customization

### Adding New Data Sources
Extend the RAG pipeline by modifying the data ingestion logic in `app.py`

### Model Configuration
Switch between different Groq models by updating the LLM configuration

### Vector Store Settings
Optimize Milvus parameters for your specific use case and data size

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **🍴 Fork** the repository
2. **🌟 Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **💾 Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **📤 Push** to the branch (`git push origin feature/amazing-feature`)
5. **🔄 Open** a Pull Request

## 📋 Troubleshooting

### Common Issues

**🐛 Import Errors**
```bash
# Ensure all dependencies are installed
uv sync
```

**🔑 API Key Issues**
- Verify your `.env` file is in the project root
- Check that environment variables are properly loaded

**☁️ Deployment Issues**
- Confirm Beam token is configured correctly
- Check your internet connection and Beam service status

---
<div align="center">

**⭐ Star this repo if you found it helpful!**

Made with ❤️ for the AI community

</div>
