import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()

    recognizer.energy_threshold = 300
    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 0.8
    recognizer.phrase_threshold = 0.3
    recognizer.non_speaking_duration = 0.5

    try:
        with sr.Microphone() as source:
            print("🎙️ Speak now...")
            recognizer.adjust_for_ambient_noise(source, duration=1.0)

            audio = recognizer.listen(
                source,
                timeout=5,           # wait for speech
                phrase_time_limit=8  # max speech length
            )

        text = recognizer.recognize_google(
            audio,
            language="en-IN"
        )
        print("✅ Heard:", text)
        return text.lower()

    except sr.WaitTimeoutError:
        # ✅ VERY IMPORTANT: silent fail
        return ""

    except sr.UnknownValueError:
        print("❌ Could not understand")
        return ""

    except sr.RequestError as e:
        print("❌ Network error:", e)
        return ""
