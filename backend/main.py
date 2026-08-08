from fastapi import FastAPI, Form
import requests
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents.base import call_llm

app = FastAPI(title="Code Review Assistant", version="1.0.0")

@app.get("/")
def root():
    return {"message": "Code Review Assistant API"}

@app.post("/review/")
def review_code(code: str = Form(...), language: str = Form("Python")):
    prompt = f"""
You are a senior developer. Review the following {language} code for:
1. Bugs
2. Improvements
3. Optimization tips
4. Best-practice recommendations

Format your response as:

### Bugs
- [List any bugs found]

### Improvements
- [List improvements]

### Optimizations
- [List optimizations]

### Best Practices
- [List best practices]

### Overall Score
- Score: X/10

Code to review:
{code}

Review:
"""
    
    review = call_llm(prompt)
    return {"review": review}