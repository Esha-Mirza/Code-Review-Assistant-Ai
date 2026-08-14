# CodeLens AI

AI-powered code review that runs locally with Ollama.

Paste a function, module, or complete code snippet and get structured feedback on potential bugs, code quality, optimization opportunities, and development practices — without sending your source code to a hosted LLM API.

```text
                 Your Source Code
                        │
                        ▼
              ┌──────────────────┐
              │   Streamlit UI   │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │   FastAPI API    │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │     Ollama       │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │      Phi-3       │
              │   Code Analysis  │
              └────────┬─────────┘
                       │
                       ▼
              Structured Review
```

---

## Why this exists

Code review is one of the most valuable parts of software development, but it is also one of the easiest stages to delay.

A developer may want a second opinion before opening a pull request, debugging an unfamiliar function, or refactoring an existing implementation. Cloud-based coding assistants can help, but they are not always suitable when source code needs to remain on the local machine.

CodeLens AI provides a local first-pass reviewer.

The application sends source code to a locally running language model through Ollama and returns a structured analysis that can help identify problems before human review.

The goal is not to replace experienced developers or formal testing. It is to make an additional code-review pass inexpensive, accessible, and easy to run during development.

---

## What it reviews

CodeLens AI organizes its analysis around four primary areas:

| Category           | Purpose                                                      |
| ------------------ | ------------------------------------------------------------ |
| **Bugs**           | Identify potential logical and implementation errors         |
| **Improvements**   | Suggest clearer or more maintainable approaches              |
| **Optimizations**  | Identify opportunities to simplify or improve implementation |
| **Best Practices** | Recommend language and software-engineering practices        |

A typical review can therefore move beyond simply answering “does this code work?” and instead ask:

```text
Does it work?
    │
    ├── Are there bugs?
    ├── Is the implementation maintainable?
    ├── Can it be simplified?
    ├── Are there performance concerns?
    └── Does it follow reasonable development practices?
```

---

## Quick start

### 1. Install the project

```bash
git clone https://github.com/Esha-Mirza/Code-Review-Assistant-Ai.git
cd Code-Review-Assistant-Ai

python -m venv venv
```

Activate the environment.

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 2. Start Ollama

Install [Ollama](https://ollama.com/) and make sure the local service is running.

Pull the model used by the application:

```bash
ollama pull phi3
```

Verify the installation:

```bash
ollama list
```

### 3. Start the backend

From the project root:

```bash
uvicorn backend.main:app --reload
```

The API will be available at:

```text
http://localhost:8000
```

FastAPI's interactive documentation will be available at:

```text
http://localhost:8000/docs
```

### 4. Start the frontend

In another terminal:

```bash
streamlit run frontend/app.py
```

Then open:

```text
http://localhost:8501
```

---

## Example

Suppose you submit:

```python
def find_user(users, user_id):
    for user in users:
        if user["id"] == user_id:
            return user
```

CodeLens AI can analyze the implementation and return feedback such as:

```text
Bugs
- The function assumes every item in users contains an "id" key.
- A malformed user object can raise a KeyError.

Improvements
- Consider using user.get("id") when the input structure is not guaranteed.
- Add type annotations for better readability and tooling support.

Best Practices
- Document the expected structure of users.
- Define the return type explicitly.
```

The generated response depends on the local model and the code supplied for review.

---

## How it works

CodeLens AI is split into three primary layers:

```text
┌─────────────────────────────────────────┐
│              Frontend                   │
│                                         │
│              Streamlit                  │
│                                         │
│  Code Input → Language → Review Output  │
└────────────────────┬────────────────────┘
                     │
                     │ HTTP
                     ▼
┌─────────────────────────────────────────┐
│               Backend                   │
│                                         │
│               FastAPI                   │
│                                         │
│       Request → Validation → Model      │
└────────────────────┬────────────────────┘
                     │
                     │ Local inference
                     ▼
┌─────────────────────────────────────────┐
│             Model Runtime               │
│                                         │
│                Ollama                   │
│                    │                    │
│                  Phi-3                   │
│                    │                    │
│              Code Analysis              │
└─────────────────────────────────────────┘
```

### Frontend

The Streamlit frontend provides the interactive interface for submitting source code and displaying the generated review.

### Backend

The FastAPI backend acts as the application API.

It receives the submitted code, prepares the model request, communicates with Ollama, and returns the generated review.

### Model runtime

Ollama provides the local inference layer.

The language model is responsible for interpreting the source code and generating the review.

Keeping these responsibilities separate means the interface can be changed without redesigning the model layer, and the model can be replaced without rebuilding the frontend.

---

## Request flow

A review request follows this path:

```text
User
 │
 │ source code
 ▼
Streamlit
 │
 │ HTTP request
 ▼
FastAPI
 │
 │ prompt + source code
 ▼
Ollama
 │
 ▼
Phi-3
 │
 │ generated analysis
 ▼
FastAPI
 │
 │ response
 ▼
Streamlit
 │
 ▼
User
```

The application therefore separates **presentation**, **API handling**, and **model inference** rather than putting the complete workflow into a single application component.

---

## Project structure

```text
Code-Review-Assistant-Ai/
│
├── agents/
│   └── AI review / agent components
│
├── backend/
│   └── FastAPI application
│
├── frontend/
│   └── Streamlit application
│
├── requirements.txt
├── .gitignore
└── README.md
```

### `agents/`

Contains the AI-related components used by the review workflow.

### `backend/`

Contains the FastAPI application responsible for handling review requests and communicating with the local model runtime.

### `frontend/`

Contains the Streamlit interface used to interact with the application.

---

## Model configuration

The application uses Ollama as the local model runtime.

The model can be changed depending on the hardware available on the host machine and the models supported by the application.

For example:

```bash
ollama list
```

To download a model:

```bash
ollama pull phi3
```

To test the model independently:

```bash
ollama run phi3
```

If you change the configured model, make sure the model name used by the application matches the model installed in Ollama.

---

## API

The backend exposes the code-review functionality through FastAPI.

Once the backend is running, open:

```text
http://localhost:8000/docs
```

This provides an interactive API interface for inspecting and testing the available endpoints.

The API layer makes the review engine usable independently of the Streamlit interface and leaves room for future integrations such as:

* IDE extensions
* Git hooks
* CI/CD pipelines
* GitHub pull-request automation
* Other web interfaces

---

## Local inference

One of the main design choices in CodeLens AI is the use of local model inference.

Instead of:

```text
Application
    │
    ▼
Internet
    │
    ▼
Hosted LLM
    │
    ▼
Response
```

the project uses:

```text
Application
    │
    ▼
Local API
    │
    ▼
Ollama
    │
    ▼
Local Model
    │
    ▼
Response
```

This approach can be useful when working with source code that developers prefer not to send to an external model provider.

Local inference also removes the need for a per-request hosted LLM API subscription, although model performance depends on the hardware available locally.

---

## Supported review scenarios

CodeLens AI can be used as a first-pass reviewer for several development workflows.

### Before committing

Paste a newly written function into the reviewer to identify obvious problems before committing.

### Before opening a pull request

Use the reviewer as an additional automated pass before requesting human review.

### Refactoring

Submit an existing implementation and ask the model to identify opportunities for simplification or maintainability improvements.

### Learning

Use the generated feedback to understand why a particular implementation could be improved.

### Debugging

Provide suspicious or recently modified code and use the generated analysis as another source of hypotheses.

---

## Configuration and environment

The application is designed to run against a locally available Ollama instance.

The basic setup is:

```text
Python Application
       │
       ▼
FastAPI
       │
       ▼
Ollama
       │
       ▼
Local Model
```

Make sure Ollama is available before submitting review requests.

If Ollama is running on a non-default host or port, the corresponding backend configuration should be updated accordingly.

---

## Performance considerations

Local inference performance depends primarily on the selected model and available hardware.

Important factors include:

* CPU performance
* GPU availability
* Available RAM
* Model size
* Input source-code length
* Concurrent requests

For larger source files, model response time can increase significantly.

A practical workflow is therefore to review focused modules, functions, or diffs rather than submitting an entire large repository in one request.

---

## Limitations

CodeLens AI is an AI-assisted review tool, not a replacement for human code review, testing, static analysis, or security tooling.

Generated feedback may contain:

* False positives
* Missed issues
* Incorrect assumptions
* Incomplete understanding of application context
* Recommendations that are inappropriate for a specific codebase

AI-generated suggestions should therefore be treated as recommendations and validated against the actual application requirements.

For production systems, CodeLens AI should complement—not replace—automated tests, linters, static analyzers, security scanners, and experienced human reviewers.

---

## Roadmap

Potential improvements include:

* Repository-level review
* Git diff analysis
* Pull-request review
* Severity classification
* Security-focused analysis
* Code smell detection
* Complexity analysis
* Automated test recommendations
* Refactoring suggestions
* Review history
* Multiple local model support
* GitHub integration
* CI/CD integration
* IDE integration
* Streaming model responses

---

## Development

Create a development branch:

```bash
git checkout -b feature/your-feature
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

Run the backend:

```bash
uvicorn backend.main:app --reload
```

Run the frontend:

```bash
streamlit run frontend/app.py
```

After making changes:

```bash
git add .
git commit -m "feat: describe your change"
git push origin feature/your-feature
```

---

## Contributing

Contributions are welcome.

If you find a bug, have an improvement, or want to add support for another model or integration, open an issue or submit a pull request.

When submitting a pull request, include:

* What changed
* Why the change was needed
* How it was tested
* Any configuration changes required

---

## License

MIT License

See the `LICENSE` file for details.

---

## Author

**Esha Mirza**

[GitHub](https://github.com/Esha-Mirza)

---

## Built with

[Ollama](https://ollama.com/) · [FastAPI](https://fastapi.tiangolo.com/) · [Streamlit](https://streamlit.io/) · [Python](https://www.python.org/)
