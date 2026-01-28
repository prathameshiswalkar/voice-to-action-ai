from fastapi import FastAPI
from pydantic import BaseModel

from nlp.intent_classifier import predict_intent
from nlp.entity_extractor import extract_entities
from nlp.decision_engine import decide_next_action

app = FastAPI(
    title = 'Voice-to-Action AI Pipeline',
    description= 'Prototype API for intent detection, entity extraction, and action decisioning.',
    version='1.0.0'
)

class VoiceInput(BaseModel):
    text: str

@app.post("/voice-agent/parse")
def parse_voice(input: VoiceInput):
    intent, confidence = predict_intent(input.text)
    entities = extract_entities(input.text)
    action = decide_next_action(intent, entities)

    return {
        "intent": intent,
        "confidence": confidence,
        "entities": entities,
        "action": action
    }

