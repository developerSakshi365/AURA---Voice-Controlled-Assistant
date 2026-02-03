import json

with open("data/intents.json", "r") as f:
    INTENTS = json.load(f)


def predict_intent(text):
    text = text.lower()

    best_intent = "unknown"
    best_score = 0.0

    for intent, phrases in INTENTS.items():
        for phrase in phrases:
            if phrase in text:
                score = len(phrase) / len(text)
                if score > best_score:
                    best_intent = intent
                    best_score = score

    if best_score > 0:
        return best_intent, round(min(0.9, best_score + 0.3), 2)

    return "unknown", 0.2
