
# GitBuddy-AI Tech Stack (v1.0.3)

## Backend
- **Python 3.13**: Core language for scripts and backend logic.
- **GitPython 3.1.44**: Manages GitHub repositories.
- **PyGithub 2.4.0**: Interacts with GitHub API for repository updates.
- **Ollama 0.3.12**: Local LLM for 5% simple tasks (e.g., commit message generation).
- **xAI’s Grok API**: For 98% complex tasks (e.g., code analysis), ~₹664/month (within ₹6000 budget).
- **python-dotenv**: Loads PAT and credentials from `.env` for security.

## Frontend
- **Streamlit 1.38.0**: Layman-friendly dashboard, now enhanced with AG-UI streaming.
- **AG-UI Protocol (CopilotKit SDK)**: Streams real-time events (e.g., `TEXT_MESSAGE_CONTENT`) for interactive UI features.

## Training and Self-Adaptive Features
- **JSONL Format**: Stores training data in `data/training.jsonl` for LLM fine-tuning and cross-project reuse.
- **AG-UI Event Handler**: Processes events (`STATE_DELTA`, `USER_CONFIRMATION_REQUEST`) for self-suring/healing/evolving.
- **Logging**: Stores health metrics (`logs/health_metrics.log`) and healing actions (`logs/healing_actions.log`).

## Hardware Optimization
- **Lightweight Design**: AG-UI streaming uses <200MB RAM, suitable for 12GB RAM laptops.
- **API-Heavy**: Offloads complex tasks to Grok API, minimizing local CPU usage.
- **Training Schedule**: Fine-tunes Ollama during idle periods (e.g., overnight), keeping resource usage low.

## Layman Comment
This is your ship’s toolkit, Anil, now with smarter tools (AG-UI, Ollama) to make your voyage smoother and safer!
