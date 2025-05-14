# GitBuddy-AI Overview (v1.0.0)

**GitBuddy-AI** automates GitHub projects with 98% AI tasks, 2% input. It's free, open-source, cross-platform.

## Modules
- UI: Streamlit dashboard
- AI Engine: Specs/workflows
- GitHub: Manages repos
- Maintenance: Auto-fixes
- Validation: Deploys apps

# Developer Comment: Guide. Bhargavi/Indra to add setup, APIs.
# Layman Comment: Ship's manual for crew.

## Project Prompt (v1.0.0)

**Project Name**: GitBuddy-AI  
**Version**: 1.0.0  
**Objective**: Create a fresh GitHub repository (`https://github.com/rocketlang/gitbuddy-ai`) to automate GitHub project setup and management with 98% AI-driven tasks and 2% layman input, integrating with **CyberShield-Easy** and **RocketAutomation**.  
**Core Features**:  
- **Repo Creation**: AI creates GitHub repo with predefined structure.  
- **File Population**: Generates minimal files (workflow, UI, AI logic, logs, docs).  
- **Layman UI**: Streamlit dashboard with maritime-inspired prompts (e.g., “Enter project name”).  
- **Self-Curing**: Auto-retries on errors (e.g., invalid token), logs issues.  
- **Self-Evolving**: Learns from inputs (e.g., maritime terms) in JSONL format.  
- **AI-Agnostic**: Portable data for LLMs like Qwen2.5 or Grok 3.  
**Files Needed**:  
- `.github/workflows/setup.yml`: Basic GitHub Action workflow.  
- `src/ui/app.py`: Streamlit UI for layman interaction.  
- `src/ai_engine/spec_gen.py`: AI-driven spec generation placeholder.  
- `data/training.jsonl`: Empty file for AI training data.  
- `logs/app.log`: Log file for runtime/errors.  
- `docs/index.md`: Developer guide with project overview.  
- `requirements.txt`: Python dependencies.  
- `README.md`: Layman-friendly project overview and setup.  
**Requirements**:  
- Hardcode PAT `[REDACTED_PAT]`, project name `GitBuddy-AI for CyberShield-Easy`, repo URL `https://github.com/rocketlang/gitbuddy-ai`.  
- Python script (`init_gitbuddy.py`) with no user input.  
- Include developer/layman comments (maritime analogies).  
- Cross-platform (Windows/Ubuntu), free/open-source, within ₹6000/month.  
- Error-proof with clear troubleshooting (e.g., “Replace token on line X”).  
**Constraints**: No Bhargavi, minimal input, Windows-compatible, avoid complex YAML/Markdown.  
**Budget**: ₹6000/month, using existing hardware (8–16GB RAM laptops, 50 Mbps broadband).  
**Team**: Anil (layman, maritime expert), Bhargavi (junior, Odoo-trained, unavailable), Indra (senior, Odoo-trained, future support).  
**Timeline**: Start May 14, 2025; initial setup complete by May 21, 2025.


## Project Prompt (v1.0.0)

**Project Name**: GitBuddy-AI  
**Version**: 1.0.0  
**Objective**: Create a fresh GitHub repository (`https://github.com/rocketlang/gitbuddy-ai`) to automate GitHub project setup and management with 98% AI-driven tasks and 2% layman input, integrating with **CyberShield-Easy** and **RocketAutomation**.  
**Core Features**:  
- **Repo Creation**: AI creates GitHub repo with predefined structure.  
- **File Population**: Generates minimal files (workflow, UI, AI logic, logs, docs).  
- **Layman UI**: Streamlit dashboard with maritime-inspired prompts (e.g., “Enter project name”).  
- **Self-Curing**: Auto-retries on errors (e.g., invalid token), logs issues.  
- **Self-Evolving**: Learns from inputs (e.g., maritime terms) in JSONL format.  
- **AI-Agnostic**: Portable data for LLMs like Qwen2.5 or Grok 3.  
**Files Needed**:  
- `.github/workflows/setup.yml`: Basic GitHub Action workflow.  
- `src/ui/app.py`: Streamlit UI for layman interaction.  
- `src/ai_engine/spec_gen.py`: AI-driven spec generation placeholder.  
- `data/training.jsonl`: Empty file for AI training data.  
- `logs/app.log`: Log file for runtime/errors.  
- `docs/index.md`: Developer guide with project overview.  
- `requirements.txt`: Python dependencies.  
- `README.md`: Layman-friendly project overview and setup.  
**Requirements**:  
- Hardcode PAT `[REDACTED_PAT]`, project name `GitBuddy-AI for CyberShield-Easy`, repo URL `https://github.com/rocketlang/gitbuddy-ai`.  
- Python script (`init_gitbuddy.py`) with no user input.  
- Include developer/layman comments (maritime analogies).  
- Cross-platform (Windows/Ubuntu), free/open-source, within ₹6000/month.  
- Error-proof with clear troubleshooting (e.g., “Replace token on line X”).  
**Constraints**: No Bhargavi, minimal input, Windows-compatible, avoid complex YAML/Markdown.  
**Budget**: ₹6000/month, using existing hardware (8–16GB RAM laptops, 50 Mbps broadband).  
**Team**: Anil (layman, maritime expert), Bhargavi (junior, Odoo-trained, unavailable), Indra (senior, Odoo-trained, future support).  
**Timeline**: Start May 14, 2025; initial setup complete by May 21, 2025.


## AG-UI Integration Strategy (v1.1)

We’ve brainstormed a strategy to integrate the AG-UI protocol across GitBuddy, Rocketlang, and Cybershield, focusing on modularity, AI training, and self-adaptive features. Here’s the plan, with examples for GitBuddy, but it applies to all projects:

- **Shared Chat Widget**: Build a streaming chat widget with AG-UI’s TypeScript SDK to show commit messages in GitBuddy, code suggestions in Rocketlang, and threat alerts in Cybershield. It’s like a ship’s control panel that works for all voyages.
- **AI Training**: Use AG-UI events to collect user feedback (e.g., edited commit messages in GitBuddy) and store it in data/training.jsonl. This helps the AI learn better messages over time, and the data can be reused for Rocketlang and Cybershield.
- **Self-Monitoring**: AG-UI’s events can check if commit messages in GitBuddy follow rules, logging issues in logs/app.log. It’s like a ship’s lookout spotting problems early.
- **Self-Healing**: If a commit message is wrong, AG-UI can ask the user to fix it or retry using the AI. It’s like a ship fixing a sail automatically during a storm.
- **Self-Evolving**: The AI learns from user edits, getting better at commit messages, coding, and threat detection over time, like a ship learning the best routes.
- **Easy for Beginners**: AG-UI’s quick-start guide lets the team set up features fast, even with little AI knowledge, like following a simple map.
- **Resource Efficiency**: Use small JSON events and cloud APIs (like Grok) to keep things light on our 16GB RAM laptops, ensuring smooth sailing.

# Developer Comment: Strategy for Bhargavi and Indra to implement AG-UI features.
# Layman Comment: A plan for the crew to make the ship smarter and easier to use, Anil.
