# Smart City AI Carbon Copilot

An agentic AI application that analyzes buildings across Delhi NCR to support carbon-aware urban planning and decision-making.

---

## 1. Project Overview

**Smart City AI Carbon Copilot** is a production-grade, multi-agent AI system designed to assist city planners, sustainability teams, and building stakeholders in understanding the carbon footprint of buildings across the Delhi NCR region.

The system uses a coordinated crew of specialized AI agents to analyze building and geospatial data, retrieve relevant domain knowledge, and produce actionable insights — combining structured data analysis with retrieval-augmented reasoning in an agentic workflow.

This repository contains the foundational architecture for the application, built with scalability, modularity, and maintainability in mind.

---

## 2. Features

- Agentic, multi-agent workflow for building-level carbon analysis
- Retrieval-augmented knowledge access via a vector database
- Support for both cloud-hosted and local LLM inference
- Secure authentication for application users
- Modular backend designed for independent scaling of agents, tasks, and tools
- Modern web-based frontend for interacting with the system
- Clear separation of concerns across API, orchestration, data, and presentation layers

---

## 3. Architecture Overview

The application follows a layered, modular architecture:

- **Frontend** — A React-based web interface for user interaction.
- **API Layer** — A FastAPI service exposing the application's capabilities to the frontend and external consumers.
- **Agentic Layer (CrewAI)** — A crew of specialized agents, each responsible for a distinct part of the analysis workflow, coordinated through defined tasks and tools.
- **Knowledge Layer** — A vector database used for retrieval-augmented context relevant to building and carbon analysis.
- **Authentication Layer** — Handles user identity and access control.
- **LLM Inference Layer** — Supports a cloud-hosted inference provider for deployment and a local inference runtime for development.
- **Data Layer** — Structured storage for application and domain data.

The layers are intentionally decoupled so that agents, tools, tasks, and services can evolve independently without affecting the API contract or the frontend.

---

## 4. Folder Structure

```
SmartCityAICarbon/
├── backend/
│   ├── app/
│   │   ├── api/          # API layer (routing to be added)
│   │   ├── crew/         # CrewAI crew orchestration
│   │   ├── agents/       # Agent definitions
│   │   ├── tasks/        # Task definitions
│   │   ├── tools/        # Custom tools for agents
│   │   ├── services/     # Application services
│   │   ├── config/       # Configuration and settings
│   │   ├── database/     # Database connectivity layer
│   │   ├── models/       # Data models
│   │   ├── schemas/      # Request/response schemas
│   │   ├── utils/        # Shared utilities
│   │   └── main.py       # Application entry point
│   └── tests/            # Backend test suite
├── frontend/              # React web application
├── rag/                   # Retrieval-augmented knowledge base and source documents
├── data/                  # Domain and model data
├── deployment/            # Deployment configuration
└── docs/                  # Project documentation
```

---

## 5. Technology Stack

| Layer | Technology |
|---|---|
| Agentic Orchestration | CrewAI |
| Backend API | FastAPI |
| Frontend | React |
| Vector Database | ChromaDB |
| Authentication | Supabase Auth |
| Cloud LLM Inference (Deployment) | Groq |
| Local LLM Inference (Development) | Ollama |
| Core Language | Python |

---

## 6. Installation

> Setup instructions will be added as the implementation progresses.

```bash
# Clone the repository
git clone <repository-url>

# Backend setup (placeholder)
# ...

# Frontend setup (placeholder)
# ...
```

---

## 7. Development Roadmap

- [ ] Define agent roles and responsibilities
- [ ] Implement CrewAI crew orchestration
- [ ] Build FastAPI endpoints
- [ ] Integrate ChromaDB for retrieval-augmented context
- [ ] Integrate Supabase Auth for user authentication
- [ ] Connect Groq for deployed inference
- [ ] Connect Ollama for local development inference
- [ ] Build the React frontend
- [ ] Add automated testing across backend and frontend
- [ ] Prepare deployment configuration

---

## 8. License

This project is currently unlicensed. A license will be added prior to public release.
