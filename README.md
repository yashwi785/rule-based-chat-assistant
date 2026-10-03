
Mini AI Chatbot (Rule-Based Chat Assistant) 🤖
A personalized, interactive command-line chat assistant built in Python. The bot greets users dynamically according to the time of day, resolves user queries via keyword matching in an internal dictionary memory, and handles interactive sessions in a continuous loop.
📌 Table of Contents
Overview
Key Features
How It Works
Getting Started
Prerequisites
Running the Code
Sample Execution
Code Structure
Potential Improvements
License
📖 Overview
This program demonstrates fundamental Python constructs working together:
Dynamic Greeting: Uses datetime.datetime.now().hour to offer time-aware salutations (Morning, Afternoon, Evening) paired with the user's name.
Intent Matching: Maintains an in-memory dictionary of predefined triggers and responses.
Substring Search: Scans user input to detect recognized keywords and deliver appropriate responses.
Interactive REPL Loop: Runs an ongoing while True loop until a termination keyword (bye) is detected.
✨ Key Features
Time-Aware Salutations: Automatically switches between:
Morning (hour < 12)
Afternoon (12 <= hour < 18)
Evening (hour >= 18)
Normalized Input Checking: Converts user input to lowercase using .lower() to ensure case-insensitive keyword detection.
Graceful Fallback: Catches unknown input gracefully with a helpful prompt to rephrase.
Clean Exit Logic: Detects "bye" in input, provides a farewell message, and breaks the execution loop cleanly.
⚙️ How It Works[ User runs script ]
        │
        ▼
[ Prompt for Name ] ──────► Read system hour via datetime.datetime.now().hour
        │
        ▼
[ Print Personalized Time Greeting ]
        │
        ▼
┌───► [ while True: Prompt "please ask you question:" ]
│       │
│       ▼
│     [ Convert input to lowercase ]
│       │
│       ├──► Keyword found in memory? ──► Return bot reply
│       └──► No keyword found?        ──► Return fallback message
│       │
│       ▼
│     [ Contains "bye"? ]
│       ├──► Yes: Print farewell & exit loop (break)
└───-───└──► No:  Loop repeats
🚀 Getting Started
Prerequisites
Python 3.x installed.
Built exclusively using the standard library (datetime, time), so no external packages (pip) are required.
Running the Code
Save the code in a file named main.py (or chatbot.py).
Open your terminal or command prompt in that directory.
Run:
python main.py
💻 Sample Execution
Enter your name: Alex
Good Evening! Alex
Hello! I am your mini AI chatbot.
 How can I assist you today?
Type 'bye' to exit from bot

please ask you question: hi there!
 bot reply:  Hi there! What can I do for you?

please ask you question: tell me a joke
 bot reply:  Why don't scientists trust atoms? Because they make up everything!

please ask you question: can you inspire me?
 bot reply:  The only way to do great work is to love what you do. - Steve Jobs

please ask you question: what's the stock market doing?
 bot reply:  I'm sorry, I don't understand. Can you please rephrase your question?

please ask you question: bye
 bot reply:  Goodbye! Have a great day!
Goodbye! Have a great day!
📂 Code Structure
Time greeting block: Determines the current hour and greets the user by name.
chatbot_memory: A key-value dictionary mapping string triggers to chatbot responses.
getresponseof(user_input): A lookup function iterating through dictionary keys with containment checks (eachkey in user_input).
Main execution loop: An interactive while True loop coordinating inputs, function calls, and session termination.
📄 License

This project is open-source and available under the MIT License.
