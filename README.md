
# Mini AI Chatbot (Rule-Based Chat Assistant) 🤖

A lightweight, interactive command-line chat assistant built with Python. The bot greets users dynamically according to the time of day, resolves user queries via keyword matching from an internal dictionary, and manages continuous interactive sessions in a loop.

---

## 📌 Table of Contents
- [Overview](#-overview)
- [Key Features](#-key-features)
- [How It Works](#-how-it-works)
- [Getting Started](#-getting-started)
- [Sample Execution](#-sample-execution)
- [Code Structure](#-code-structure)
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
