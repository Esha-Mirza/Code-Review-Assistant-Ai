# CodeLens AI

### Local AI Code Review Assistant

CodeLens AI is an AI-powered code review application that uses a locally hosted large language model to analyze source code, identify potential issues, and provide actionable suggestions for improving code quality.

The application combines a **DeepSeek-Coder model running through Ollama**, a **FastAPI backend**, and a **Streamlit frontend** to provide a complete local code-review workflow.

---

## Overview

Code review is an essential part of software development, but manually reviewing every implementation can be time-consuming.

CodeLens AI provides an automated first-pass review by analyzing submitted source code and generating structured feedback covering potential bugs, improvements, optimizations, and development best practices.

The application runs the language model locally through Ollama, allowing source code to be processed on the user's own machine rather than requiring a hosted LLM API.

### Review Workflow

```text
Source Code
     │
     ▼
Streamlit Interface
     │
     ▼
FastAPI Backend
     │
     ▼
Ollama
     │
     ▼
DeepSeek-Coder
     │
     ▼
AI Code Analysis
     │
     ▼
Structured Review
     │
     ▼
Streamlit Interface
```

---

## Key Features

* AI-assisted source code review
* Local LLM inference through Ollama
* DeepSeek-Coder for code-focused analysis
* FastAPI REST backend
* Streamlit web interface
* Support for multiple programming languages
* Bug and issue identification
* Code improvement recommendations
* Optimization suggestions
* Best-practice recommendations
* No external LLM API required for inference
* Simple local development setup

---

## Architecture

CodeLens AI follows a simple separation-of-concerns architecture.

```text
┌──────────────────────────────┐
│        Streamlit UI          │
│                              │
│  Language Selection          │
│  Code Input                  │
│  Review Output               │
└──────────────┬───────────────┘
               │
               │ HTTP
               ▼
┌──────────────────────────────┐
│        FastAPI Backend       │
│                              │
│  Request Validation          │
│  Review Endpoint             │
│  Model Communication         │
└──────────────┬───────────────┘
               │
               │ Local API
               ▼
┌──────────────────────────────┐
│            Ollama            │
│                              │
│      Local Model Runtime     │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       DeepSeek-Coder         │
│                              │
│       Code Analysis          │
└──────────────────────────────┘
```

### Frontend

The Streamlit application provides the user-facing interface.

Users can:

1. Select a programming language.
2. Enter or paste source code.
3. Submit the code for analysis.
4. Review the generated feedback.

### Backend

The FastAPI application exposes the code-review API and manages communication between the frontend and local model runtime.

### Model Layer

Ollama provides the local model runtime, while DeepSeek-Coder performs the actual code-oriented language-model analysis.

---

## Review Categories

The generated review can be organized around several areas of software quality.

### Bugs

Potential logical errors, runtime problems, missing checks, and other implementation issues.

### Improvements

Suggestions for making the implementation clearer, safer, or easier to maintain.

### Optimizations

Potential opportunities to simplify implementation or improve efficiency.

### Best Practices

Recommendations related to readability, maintainability, type safety, error handling, documentation, and language-specific conventions.

---

## Example

### Input

```python
def calculate_average(numbers):
    total = 0

    for i in range(len(numbers)):
        total += numbers[i]

    return total / len(numbers)
```

### Example Review

```text
Code Review

Bugs
- Potential ZeroDivisionError when numbers is empty.

Improvements
- Use sum(numbers) instead of manually iterating through the list.
- Consider adding type annotations.

Optimizations
- The implementation can be simplified using Python's built-in functions.

Best Practices
- Add a docstring describing the function.
- Define an explicit return type.
- Validate the input before calculating the average.
```

The exact output depends on the selected local model and its generated response.

---

# Technology Stack

| Technology     | Purpose                     |
| -------------- | --------------------------- |
| Python         | Application development     |
| DeepSeek-Coder | Code-focused language model |
| Ollama         | Local model runtime         |
| FastAPI        | Backend REST API            |
| Streamlit      | Frontend interface          |
| Requests       | HTTP communication          |
| Uvicorn        | ASGI server                 |

---

# Project Structure

```text
Code-Review-Assistant-Ai/
│
├── agents/
│
├── backend/
│   └── main.py
│
├── frontend/
│   └── app.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

### `backend/`

Contains the FastAPI application and model interaction logic.

### `frontend/`

Contains the Streamlit user interface.

### `agents/`

Contains the project's agent-related components and supporting AI logic.

### `requirements.txt`

Defines the Python dependencies required to run the application.

---

# Requirements

Before running CodeLens AI, make sure the following are installed:

* Python 3.8 or newer
* Ollama
* DeepSeek-Coder or another compatible local model
* 8 GB+ RAM recommended
* Approximately 4 GB+ available storage for the model

Larger models may require significantly more memory and storage.

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Esha-Mirza/Code-Review-Assistant-Ai.git

cd Code-Review-Assistant-Ai
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configure Ollama

Install Ollama and make sure the service is running.

Pull the model used by the project:

```bash
ollama pull deepseek-coder
```

Verify the model:

```bash
ollama list
```

Start the Ollama service if required:

```bash
ollama serve
```

> If the project configuration uses a different model tag, use that model instead.

---

# Running the Application

CodeLens AI uses separate processes for the model runtime, backend, and frontend.

## 1. Start Ollama

```bash
ollama serve
```

---

## 2. Start the FastAPI Backend

Open another terminal:

```bash
uvicorn backend.main:app --reload
```

The backend will be available at:

```text
http://localhost:8000
```

FastAPI also provides interactive API documentation at:

```text
http://localhost:8000/docs
```

---

## 3. Start the Streamlit Frontend

Open another terminal:

```bash
streamlit run frontend/app.py
```

The frontend will be available at:

```text
http://localhost:8501
```

---

# Using CodeLens AI

Once the application is running:

1. Open the Streamlit interface.
2. Select the programming language.
3. Paste the source code you want to analyze.
4. Submit the code for review.
5. Wait for the local model to process the request.
6. Review the generated analysis.

The complete request flow is:

```text
User
 │
 │ Source Code
 ▼
Streamlit
 │
 │ HTTP Request
 ▼
FastAPI
 │
 │ Model Request
 ▼
Ollama
 │
 ▼
DeepSeek-Coder
 │
 │ Generated Review
 ▼
FastAPI
 │
 ▼
Streamlit
 │
 ▼
User
```

---

# API

## `POST /review/`

Submits source code for AI-assisted review.

### Request

```json
{
  "code": "def example():\n    pass"
}
```

### Response

```json
{
  "review": "Generated code review..."
}
```

The endpoint is intended to provide a simple interface between the frontend and the local code-review model.

---

# Configuration

The model used by the application can be changed through the backend configuration.

For example:

```python
model = "deepseek-coder"
```

Depending on the available hardware, a smaller model may provide faster inference.

For example:

```bash
ollama pull deepseek-coder:1.3b
```

The appropriate model should be configured consistently between Ollama and the application.

---

# Performance Considerations

Because inference is performed locally, performance depends heavily on the available hardware and selected model.

Factors that affect response time include:

* Model size
* Available RAM
* CPU performance
* GPU availability
* Input code size
* Model quantization

For systems with limited resources, a smaller model can provide faster responses at the cost of potentially lower review quality.

---

# Privacy

When configured to use Ollama for local inference, the source code submitted to CodeLens AI is processed through the locally running model rather than being sent to a third-party hosted LLM API.

This makes local inference useful for development environments where keeping source code within the local machine is important.

Users should still review their own environment and configuration before processing sensitive or proprietary code.

---

# Troubleshooting

## Model Not Found

Check the installed Ollama models:

```bash
ollama list
```

If the required model is missing:

```bash
ollama pull deepseek-coder
```

---

## Ollama Connection Error

Make sure Ollama is running:

```bash
ollama serve
```

---

## Backend Connection Error

Start the FastAPI server:

```bash
uvicorn backend.main:app --reload
```

Then verify:

```text
http://localhost:8000/docs
```

---

## Frontend Cannot Connect to Backend

Make sure the backend is running on the expected port:

```text
http://localhost:8000
```

If the backend is running on another port, update the frontend configuration accordingly.

---

## Slow Model Responses

Try a smaller model:

```bash
ollama pull deepseek-coder:1.3b
```

Model performance will vary depending on the available hardware.

---

# Roadmap

Potential future improvements include:

* Repository-level code analysis
* Git diff and pull-request review
* Security vulnerability analysis
* Code smell detection
* Complexity analysis
* Automated test suggestions
* Refactoring recommendations
* Inline code annotations
* Review severity levels
* Review history
* Support for additional local LLMs
* GitHub integration
* GitLab integration
* Automated CI/CD code review

---

# Limitations

AI-generated code reviews should be treated as an additional development aid rather than a replacement for human review.

Model-generated feedback can contain:

* Incorrect recommendations
* False positives
* Missed bugs
* Incomplete context
* Language-specific inaccuracies

For production systems, AI-generated recommendations should be validated by developers and appropriate automated testing.

---

# Contributing

Contributions are welcome.

To contribute, create a feature branch:

```bash
git checkout -b feature/your-feature
```

Make your changes and commit them:

```bash
git add .

git commit -m "feat: describe your change"
```

Push the branch:

```bash
git push origin feature/your-feature
```

Then open a pull request with a description of the proposed changes.

---

# License

This project is licensed under the MIT License.

See the `LICENSE` file for details.

---

# Author

**Esha Mirza**

GitHub: [Esha-Mirza](https://github.com/Esha-Mirza)

---

## Related Technologies

* [Ollama](https://ollama.com/)
* [DeepSeek](https://www.deepseek.com/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Streamlit](https://streamlit.io/)

---

<p align="center">
  <strong>CodeLens AI</strong><br>
  Local AI-assisted code analysis for developers.
</p>
