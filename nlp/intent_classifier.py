import pickle

MODEL_PATH = "models/intent_model.pkl"

# predict intent
def rule_based_intent_override(text):
    text = text.lower()

    if 'cancel' in text:
        return 'CANCEL_ORDER'
    
    if 'track' in text or 'tracking' in text or 'awb' in text:
        return 'TRACK_ORDER'
    
    if 'price' in text or 'rate' in text or 'cost' in text:
        return "CHECK_RATE"
    
    if 'agent' in text or 'driver' in text or 'support' in text:
        return 'CONNECT_TO_AGENT'
    
    if 'complaint' in text or 'problem' in text or 'issue' in text:
        return 'RAISE_COMPLAINT'
    if 'pickup' in text:
        return "BOOK_PICKUP"
    
# predict intent

def predict_intent(text):
    override = rule_based_intent_override(text)
    if override:
        return override, 0.99 # High confidence for rule-based intents
    
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    probs = model.predict_proba([text])[0]
    intent = model.classes_[probs.argmax()]
    confidence = probs.max()

    return intent, round(float(confidence), 2)
