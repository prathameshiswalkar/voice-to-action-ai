Voice-to-Action Pipeline

This project is a real-time voice-driven pipeline that converts customer voice queries into structured intents, extracted entities, and system actions, with optional voice-based responses. The system simulates how voice assistants are used in logistics and customer support environments.

------------------------------------------------------------

Demo Video

A complete working demonstration of the system is available at the link below:

https://drive.google.com/file/d/1cYELekQ_LjJCZYUMc2bvo8LSJ5MOBqm5/view?usp=sharing

The demo showcases:
- Browser-based voice input
- Automatic recording start and stop
- Speech-to-text conversion
- Intent classification
- Entity extraction
- Decision logic
- Voice-based system response

------------------------------------------------------------

System Overview

Input (Voice or Text):
"Pickup karna hai Andheri se Powai, 2 boxes"

Processing Pipeline:
1. Speech-to-text conversion
2. Intent classification
3. Entity extraction
4. Next-action decision logic
5. Text or voice-based response

Output (Structured Format):
{
  "intent": "BOOK_PICKUP",
  "confidence": 0.92,
  "entities": {
    "pickup_location": "Andheri",
    "drop_location": "Powai",
    "packages": 2,
    "pickup_time": null,
    "fragile": false
  },
  "action": {
    "next_action": "ASK_MISSING_FIELDS",
    "missing_fields": ["pickup_time"]
  }
}

------------------------------------------------------------

Supported Intents

The system supports multiple logistics-style customer intents, including:

- BOOK_PICKUP
- CHECK_RATE
- CHECK_SERVICEABILITY
- TRACK_ORDER
- CANCEL_ORDER
- RESCHEDULE_PICKUP
- RAISE_COMPLAINT
- CONNECT_TO_AGENT
- PAYMENT_QUERY
- DOCUMENT_UPLOAD_QUERY

Rule-based intent overrides are applied for high-confidence keywords such as "cancel", "track", or "complaint" to ensure reliable predictions.

------------------------------------------------------------

Entity Extraction

The system extracts structured information from English, Hindi, and Hinglish queries. Supported entities include:

- pickup_location
- drop_location
- weight_kg
- packages
- pickup_time
- fragile
- payment_mode
- phone_number

Entity extraction is handled using lightweight NLP techniques and regular expressions for speed and reliability.

------------------------------------------------------------

Decision Engine

After intent classification and entity extraction, the system determines the next action based on missing or available information.

Examples:
- If weight is missing during rate check, the system asks for weight
- If pickup time is missing during booking, the system asks for pickup time
- Complaint requests generate a complaint ticket action
- Agent requests trigger a handoff action

This mimics real-world conversational flow control used in production systems.

------------------------------------------------------------

Voice Interaction Features

- Browser-based microphone input
- Automatic recording stop after fixed duration
- Text-to-speech voice response
- Hands-free interaction flow

The system is tuned to balance responsiveness and accuracy for real-time use cases.

------------------------------------------------------------

Technology Stack

Backend:
- FastAPI

Speech Processing:
- Whisper for speech-to-text
- Edge TTS for text-to-speech

NLP and Machine Learning:
- scikit-learn
- spaCy
- Regular expressions

Frontend:
- HTML
- CSS
- JavaScript (MediaRecorder API)

------------------------------------------------------------

API Endpoints

POST /voice-agent/parse
Accepts text input and returns intent, entities, and action.

POST /voice-agent/parse-audio
Accepts audio input and returns recognized text, intent, entities, action, and optional voice output.

------------------------------------------------------------

Performance Trade-off

The system is intentionally configured to prioritize low processing time with moderate accuracy. This trade-off ensures a smooth real-time user experience while maintaining reliable intent detection and entity extraction.

Typical response time ranges between 1.5 to 2.5 seconds.

------------------------------------------------------------

Evaluation and Improvements

Current strengths:
- Modular and clean pipeline design
- Real-time voice interaction
- Multilingual robustness

Possible future improvements:
- Context handling across multiple turns
- Streaming transcription
- Improved entity disambiguation
- Cloud-based speech services for lower latency

------------------------------------------------------------

Conclusion

This project demonstrates an end-to-end voice-driven system that converts unstructured customer queries into structured, actionable outputs. It reflects practical system design considerations and real-world conversational workflows used in logistics and customer support applications.
