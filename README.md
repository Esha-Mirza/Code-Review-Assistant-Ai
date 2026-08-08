# Code Review Assistant AI

An AI-powered code review application that uses a locally hosted DeepSeek-Coder model to analyze code for bugs, improvements, and optimization tips.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Ollama](https://img.shields.io/badge/LLM-Ollama-black)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

---

## Overview

This application leverages Large Language Models (LLMs) to automatically review source code, identify potential bugs, suggest improvements, and recommend optimizations. It is designed for developers, engineering teams, and students who want to improve code quality and learn best practices.

The application runs entirely locally, ensuring code privacy and eliminating API costs. It uses Ollama to host the DeepSeek-Coder model, FastAPI for the backend API, and Streamlit for the user interface.

---

## Features

- **Code Analysis** — Detects bugs, suggests improvements, and recommends optimizations
- **Multiple Language Support** — Works with Python, JavaScript, Java, C++, Go, Rust, and more
- **Local LLM Inference** — Runs the DeepSeek-Coder model locally using Ollama
- **FastAPI Backend** — Provides a RESTful API for code review
- **Streamlit Frontend** — Clean, intuitive user interface with language selection
- **Privacy-Focused** — All processing happens locally, no code is sent to external servers
- **No API Costs** — Free to use with no usage limits

---

## Technology Stack

| Technology | Purpose |
|---|---|
| **Ollama** | Local LLM hosting and inference |
| **DeepSeek-Coder** | Code-specialized Large Language Model |
| **FastAPI** | Backend API framework |
| **Streamlit** | Frontend user interface |
| **Requests** | HTTP client for API communication |
| **Uvicorn** | ASGI server for FastAPI |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Python** | Version 3.8 or higher |
| **Ollama** | Installed and running |
| **DeepSeek-Coder Model** | Downloaded via Ollama |
| **RAM** | 8GB+ recommended |
| **Storage** | 4GB+ free space for model |

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Esha-Mirza/School_Of_AI_Internship.git
cd School_Of_AI_Internship/"Project-4 Code Review Deepseek"
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Pull DeepSeek-Coder Model via Ollama

```bash
ollama pull deepseek-coder
```

This downloads the DeepSeek-Coder model (~3.8 GB). Alternatively, you can use a smaller model:

```bash
ollama pull deepseek-coder:1.3b    # 776 MB, faster but less capable
ollama pull phi3                    # 2.2 GB, faster inference
```

---

## Running the Application

**Terminal 1: Start Ollama Service**

```bash
ollama serve
```

**Terminal 2: Start Backend (FastAPI)**

```bash
uvicorn backend.main:app --reload
```

The backend will be available at: `http://localhost:8000`

**Terminal 3: Start Frontend (Streamlit)**

```bash
streamlit run frontend/app.py
```

The frontend will open at: `http://localhost:8501`

---

## Usage

1. Open your browser and navigate to `http://localhost:8501`
2. Select the programming language
3. Paste your code in the text area
4. Click the **Get Review** button
5. Review the AI-generated feedback

### Sample Input (Python)

```python
def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total / len(numbers)

result = calculate_average([1, 2, 3, 4, 5])
print("Average:", result)
```

**Expected Output:**

```text
## Code Review

### Bugs
- Potential ZeroDivisionError: The function does not handle empty lists.

### Improvements
- Use `sum(numbers)` instead of manual loop.
- Use `len(numbers)` directly.

### Optimizations
- Consider using `statistics.mean()` from the standard library.

### Best Practices
- Add type hints: `def calculate_average(numbers: list[float]) -> float:`
- Add docstring to explain the function purpose.
```

### Sample Input (JavaScript)

```javascript
function getUserData(id) {
    const user = database.find(u => u.id === id);
    return user.name;
}
```

**Expected Output:**

```text
## Code Review

### Bugs
- No error handling if user is not found.
- `database` is not defined or imported.

### Improvements
- Add null check: `if (!user) return null;`
- Use `try/catch` for error handling.

### Best Practices
- Add JSDoc comments.
- Consider using async/await if database call is asynchronous.
```

---

## API Endpoints

### `POST /review/`

**Request:**

```json
{
  "code": "Your code to review..."
}
```

**Response:**

```json
{
  "review": "Generated review text..."
}
```

---

## Project Structure

```
Project-4 Code Review Deepseek/
├── backend/
│   └── main.py          # FastAPI implementation
├── frontend/
│   └── app.py           # Streamlit UI
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## Configuration

### Changing the Model

To use a different model, modify `backend/main.py`:

```python
"model": "deepseek-coder:1.3b",   # Smaller, faster
"model": "phi3",                  # Alternative model
```

### Changing the Port

**Backend Port** (default: 8000):

```bash
uvicorn backend.main:app --reload --port 8001
```

**Frontend Port** (default: 8501):

```bash
streamlit run frontend/app.py --server.port 8502
```

---

## Troubleshooting

| Issue | Solution |
|---|---|
| Model not found | Run `ollama pull deepseek-coder` to download the model |
| Connection refused | Ensure Ollama is running (`ollama serve`) |
| Port already in use | Use `--port` flag to specify a different port |
| Module not found | Run `pip install -r requirements.txt` |
| Slow inference | Switch to a smaller model like `deepseek-coder:1.3b` or `phi3` |

---

## Roadmap

- [ ] Add support for reviewing entire files/folders instead of pasted snippets
- [ ] Add severity levels to flagged issues (critical / warning / suggestion)
- [ ] Add downloadable review report (Markdown/PDF export)

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Acknowledgments

- [Ollama](https://ollama.com/) - Local LLM runtime
- DeepSeek - DeepSeek-Coder model
- FastAPI - Web framework
- Streamlit - UI framework

---

## Contact

- **GitHub:** [Esha-Mirza](https://github.com/Esha-Mirza)
- **Email:** esha101374@gmail.com
