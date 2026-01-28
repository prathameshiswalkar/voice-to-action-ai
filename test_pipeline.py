from nlp.intent_classifier import predict_intent
from nlp.entity_extractor import extract_entities
from nlp.decision_engine import decide_next_action

tests = [
    "pickup kal morning Andheri se Powai",
    "price batao Mumbai to Pune",
    "order cancel kar do",
    "tracking link bhejo",
    "agent se baat karni hai"
]

for text in tests:
    intent, confidence = predict_intent(text)
    entities = extract_entities(text)
    action = decide_next_action(intent, entities)

    print("\nINPUT:", text)
    print("INTENT:", intent, "with confidence", confidence)
    print("ENTITIES:", entities)
    print("ACTION:", action)