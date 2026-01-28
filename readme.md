# Voice-to-Action AI Pipeline (Prototype)

This project implements a Voice-to-Action AI system that converts voice-style customer queries into structured intent, extracted entities, and deterministic next actions.

The system is designed under realistic constraints such as limited data, multilingual Hinglish input, and the need for safe and explainable behavior.

## Features
- Intent classification using TF-IDF and Logistic Regression
- Rule-based overrides for critical intents
- Entity extraction using regex and heuristics
- Deterministic decision engine for next-action logic
- FastAPI-based API with Swagger UI for testing

## Project Structure
voice-agent-ai/
├── api/                # FastAPI application
├── nlp/                # Intent, entity, decision logic
├── models/             # Trained ML model
├── data/               # Dataset
├── test_pipeline.py    # End-to-end pipeline test
└── requirements.txt

## How to Run

1. Install dependencies  
pip install -r requirements.txt

2. Train the intent model  
python nlp/train_intent_model.py

3. Run the API  
uvicorn api.main:app --reload

4. Open Swagger UI  
http://127.0.0.1:8000/docs

## Example Input
{
  "text": "pickup kal morning Andheri se Powai"
}

## Output
Returns detected intent, confidence score, extracted entities, and the next system action.

## Notes
This is a prototype designed for internship evaluation and demonstrates system design, safety-first logic, and modular architecture.
