
# Mini AI Chatbot (Rule-Based Chat Assistant) 🤖

A lightweight, interactive command-line chat assistant built with Python. The bot greets users dynamically according to the time of day, resolves user queries via keyword matching from an internal dictionary, and manages continuous interactive sessions in a loop.

---

## 📌 Table of Contents
- [Overview](#-overview)
- [Key Features](#-key-features)
- [How It Works](#-how-it-works)
- [Sample Execution](#-sample-execution)
- [Future Improvements](#-future-improvements)

---

## 📖 Overview
This project demonstrates fundamental Python programming concepts working together seamlessly:
* **Dynamic Salutations:** Uses `datetime.datetime.now().hour` to deliver personalized greetings based on the time of day.
* **Dictionary-Driven Responses:** Matches user queries against predefined keyword-response pairs.
* **Substring Search:** Detects keywords embedded within natural sentences.
* **Interactive Control Flow:** Employs a continuous `while True` loop with graceful exit handling.

---

## ✨ Key Features
* **Time-Aware Greetings:**
  * Morning (`hour < 12`)
  * Afternoon (`12 <= hour < 18`)
  * Evening (`hour >= 18`)
* **Case-Insensitive Matching:** Uses `.lower()` normalization to ensure smooth query matching regardless of user casing.
* **Graceful Fallback:** Provides a polite default response whenever a keyword isn't recognized.
* **Zero Dependencies:** Built entirely with Python's standard library.

---

## ⚙️ How It Works

```text
[ Start Script ]
       │
       ▼
[ Prompt User for Name ]
       │
       ▼
[ Check System Hour (datetime) ] ──► [ Print Morning / Afternoon / Evening Greeting ]
       │
       ▼
┌──► [ while True: Prompt User Question ]
│      │
│      ▼
│    [ Convert Input to Lowercase ]
│      │
│      ├──► Keyword found in memory? ──► Print bot reply
│      │
│      ├──► Keyword not found?       ──► Print fallback response
│      │
│      └──► Contains "bye"?          ──► Print farewell & break loop
└──────┘
💻 Sample Execution
Enter your name: Alex
Good Evening! Alex
Hello! I am your mini AI chatbot.
 How can I assist you today?
Type 'bye' to exit from bot

please ask you question: hi there!
 bot_reply:  Hi there! What can I do for you?

please ask you question: can you tell me a joke?
 bot_reply:  Why don't scientists trust atoms? Because they make up everything!

please ask you question: what's the weather today?
 bot_reply:  I am not sure about the weather, but you can check a weather app or website for the latest updates.

please ask you question: bye
 bot_reply:  Goodbye! Have a great day!
Goodbye! Have a great day!

🔮 Future Improvements
Add fuzzy matching (difflib) to tolerate typos in user input.

Separate response data into an external intents.json file.

Save chat history with timestamps to an external log file.
