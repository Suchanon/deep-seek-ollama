# DeepSeek Local Setup Walkthrough

## Status
- **Ollama Installed**: ✅
- **DeepSeek-Coder-V2 Model**: ✅ (Ready)
- **Python Integration**: ✅ (Ready)

## How to Run
### 1. Terminal Chat
To start chatting with your local DeepSeek model directly in the terminal:
```bash
ollama run deepseek-coder-v2
```

### 2. Python Client
I've set up a Python environment in your folder to interact with the model programmatically.

**Files Created:**
- `client.py`: A sample script to send prompts to DeepSeek.
- `chat.py`: An interactive chat script with conversation memory.
- `venv/`: Virtual environment with dependencies installed.

**How to Run Python Script:**
Run the following command in your terminal:
```bash
# Activate virtual environment and run script
source venv/bin/activate
python client.py
```

### 3. Interactive Chat with Memory (`chat.py`)
I've also created `chat.py`, which remembers your conversation history (unlike `client.py` which is one-off).

**How to Run:**
```bash
source venv/bin/activate
python chat.py
```
- Type your message and press Enter.
- Type `quit` or `exit` to stop.

### 4. Chat with PDF (`rag.py`)
I've implemented a RAG system to chat with your PDF.

**How to Run:**
```bash
source venv/bin/activate
python rag.py
```

## Quick Verification
You can also run a one-off prompt without entering interactive mode:
```bash
ollama run deepseek-coder-v2 "Write a Python Hello World"
```

## Model Details
- **Model**: DeepSeek-Coder-V2 (Lite Instruct)
- **Size**: ~16B parameters
- **Performance**: Optimized for Apple Silicon (M-series chips).
- **RAM Usage**: Efficient (~9-11GB), leaving plenty of room on your 24GB Mac.

## Resources
- [Ollama Documentation](https://github.com/ollama/ollama)
- [DeepSeek Coder V2 Info](https://github.com/deepseek-ai/DeepSeek-Coder-V2)
