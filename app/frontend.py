import gradio as gr
import requests
from gradio import ChatMessage

API_URL = "http://localhost:8000/chat"

def gradio_chat(message, history):
    # Convert Gradio ChatMessage list to OpenAI-style dicts
    formatted_history = [
        {"role": msg["role"], "content": msg["content"]}
        for msg in history
    ]

    # Call FastAPI backend
    resp = requests.post(API_URL, json={"message": message, "history": formatted_history})
    resp.raise_for_status()
    data = resp.json()


    # Extract only the last assistant message (the bot response)
    latest_bot_msg = data["response"]  # already just the last message content

    # Return just the bot's response (Gradio will handle appending it)
    return latest_bot_msg


iface = gr.ChatInterface(
    fn=gradio_chat,
    type = "messages",
    title="SmartChat: Your AI Agent"
)
iface.launch()
