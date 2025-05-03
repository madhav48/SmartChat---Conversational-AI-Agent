from .llm_client_gemini import GeminiClient
from .llm_client_deepseek import DeepSeekClient
from .llm_client_ms_phi4 import MS_PHI4Client

def get_llm_client(provider_name, api_key=None):
    if provider_name == "gemini":
        return GeminiClient()
    elif provider_name == "deepseek":
        return DeepSeekClient()
    elif provider_name == "microsoft_phi4":
        return MS_PHI4Client()
    else:
        raise ValueError(f"Unsupported provider: {provider_name}")