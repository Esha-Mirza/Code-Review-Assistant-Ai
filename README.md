<h1 align="center">CodeLens AI</h1>

<p align="center">
  <strong>Local AI-powered code review for developers.</strong>
</p>

<p align="center">
  Review source code with a locally hosted language model and receive structured feedback on bugs, improvements, optimizations, best practices, and overall code quality — without relying on a cloud-based LLM API.
</p>

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/python-3.8%2B-3776AB?logo=python&logoColor=white" alt="Python 3.8+">
  </a>
  <a href="https://ollama.com/">
    <img src="https://img.shields.io/badge/Ollama-local%20LLM-black?logo=ollama&logoColor=white" alt="Ollama">
  </a>
  <a href="https://fastapi.tiangolo.com/">
    <img src="https://img.shields.io/badge/FastAPI-backend-009688?logo=fastapi&logoColor=white" alt="FastAPI">
  </a>
  <a href="https://streamlit.io/">
    <img src="https://img.shields.io/badge/Streamlit-frontend-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit">
  </a>
  <img src="https://img.shields.io/badge/LLM-DeepSeek--Coder-blueviolet" alt="DeepSeek-Coder">
</p>

---

## Overview

CodeLens AI is a local AI-assisted code review application that analyzes source code and generates structured developer feedback.

The application combines a **Streamlit frontend**, **FastAPI backend**, **Ollama model runtime**, and an agent layer to create a simple workflow:

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
Agent / Prompt Layer
     │
     ▼
Ollama
     │
     ▼
Local LLM
     │
     ▼
Code Review
     │
     ▼
Streamlit Interface
```

The current review workflow asks the model to evaluate four areas:

* Bugs
* Improvements
* Optimization tips
* Best-practice recommendations

The backend also requests an **overall score out of 10**, giving the review a concise quality signal in addition to detailed feedback.

---

## Why CodeLens AI?

Code review is an important part of software development, but getting a second opinion on every function or code change can be time-consuming.

CodeLens AI provides an additional automated review pass before code reaches a human reviewer.

The local-first architecture is particularly useful when experimenting with source code that developers prefer to keep within their own development environment.

Instead of sending code to a hosted AI service:

```text
Application
     │
     ▼
Internet
     │
     ▼
Cloud LLM
     │
     ▼
Response
```

CodeLens AI can process the request through a locally running model:

```text
Application
     │
     ▼
FastAPI
     │
     ▼
Ollama
     │
     ▼
Local LLM
     │
     ▼
Response
```

This also avoids per-request API charges when using local inference.

---

## Features

### Code Analysis

Analyzes submitted source code for potential issues and improvement opportunities.

### Structured Reviews

Reviews are organized into:

```text
Bugs
Improvements
Optimizations
Best Practices
Overall Score
```

This structure is defined directly in the backend prompt sent to the model.

### Multiple Programming Languages

The frontend currently provides language selection for:

```text
Python
JavaScript
Java
C++
C#
Go
Rust
TypeScript
```

The selected language is passed to the backend and incorporated into the review prompt.

### Local LLM Inference

The application uses Ollama as the local model runtime, allowing the model to run on the developer's own machine.

### FastAPI Backend

A lightweight REST API separates the user interface from the code-review logic.

### Streamlit Interface

A browser-based interface provides:

* Programming-language selection
* Code input
* Review execution
* Review results
* Review download

The frontend can download the generated review as a text file.

### No Cloud API Requirement

The core review workflow communicates with a locally running Ollama instance rather than requiring a hosted LLM API.

---

## Architecture

CodeLens AI is divided into several components.

```text
                         CodeLens AI
                              │
                ┌─────────────┴─────────────┐
                │                           │
                ▼                           ▼
        Streamlit Frontend            FastAPI Backend
                │                           │
                │ HTTP POST                 │
                └─────────────►─────────────┘
                                            │
                                            ▼
                                     Agent Layer
                                            │
                                            ▼
                                         Ollama
                                            │
                                            ▼
                                      Local LLM
                                            │
                                            ▼
                                      Review Result
                                            │
                                            ▼
                                    Streamlit Output
```

### Frontend

The Streamlit application handles the user interaction layer.

The user selects a programming language, enters source code, and submits it for review.

The frontend sends the code and selected language to:

```text
POST /review/
```

It then displays the generated review and provides a download option.

### Backend

The FastAPI application exposes the code-review endpoint.

The current backend defines:

```text
GET  /
POST /review/
```

The root endpoint provides a simple API status message, while `/review/` accepts the source code and programming language and generates the review.

### Agent Layer

The backend imports the LLM interaction through:

```python
from agents.base import call_llm
```

This keeps model communication separate from the FastAPI route itself and provides a natural extension point for more sophisticated agent behavior.

### Model Layer

Ollama provides the local inference runtime.

The model can be selected according to the available hardware and the model installed locally.

---

## Review Pipeline

A complete review request follows this sequence:

```text
1. User enters source code
             │
             ▼
2. User selects language
             │
             ▼
3. Streamlit sends HTTP request
             │
             ▼
4. FastAPI receives code + language
             │
             ▼
5. Review prompt is constructed
             │
             ▼
6. Agent layer calls the local LLM
             │
             ▼
7. Model analyzes the source code
             │
             ▼
8. Structured review is returned
             │
             ▼
9. Streamlit displays the result
```

The backend explicitly constructs a review prompt containing the selected programming language and requested review categories.

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

### Possible Review

```text
### Bugs

- Potential ZeroDivisionError if numbers is empty.

### Improvements

- Use sum(numbers) instead of manually accumulating the values.
- Add type annotations to clarify the expected input and return type.

### Optimizations

- The manual loop can be replaced with Python's built-in sum() function.
- statistics.mean() could be considered when appropriate.

### Best Practices

- Add a docstring explaining the function.
- Define the expected input and return types.

### Overall Score

- Score: 7/10
```

The exact output will vary depending on the selected model and the source code being reviewed.

---

## Quick Start

### Requirements

Before running CodeLens AI, install:

| Requirement            | Purpose                           |
| ---------------------- | --------------------------------- |
| Python 3.8+            | Application runtime               |
| Ollama                 | Local LLM runtime                 |
| Compatible local model | Code analysis                     |
| 8 GB+ RAM              | Recommended for local inference   |
| ~4 GB+ storage         | Model storage, depending on model |

The repository currently documents Python 3.8+ and recommends at least 8 GB of RAM for local model execution.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Esha-Mirza/CodeLens-AI.git
cd CodeLens-AI
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Ollama

Install Ollama and make sure the local service is running.

Download the model you want to use.

For example:

```bash
ollama pull deepseek-coder
```

Or use a smaller model when working with limited hardware:

```bash
ollama pull deepseek-coder:1.3b
```

You can also use another compatible model supported by your configuration.

Check installed models with:

```bash
ollama list
```

The repository's existing documentation lists DeepSeek-Coder as the primary model and also mentions smaller alternatives such as `deepseek-coder:1.3b` and `phi3`.

---

## Running the Application

CodeLens AI consists of three processes:

```text
Terminal 1
    Ollama

Terminal 2
    FastAPI

Terminal 3
    Streamlit
```

### Start Ollama

```bash
ollama serve
```

### Start the FastAPI backend

```bash
uvicorn backend.main:app --reload
```

The API will be available at:

```text
http://localhost:8000
```

Interactive FastAPI documentation:

```text
http://localhost:8000/docs
```

### Start the Streamlit frontend

Open another terminal:

```bash
streamlit run frontend/app.py
```

The application will be available at:

```text
http://localhost:8501
```

The frontend currently communicates with the backend at `localhost:8000/review/`.

---

## Usage

1. Start Ollama.
2. Start the FastAPI backend.
3. Start the Streamlit frontend.
4. Open `http://localhost:8501`.
5. Select the programming language.
6. Paste the code you want to review.
7. Select **Review Code**.
8. Wait for the local model to generate the analysis.
9. Review the results.
10. Download the generated review if needed.

The current Streamlit interface includes a code editor, language selector, review button, result display, and review download functionality.

---

## API

### `GET /`

Returns a basic API status response.

Example:

```json
{
  "message": "Code Review Assistant API"
}
```

### `POST /review/`

Analyzes submitted source code.

The endpoint accepts form data containing:

```text
code
language
```

Example request:

```text
POST /review/

code=def hello_world():
    print("Hello World")

language=Python
```

Example response:

```json
{
  "review": "### Bugs\n..."
}
```

The endpoint is implemented using FastAPI's form handling and passes the selected language into the review prompt.

---

## Model Configuration

The model is accessed through the agent layer rather than directly from the frontend.

This separation allows the model implementation to evolve without requiring changes to the Streamlit interface.

For local model management:

```bash
ollama list
```

Download a model:

```bash
ollama pull <model-name>
```

Run a model directly:

```bash
ollama run <model-name>
```

For lower-resource systems, smaller models can reduce inference time and memory requirements at the cost of potentially weaker code-analysis quality.

---

## Changing Ports

### FastAPI

Default:

```text
8000
```

Run on another port:

```bash
uvicorn backend.main:app --reload --port 8001
```

### Streamlit

Default:

```text
8501
```

Run on another port:

```bash
streamlit run frontend/app.py --server.port 8502
```

If the backend port changes, update the frontend's backend URL accordingly.

---

## Project Structure

```text
CodeLens-AI/
│
├── agents/
│   └── LLM / agent components
│
├── backend/
│   └── main.py
│       └── FastAPI application
│
├── frontend/
│   └── app.py
│       └── Streamlit interface
│
├── requirements.txt
├── .gitignore
└── README.md
```

### `agents/`

Contains the model/agent interaction layer used by the backend.

### `backend/main.py`

Defines the FastAPI application and `/review/` endpoint.

### `frontend/app.py`

Defines the Streamlit interface and communicates with the FastAPI backend.

### `requirements.txt`

Contains the Python dependencies required by the project.

---

## Supported Languages

The current interface provides the following language options:

```text
Python
JavaScript
Java
C++
C#
Go
Rust
TypeScript
```

The selected language is included in the model prompt so the review can be framed around the appropriate programming language.

---

## Local-First Design

CodeLens AI is designed around local model execution.

With Ollama running locally, the application does not need to send the source code to a hosted LLM provider for the core review workflow.

This provides two practical benefits:

**Local processing**

Source code can remain within the local development environment when the entire stack is configured locally.

**No per-request cloud inference cost**

Using a locally hosted model avoids usage-based API charges from external LLM providers.

These benefits come with a tradeoff: inference speed and review quality depend on the hardware and model available on the machine.

---

## Performance

Local LLM inference can be computationally expensive.

Performance depends on:

* Model size
* CPU performance
* GPU availability
* Available RAM
* Source-code length
* Model quantization
* Concurrent requests

For faster responses on lower-end systems, consider using a smaller compatible model.

For more detailed analysis, a larger code-specialized model may produce better results but require more computational resources.

---

## Limitations

AI-generated code reviews should be treated as an additional development aid rather than a definitive assessment of code quality.

The model may:

* Miss real bugs
* Report false positives
* Recommend unnecessary changes
* Misunderstand application-specific requirements
* Produce incorrect optimization advice
* Lack context about the wider codebase

CodeLens AI should therefore complement, rather than replace:

* Human code review
* Unit and integration tests
* Linters
* Static analysis
* Security scanners
* Application-specific testing

---

## Roadmap

The current project provides a foundation for a more complete AI-assisted developer tool.

Potential future improvements include:

* [ ] Review complete files and directories
* [ ] Git diff analysis
* [ ] Pull-request review
* [ ] Severity levels for findings
* [ ] Security-focused code analysis
* [ ] Code smell detection
* [ ] Complexity analysis
* [ ] Automated test suggestions
* [ ] Refactoring suggestions
* [ ] Downloadable Markdown/PDF reports
* [ ] Review history
* [ ] Support for additional local models
* [ ] GitHub integration
* [ ] CI/CD integration
* [ ] IDE integration

---

## Troubleshooting

### Ollama connection refused

Make sure the Ollama service is running:

```bash
ollama serve
```

Then verify:

```bash
ollama list
```

### Model not found

Download the required model:

```bash
ollama pull deepseek-coder
```

### Backend connection error

Start FastAPI:

```bash
uvicorn backend.main:app --reload
```

Then check:

```text
http://localhost:8000/docs
```

### Frontend cannot connect to backend

Make sure the backend is running on the port configured in `frontend/app.py`.

The current frontend expects:

```text
http://localhost:8000/review/
```

### Slow inference

Try a smaller local model:

```bash
ollama pull deepseek-coder:1.3b
```

Also consider reviewing smaller code snippets rather than very large files.

### Missing Python dependencies

Reinstall:

```bash
pip install -r requirements.txt
```

---

## Design Decisions

### Why FastAPI?

FastAPI keeps the model-processing layer independent from the user interface and provides a straightforward HTTP API for future integrations.

### Why Streamlit?

Streamlit makes it possible to build a functional developer interface in Python without introducing a separate frontend framework.

### Why Ollama?

Ollama provides a convenient local runtime for experimenting with and deploying open-weight language models on a developer workstation.

### Why a separate agent layer?

Keeping LLM interaction behind the `agents` layer makes the application easier to extend with different models, prompts, routing logic, or specialized review agents.

---

## Future Extensions

The current architecture can evolve from a code-snippet reviewer into a broader developer-assistance platform.

A possible future architecture could look like:

```text
                         CodeLens AI
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
          ▼                   ▼                   ▼
     Code Review          Security Review    Test Generation
          │                   │                   │
          └───────────────────┼───────────────────┘
                              │
                              ▼
                         Local LLM
                              │
                              ▼
                         Review Report
```

This would allow the same local inference infrastructure to support multiple software-engineering workflows.

---

## Contributing

Contributions are welcome.

To contribute:

```bash
git checkout -b feature/your-feature
```

Make your changes, then:

```bash
git add .
git commit -m "feat: describe your change"
git push origin feature/your-feature
```

Open a pull request with:

* A description of the change
* The motivation behind it
* Testing performed
* Any configuration changes required

---

## License

This project is licensed under the MIT License.

See `LICENSE` for details.

---

## Acknowledgments

* [Ollama](https://ollama.com/) — Local LLM runtime
* [DeepSeek](https://www.deepseek.com/) — Code-focused language models
* [FastAPI](https://fastapi.tiangolo.com/) — Backend API framework
* [Streamlit](https://streamlit.io/) — Python application framework

---

## Author

**Esha Mirza**

[GitHub](https://github.com/Esha-Mirza)

---

<p align="center">
  <strong>CodeLens AI</strong><br>
  Local AI-assisted code review for developers.
</p>
