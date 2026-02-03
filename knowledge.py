import requests

def shorten_answer(text, max_words=30):
    words = text.split()
    if len(words) > max_words:
        return " ".join(words[:max_words]) + "..."
    return text


def answer_question(question):
    """
    Fetches factual information using DuckDuckGo Instant Answer API
    """

    url = "https://api.duckduckgo.com/"
    params = {
        "q": question,
        "format": "json",
        "no_html": 1,
        "skip_disambig": 1
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if data.get("AbstractText"):
            return shorten_answer(data["AbstractText"])

        if data.get("Definition"):
            return shorten_answer(data["Definition"])

        related = data.get("RelatedTopics", [])
        if related and isinstance(related[0], dict):
            return shorten_answer(related[0].get("Text", ""))

        return "Sorry, I couldn't find a clear answer."

    except Exception as e:
        print("KNOWLEDGE ERROR:", e)
        return "There was a problem fetching information."
