import threading
import time

from listener import listen
from speaker import speak, stop_speaking
from nlu import predict_intent
from router import handle_intent
from knowledge import answer_question
from smalltalk import handle_smalltalk


WAKE_WORDS = [
    "hey aura", "hi aura", "hello aura",
    "play aura", "hey ora", "hiora", "hai aur"
]

PARTIAL_WAKE = ["hey", "hi", "hello", "hai"]
CONFIRM_WORDS = ["yes", "yeah", "yep", "aura", "hi", "hello"]


class Assistant:
    def __init__(self, ui):
        self.ui = ui
        self.awake = False
        self.awaiting_confirmation = False
        self.last_app = None
        self.running = True
        self.speaking = False

        # 🔥 Start assistant in background thread
        self.thread = threading.Thread(
            target=self.run,
            daemon=True
        )
        self.thread.start()

    # ================= MAIN THREAD =================
    def run(self):
        # ⏳ Let Qt fully initialize
        time.sleep(1.2)

        self.safe_speak("Aura online. Say hey aura to wake me.")
        self.ui.signal_mic.emit("IDLE")

        while self.running:
            text = listen()
            if not text:
                continue

            text = text.lower()
            print("HEARD:", text)

            # 🟠 Confirmation mode
            if self.awaiting_confirmation:
                if any(w in text for w in CONFIRM_WORDS):
                    self.awake = True
                    self.awaiting_confirmation = False
                    self.safe_speak("Yes, I am here.")
                    self.ui.signal_mic.emit("LISTENING")
                else:
                    self.awaiting_confirmation = False
                continue

            # 🔴 Wake logic
            if not self.awake:
                if any(w in text for w in WAKE_WORDS):
                    self.awake = True
                    self.safe_speak("Yes?")
                    self.ui.signal_command.emit("Hey Aura")
                    self.ui.signal_mic.emit("LISTENING")
                    continue

                if any(p in text for p in PARTIAL_WAKE):
                    self.safe_speak("Are you there?")
                    self.awaiting_confirmation = True
                continue

            # 🛑 STOP
            if "stop" in text or "cancel" in text:
                stop_speaking()
                self.speaking = False
                self.safe_speak("Okay.")
                self.ui.signal_mic.emit("IDLE")
                continue

            # 🟡 Sleep
            if "go to sleep" in text:
                self.awake = False
                self.safe_speak("Going to sleep.")
                self.ui.signal_mic.emit("IDLE")
                continue

            # 💬 Small talk
            reply = handle_smalltalk(text)
            if reply:
                self.safe_speak(reply)
                self.ui.signal_response.emit(reply)
                continue

            # 🧠 Intent
            intent, confidence = predict_intent(text)
            self.ui.signal_command.emit(text)
            self.ui.signal_intent.emit(intent, confidence)

            response, opened_app = handle_intent(
                intent,
                text,
                self.last_app
            )

            if opened_app:
                self.last_app = opened_app

            if response:
                self.safe_speak(response)
                self.ui.signal_response.emit(response)
                continue

            # 🌐 Knowledge fallback
            if confidence < 0.6 or intent == "unknown":
                answer = answer_question(text)
                self.safe_speak(answer)
                self.ui.signal_response.emit(answer)

    # ================= SAFE SPEAK =================
    def safe_speak(self, text):
        if self.speaking:
            stop_speaking()
            time.sleep(0.1)

        self.speaking = True
        self.ui.signal_mic.emit("SPEAKING")
        speak(text)
        self.speaking = False
        self.ui.signal_mic.emit("LISTENING")
