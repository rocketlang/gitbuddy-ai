
# GitBuddy-AI Project Documentation (v1.0.3)

## Overview
**GitBuddy-AI** automates GitHub project setup and management with 98% AI-driven tasks and 2% layman input, integrating with **CyberShield-Easy** and **RocketAutomation**. It’s designed to be a user-friendly Git/IDE assistant, now enhanced with AG-UI protocol for modular, self-adaptive features.

## Version History
- **v1.0.0 (May 14, 2025)**: Initial setup with repository creation, basic UI, and project prompt.
- **v1.0.1**: Added chat logs for reference.
- **v1.0.2**: Included layman feedback and updated README for Bhargavi/Indra.
- **v1.0.3 (May 14, 2025)**: Integrated AG-UI methodology for modular components, LLM-driven training, and self-suring/healing/evolving capabilities.

## Core Features (Updated with AG-UI)
- **Repo Creation**: AI creates GitHub repo with predefined structure.
- **File Population**: Generates minimal files (workflow, UI, AI logic, logs, docs).
- **Layman UI**: Streamlit dashboard with maritime-inspired prompts, now powered by AG-UI for real-time interaction (e.g., streaming commit messages).
- **Self-Suring**: AG-UI events (`STATE_DELTA`) monitor AI outputs (e.g., commit message quality) to ensure reliability.
- **Self-Healing**: AG-UI auto-corrects errors (e.g., reformats commit messages based on user feedback).
- **Self-Evolving**: AG-UI collects training data (e.g., user edits) to improve AI suggestions over time.
- **AI-Agnostic**: Portable data for LLMs like Ollama (5% simple tasks) and Grok (98% complex tasks).

## AG-UI Integration (New Methodology)
- **Modular Components**:
  - **Streaming Chat Widget**: Displays AI-generated commit messages in real-time, reusable across Rocketlang and Cybershield.
  - **Event Handler Hub**: Processes AG-UI events for self-suring/healing/evolving.
  - **Training Data Collector**: Captures user feedback for LLM training.
- **LLM-Driven Training**:
  - Collects user edits via `USER_CONFIRMATION_REQUEST` events.
  - Fine-tunes Ollama locally for simple tasks (e.g., commit message generation).
  - Enhances Grok’s context for complex tasks (e.g., code analysis).
- **Self-Adaptive Features**:
  - Self-suring validates AI outputs against user feedback.
  - Self-healing retries failed commit messages using LLM insights.
  - Self-evolving learns user preferences (e.g., commit message style) over time.
- **Training Data Reuse**: Stores data in `data/training.jsonl` for cross-project use (e.g., with Rocketlang, Cybershield).

## Files (Updated Structure)
- `.github/workflows/setup.yml`: GitHub Action workflow.
- `src/ui/app.py`: Enhanced Streamlit UI with AG-UI integration.
- `src/ai_engine/spec_gen.py`: AI-driven spec generation placeholder.
- `data/training.jsonl`: Training data for LLMs, now including AG-UI events.
- `logs/app.log`: Log file for runtime/errors.
- `logs/health_metrics.log`: Logs self-suring metrics (new).
- `logs/healing_actions.log`: Logs self-healing actions (new).
- `docs/index.md`: Developer guide with project overview.
- `docs/layman_guide.md`: Layman guide (to be created).
- `requirements.txt`: Python dependencies.
- `README.md`: Layman-friendly project overview and setup.

## Requirements
- Python script (`init_gitbuddy.py`) with no user input.
- Cross-platform (Windows/Ubuntu), free/open-source, within ₹6000/month.
- Error-proof with clear troubleshooting (e.g., “Replace token in .env”).
- Hardware: 12–16GB RAM laptops, 50 Mbps broadband, no GPU.

## Team
- Anil (layman, maritime expert).
- Bhargavi (junior, Odoo-trained, joins May 21, 2025).
- Indra (senior, Odoo-trained, joins May 21, 2025).

## Timeline
- Start: May 14, 2025.
- Initial setup complete: May 21, 2025.
- AG-UI integration and testing: May 14–20, 2025.

## Layman Comment
This is your ship’s logbook, Anil, now with a smarter crew (AG-UI) that learns, fixes, and grows to make your voyage smoother!
