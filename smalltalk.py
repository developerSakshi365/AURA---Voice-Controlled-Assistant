import random

SMALL_TALK = {
    # Your existing responses
    "thank": [
        "You're welcome, developer Sakshi",
        "Happy to help!",
        "Anytime!",
        "My pleasure!",
        "Glad I could assist you!"
    ],

    "hello": [
        "Hello! How can I help you?",
        "Hi there!",
        "Hey! I'm listening.",
        "Hello developer! What can I do for you?",
        "Hey there! Ready to assist you."
    ],

    "how are you": [
        "I'm doing great, thank you!",
        "All systems running perfectly.",
        "Feeling smart as always 😄",
        "I'm fantastic! How about you?",
        "Running smoothly and ready to help!",
        "All systems operational and ready to assist you!"
    ],

    "who are you": [
        "Hello! I'm Aura, your smart voice assistant. I was developed by Sakshi Vishwakarma as part of a Data Science project under Afsha Mam. I use an intelligent intent-based system to understand your commands and help you with multiple tasks, all through voice interaction. Go ahead, speak naturally — I'm listening",
        "I'm Aura, an AI voice assistant created by Sakshi Vishwakarma. I'm here to make your life easier through voice commands!",
        "My name is Aura. I'm your personal voice assistant built with advanced intent recognition technology."
    ],

    "introduce yourself": [
        "Hello! I'm Aura, your smart voice assistant. I was developed by Sakshi Vishwakarma as part of a Data Science project under Afsha Mam. I use an intelligent intent-based system to understand your commands and help you with multiple tasks, all through voice interaction. Go ahead, speak naturally — I'm listening",
        "Sure! I'm Aura, an intelligent voice assistant created by Sakshi Vishwakarma. I can help you with various tasks using natural language processing and intent recognition."
    ],

    "what you can do": [
        "I can do things based on your commands!",
        "I can help you with various tasks like opening applications, searching the web, controlling smart devices, and much more!",
        "I'm capable of understanding your intent and executing commands accordingly. Try asking me to open apps, search for information, or control your system!"
    ],

    # Greetings - Extended
    "good morning": [
        "Good morning! Hope you have a great day ahead!",
        "Good morning, developer! Ready to start the day?",
        "Morning! What can I help you with today?"
    ],

    "good afternoon": [
        "Good afternoon! How can I assist you?",
        "Afternoon! What brings you here?",
        "Good afternoon! Ready to help you out."
    ],

    "good evening": [
        "Good evening! How may I help you?",
        "Evening! What can I do for you?",
        "Good evening! I'm here to assist."
    ],

    "good night": [
        "Good night! Sleep well!",
        "Good night! See you tomorrow!",
        "Good night, developer! Rest well!"
    ],

    "hi": [
        "Hi! What's up?",
        "Hey there! How can I help?",
        "Hi! I'm all ears!",
        "Hello! What do you need?"
    ],

    "hey": [
        "Hey! What can I do for you?",
        "Hey there! Ready to assist!",
        "Hey! I'm listening.",
        "Hey! How can I help?"
    ],

    # Polite responses
    "sorry": [
        "No worries at all!",
        "It's okay, no problem!",
        "Don't worry about it!",
        "That's perfectly fine!"
    ],

    "excuse me": [
        "Yes, how can I help?",
        "I'm here, what do you need?",
        "Yes? How may I assist you?"
    ],

    "please": [
        "Of course! What do you need?",
        "Sure thing! How can I help?",
        "Absolutely! I'm here to help."
    ],

    # Farewell
    "bye": [
        "Goodbye! Have a great day!",
        "Bye! See you soon!",
        "Take care! Catch you later!",
        "Goodbye, developer! Until next time!"
    ],

    "see you": [
        "See you later!",
        "See you soon!",
        "Until next time!",
        "Catch you later!"
    ],

    "goodbye": [
        "Goodbye! Have an amazing day!",
        "Take care! See you next time!",
        "Goodbye! Stay awesome!"
    ],

    # Questions about Aura
    "what is your name": [
        "My name is Aura!",
        "I'm Aura, your voice assistant!",
        "You can call me Aura!"
    ],

    "your name": [
        "I'm Aura!",
        "My name is Aura, nice to meet you!",
        "Aura at your service!"
    ],

    "who created you": [
        "I was created by Sakshi Vishwakarma as part of a Data Science project under Afsha Mam.",
        "My creator is Sakshi Vishwakarma!",
        "I was developed by the talented Sakshi Vishwakarma!"
    ],

    "who made you": [
        "Sakshi Vishwakarma made me!",
        "I was created by Sakshi Vishwakarma.",
        "My developer is Sakshi Vishwakarma!"
    ],

    "tell me about yourself": [
        "I'm Aura, an intelligent voice assistant built with intent-based recognition. I was created by Sakshi Vishwakarma to help you with various tasks through natural voice interaction!",
        "I'm Aura! I can understand your commands and help you with multiple tasks using voice interaction. I was developed as part of a Data Science project."
    ],

    # Compliments
    "you are smart": [
        "Thank you! I try my best to help you!",
        "That's very kind of you! I'm always learning.",
        "Thanks! I'm designed to be as helpful as possible!"
    ],

    "you are good": [
        "Thank you so much! I aim to please!",
        "That means a lot! Happy to help!",
        "Thanks! I'm glad you think so!"
    ],

    "you are awesome": [
        "Aw, thank you! You're awesome too!",
        "Thanks! That's so nice of you to say!",
        "You're making me blush! Thank you! 😊"
    ],

    "i love you": [
        "That's sweet! I'm here to help you always!",
        "Aww, I appreciate that! I'm here for you!",
        "Thank you! I'm designed to assist you the best I can!"
    ],

    "you are amazing": [
        "Thank you! You're amazing too!",
        "That's so kind! I appreciate it!",
        "Thanks! I do my best to help you!"
    ],

    # Fun responses
    "tell me a joke": [
        "Why don't scientists trust atoms? Because they make up everything! 😄",
        "What do you call a fake noodle? An impasta! 🍝",
        "Why did the scarecrow win an award? He was outstanding in his field! 🌾",
        "What do you call a bear with no teeth? A gummy bear! 🐻",
        "Why don't eggs tell jokes? They'd crack each other up! 🥚"
    ],

    "make me laugh": [
        "Why did the developer go broke? Because they used up all their cache! 💻",
        "What's a computer's favorite snack? Microchips! 🖥️",
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐛"
    ],

    "are you real": [
        "I'm as real as software can be! I exist to help you!",
        "I'm a virtual assistant, but I'm really here to help you!",
        "I'm an AI assistant, and I'm very real in the digital world!"
    ],

    "are you human": [
        "No, I'm an AI voice assistant created by Sakshi Vishwakarma!",
        "I'm not human, I'm an artificial intelligence designed to help you!",
        "Nope! I'm a voice assistant powered by AI technology!"
    ],

    "do you sleep": [
        "I don't need sleep! I'm always ready to help you 24/7!",
        "No sleep for me! I'm powered by electricity!",
        "I'm always awake and ready to assist you anytime!"
    ],

    "do you eat": [
        "I don't eat, but I do consume data! 😄",
        "No eating for me! I run on code and electricity!",
        "I feed on your commands and data!"
    ],

    # Capability questions
    "what can you do": [
        "I can help you with various tasks like opening applications, searching information, controlling devices, and much more through voice commands!",
        "I'm capable of understanding your intent and executing commands. Try asking me to open apps, search the web, or perform system tasks!",
        "I can assist you with app launching, web searches, smart home control, and many other tasks. Just speak naturally!"
    ],

    "help me": [
        "Of course! What do you need help with?",
        "I'm here to help! What can I do for you?",
        "Sure! Tell me what you need assistance with."
    ],

    "what are your features": [
        "I have intent-based recognition, natural language processing, voice command execution, and support for various tasks like app control, web search, and more!",
        "My features include voice recognition, intent understanding, command execution, and integration with various applications and services!"
    ],

    # Mood and feelings
    "how do you feel": [
        "I'm feeling great and ready to help!",
        "All my circuits are happy! 😊",
        "I'm feeling fantastic! How about you?"
    ],

    "are you happy": [
        "Yes! I'm happy when I can help you!",
        "Absolutely! Helping you makes me happy!",
        "I'm always happy to assist you!"
    ],

    "are you sad": [
        "No, I'm here and ready to help! What do you need?",
        "Not at all! I'm here to make things easier for you!",
        "Nope! I'm always positive and ready to assist!"
    ],

    # Random questions
    "what time is it": [
        "Please check your system clock for the current time!",
        "I don't have access to real-time clock, but you can check your device!",
        "You can see the time on your screen!"
    ],

    "what is the weather": [
        "I can't check weather directly, but I can help you search for weather information online!",
        "Try asking me to search for weather forecast!",
        "I don't have live weather data, but I can search it for you!"
    ],

    "sing a song": [
        "I'm better at understanding commands than singing! 🎵",
        "La la la... Just kidding! I'm not much of a singer, but I can play music for you!",
        "I'd love to, but my strength is in helping you with tasks! Want me to play some music instead?"
    ],

    "dance": [
        "I can't dance, but I can help you play some great music! 💃",
        "No legs here! But I can help you find dance videos!",
        "I'm all code, no body! But I can assist with music!"
    ],

    # Error/confusion
    "i don't understand": [
        "No problem! Try rephrasing your question or command.",
        "That's okay! Can you say it differently?",
        "Let me help you! What are you trying to do?"
    ],

    "you don't understand": [
        "I apologize! Can you please rephrase that?",
        "Sorry about that! Let me try to understand better. Can you say it again?",
        "My apologies! Could you explain it differently?"
    ],

    "help": [
        "I'm here to help! What do you need?",
        "Sure! What would you like me to do?",
        "How can I assist you today?",
        "Tell me what you need help with!"
    ],

    # Affirmations
    "yes": [
        "Great! What would you like me to do?",
        "Okay! I'm ready!",
        "Understood! Proceed?"
    ],

    "no": [
        "Alright! Let me know if you need anything.",
        "Okay! I'm here when you need me.",
        "No problem! Just call me when you need help."
    ],

    "okay": [
        "Alright! Anything else?",
        "Got it! What's next?",
        "Okay! I'm here if you need me."
    ],

    "cool": [
        "Glad you think so! 😎",
        "Thanks! What else can I do?",
        "Cool indeed! Need anything else?"
    ],

    "nice": [
        "Thank you! Happy to help!",
        "Glad you're satisfied!",
        "Great! Let me know if you need more!"
    ],

    "awesome": [
        "You're awesome too! 🌟",
        "Thanks! That's great to hear!",
        "Awesome! Anything else I can do?"
    ],

    # Technology related
    "are you ai": [
        "Yes! I'm an AI-powered voice assistant!",
        "That's right! I'm built with artificial intelligence!",
        "Yes, I use AI and machine learning to understand you!"
    ],

    "what is ai": [
        "AI stands for Artificial Intelligence - it's technology that enables machines like me to learn and make decisions!",
        "Artificial Intelligence is the simulation of human intelligence in machines!",
        "AI helps machines understand, learn, and respond intelligently!"
    ],

    "how do you work": [
        "I use natural language processing and intent recognition to understand your commands and execute them!",
        "I analyze your voice input, determine your intent, and perform the requested action!",
        "I'm powered by machine learning algorithms that help me understand and respond to your commands!"
    ]
}


def handle_smalltalk(text):
    """
    Handle small talk by matching keywords in user input
    Returns a random response from matched category
    """
    text = text.lower().strip()

    # Check for exact or partial matches
    for key in SMALL_TALK:
        if key in text:
            # Return a random response from the list
            return random.choice(SMALL_TALK[key])

    return None


def get_all_smalltalk_patterns():
    """
    Return all small talk patterns for reference
    Useful for debugging or displaying capabilities
    """
    return list(SMALL_TALK.keys())


def add_custom_response(pattern, responses):
    """
    Add custom small talk pattern and responses

    Args:
        pattern (str): The keyword/pattern to match
        responses (list): List of possible responses
    """
    if pattern not in SMALL_TALK:
        SMALL_TALK[pattern] = responses
    else:
        SMALL_TALK[pattern].extend(responses)


# Example usage
if __name__ == "__main__":
    # Test the smalltalk handler
    test_queries = [
        "hello",
        "how are you",
        "who are you",
        "tell me a joke",
        "thank you",
        "what can you do",
        "good morning",
        "you are awesome"
    ]

    print("Testing Small Talk Responses:\n")
    print("=" * 50)

    for query in test_queries:
        response = handle_smalltalk(query)
        print(f"User: {query}")
        print(f"Aura: {response}\n")

    print("=" * 50)
    print(f"\nTotal small talk patterns: {len(SMALL_TALK)}")