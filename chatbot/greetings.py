import random

greeting_words = [
    "hi",
    "hello",
    "hey",
    "hii",
    "good morning",
    "good afternoon",
    "good evening"
]

thanks_words = [
    "thanks",
    "thank you",
    "thx"
]

farewell_words = [
    "bye",
    "goodbye",
    "see you",
    "take care"
]

def check_greeting(text):

    text = text.lower().strip()

    if text in greeting_words:

        return (
            True,
            random.choice([
                "Hello! How can I help you today?",
                "Hi! Tell me about your symptoms or feelings.",
                "Hey! I'm here to help."
            ])
        )

    if text in thanks_words:

        return (
            True,
            random.choice([
                "You're welcome!",
                "Glad I could help.",
                "Happy to help."
            ])
        )

    if text in farewell_words:

        return (
            True,
            random.choice([
                "Take care!",
                "Goodbye!",
                "Wishing you good health."
            ])
        )

    return False, None