def extract_app_name(text):
    keywords = ["open", "launch", "start", "close", "exit", "stop"]
    words = text.lower().split()

    for word in keywords:
        if word in words:
            idx = words.index(word)
            return " ".join(words[idx + 1:])

    return None
