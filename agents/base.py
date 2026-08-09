import requests

MODEL = "tinyllama"
OLLAMA_URL = "http://localhost:11434/api/generate"

def call_llm(prompt: str, temperature: float = 0.7) -> str:
    """
    Call Ollama with the configured model
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
            },
            timeout=180   # code reviews can take a while on CPU with max_tokens=1000
        )
        return response.json()["response"].strip()
    except Exception as e:
        return f"Error: {str(e)}"