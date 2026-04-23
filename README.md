# ml_intern
# AutoStream Agent

## Overview
This project is a conversational AI agent that converts user interactions into qualified leads using:
- Intent classification
- RAG-based knowledge retrieval
- Tool execution for lead capture

## Architecture
The system uses a modular pipeline:
1. Intent Detection → classifies user input
2. RAG Module → retrieves pricing & policy info from JSON
3. State Manager → stores conversation context
4. Tool Executor → captures leads when user shows high intent
LangGraph-inspired state flow ensures smooth multi-turn conversations and memory retention across 5–6 steps.

## How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
