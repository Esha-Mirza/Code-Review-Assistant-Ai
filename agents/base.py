import requests

MODEL = "phi3"
OLLAMA_URL = "http://localhost:11434/api/generate"

def call_llm(prompt: str, temperature: float = 0.7) -> str:
    """
    Call Ollama with Phi-3 model
    """
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False,
                "temperature": temperature,
                "max_tokens": 1000
            }
        )
        return response.json()["response"].strip()
    except Exception as e:
        return f"Error: {str(e)}"