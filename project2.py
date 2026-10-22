"""A small rule-based CLI chat assistant.

Run with: python project2.py
"""
import datetime
import re

FALLBACK = "I'm sorry, I don't understand. Can you please rephrase your question?"

RESPONSES = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi there! What can I do for you?",
    "heyya": "Hey! How's it going?",
    "how are you": "I am doing well, thank you for asking!",
    "what is your name": "I am a mini AI chatbot created to assist you.",
    "what can you do": "I can answer your questions and provide information.",
    "not happy": "I'm sorry to hear that. Is there anything I can do to help?",
    "not good": "I'm sorry to hear that. Is there anything I can do to help?",
    "happy": "That's great to hear! I'm glad you're happy.",
    "sad": "I'm sorry to hear that. Is there anything I can do to help?",
    "bye": "Goodbye! Have a great day!",
    "motivate": (
        "Believe in yourself and all that you are. Know that there is something "
        "inside you that is greater than any obstacle."
    ),
    "inspire": "The only way to do great work is to love what you do. - Steve Jobs",
    "joke": "Why don't scientists trust atoms? Because they make up everything!",
    "weather": (
        "I am not sure about the weather, but you can check a weather app or "
        "website for the latest updates."
    ),
}


def greeting_for_hour(hour: int) -> str:
    """Pick a greeting based on the 24-hour clock."""
    if hour < 12:
        return "Good Morning"
    if hour < 18:
        return "Good Afternoon"
    return "Good Evening"


def get_response(user_input: str) -> str:
    """Return a reply, matching whole words only.

    Longest keys are tried first, so "how are you" wins over "hi", and
    the phrase "not happy" wins over "happy".
    """
    text = " ".join(user_input.lower().split())
    if not text:
        return FALLBACK
    for key in sorted(RESPONSES, key=len, reverse=True):
        if re.search(rf"\b{re.escape(key)}\b", text):
            return RESPONSES[key]
    return FALLBACK


def main() -> None:
    name = input("Enter your name: ").strip() or "friend"
    print(f"{greeting_for_hour(datetime.datetime.now().hour)}, {name}!")
    print("Hello! I am your mini AI chatbot.")
    print("How can I assist you today?")
    print("Type 'bye' to exit from bot")

    while True:
        user_input = input("Please ask your question: ")
        reply = get_response(user_input)
        print("bot_reply:", reply)
        if reply == RESPONSES["bye"]:
            break


if __name__ == "__main__":
    main()
