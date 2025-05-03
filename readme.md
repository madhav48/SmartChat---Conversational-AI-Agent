# Conversational AI Chat

This project is an **end-to-end Conversational AI system** built using **FastAPI**, **Gradio**, and **OpenRouter**-powered Large Language Models (LLMs). It allows real-time chat with an AI assistant and supports dynamic switching between different LLM providers via both configuration and UI.

---

## Prerequisites

Make sure the following tools are installed:

- **Python (>=3.9)** – [Download here](https://www.python.org/downloads/)
- **Visual Studio Code (VSCode)** – [Download here](https://code.visualstudio.com/)

---

## VM Setup (Windows)

### Step-by-Step Setup:

1. **Colne the repository**

  ```bash
   git clone https://github.com/madhav48/SmartChat---Conversational-AI-Agent.git
   ```

   After cloning, open **VSCode**, and open the **root directory** of the project (where `readme.md` and `app/` folder reside).

2. **Create a Virtual Environment**

   ```bash
   python -m venv .venv
   ```

3. **Activate the Virtual Environment**

   Run this in the terminal:

   ```bash
   .venv\Scripts\Activate.ps1
   ```

   > If you encounter a **permission error**, first run the following command:
   >
   > ```bash
   > powershell -NoProfile -ExecutionPolicy Bypass
   > ```
   > Then retry activating the environment.

4. **Install Dependencies**

   Inside the activated virtual environment, run:

   ```bash
   pip install fastapi uvicorn gradio python-dotenv openai
   ```

5. **Configure API Keys**

   In the root directory, find the `.env` file and replace the placeholders (`...`) with your **OpenRouter API key**:

   ```env
   OPENROUTER_API_KEY=your_key_here
   ```

---

## Running the Application

### Step 1: Run the FastAPI Server

In the terminal (inside `.venv`):

```bash
uvicorn app.main:app --reload
```

Or press `F5` in VSCode (if configured with `launch.json`, provided in zip folder).

This starts the backend API server at:

```
http://127.0.0.1:8000
```

### Step 2: Launch the Gradio Frontend

In a **new terminal** (make sure to activate the virtual environment again):

```bash
.venv\Scripts\Activate.ps1
python app/frontend.py
```

Open your browser and go to:

```
http://localhost:7860/
```

You can now chat with the AI assistant through a clean and interactive chat UI! 

---

## LLM Switching Guide

You can dynamically switch between LLMs (e.g., DeepSeek, Microsoft Phi-4) using **two methods**:

### 1. **Environment Variable Configuration**

Before running the FastAPI app, edit the `.env` file and set:

```env
DEFAULT_LLM_PROVIDER=deepseek
```

Available options depend on your code mapping (e.g., `microsoft_phi4`, `deepseek`, `gemini`, etc.).

### 2. **Admin UI Panel**

While the FastAPI server is running, visit:

```
http://127.0.0.1:8000/admin/provider
```

Select the desired LLM provider from the dropdown and click **Change**. This lets you switch models at runtime without restarting the server.

---

## Notes

- **OpenAI & Anthropic Claude not used** in this project due to API cost restrictions.
- Instead, we’ve used **DeepSeek**, **Microsoft Phi-4**, and **Google Gemini** via **OpenRouter**.
- Make sure you have a valid OpenRouter API key to use these models.

---


# File Descriptions

| File | Description |
|------|-------------|
| `app/frontend.py` | Contains the Gradio UI/UX and chat interface code. Handles user input, streaming responses, and interaction with the FastAPI backend. |
| `app/llm_client.py` | Defines the base class `BaseLLMClient` for language model clients. All LLM-specific clients inherit from this. |
| `app/llm_client_gemini.py` | Implements the Gemini LLM client using OpenRouter API. Handles model communication and history formatting. |
| `app/llm_client_deepseek.py` | Implements the DeepSeek LLM client via OpenRouter. Another LLM option for generating responses. |
| `app/llm_client_ms_phi4.py` | Implements the Microsoft Phi-4 LLM client via OpenRouter. Lightweight, efficient model integration. |
| `app/llm_client_provider.py` | Contains logic to determine which LLM client to use based on the selected provider name (from `.env` or admin panel). |
| `app/main.py` | Acts as the MCP (Model Control Plane) server using FastAPI. Central control unit that handles model selection, chat history, and orchestration between Gradio and the LLM backend. |

---

## Thankyou!!
