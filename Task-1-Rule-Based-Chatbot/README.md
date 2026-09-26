# 🤖 CodBot - Rule-Based Chatbot

A simple rule-based chatbot developed in Python as **Task 1 of the CodSoft Artificial Intelligence Internship**.

## 📌 Project Overview

CodBot is a console-based chatbot that interacts with users through predefined rules and pattern matching. It accepts user input, identifies common queries and provides appropriate responses.

The project demonstrates the basic concepts of conversational flow and rule-based natural language processing.

## ✨ Features

* 👋 Responds to greetings
* 👤 Takes and remembers the user's name during the conversation
* 🤖 Introduces itself
* 💬 Handles basic conversational queries
* 📅 Displays the current date
* 🕐 Displays the current time
* 🐍 Provides basic information about Python
* 💼 Provides information about the CodSoft internship
* ❤️ Handles simple positive interactions
* 🙏 Responds to thank-you messages
* ❓ Handles unknown inputs
* 👋 Allows the user to exit the conversation

## 🛠️ Technologies Used

* **Python 3**
* `datetime` module
* Conditional statements
* Loops
* String handling
* Functions
* Pattern matching

## 🧠 How It Works

The chatbot uses predefined rules implemented with `if`, `elif` and `else` statements.

The user's input is first converted to lowercase and common punctuation marks are removed. The chatbot then checks the input against predefined keywords and phrases.

Common acknowledgements such as "ok", "okay", "alright" and "sure" are recognized and receive predefined responses.

For example:

* Greetings → greeting response
* `"your name"` → chatbot introduces itself
* `"date"` → displays the current date
* `"time"` → displays the current time
* `"python"` → provides basic Python information
* `"bye"` → ends the conversation
* Unknown input → displays a default response

## 📂 Project Structure

```text
Task-1-Rule-Based-Chatbot/
│
├── chatbot.py
└── README.md
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-github-repository-link>
```

### 2. Navigate to the project folder

```bash
cd Task-1-Rule-Based-Chatbot
```

### 3. Run the chatbot

```bash
python chatbot.py
```

## 💻 Sample Interaction

```text
=======================================================
             WELCOME TO CODBOT
=======================================================
Hello! I am CodBot, a simple rule-based chatbot.
I can respond to greetings, basic questions and more.
Type 'bye', 'exit' or 'quit' whenever you want to leave.

CodBot: What is your name?
You: Diya

CodBot: Nice to meet you, Diya! 😊

CodBot: How can I help you today, Diya?
Diya: Hello!
CodBot: Hello! 😊 How can I help you?

Diya: What is the time?
CodBot: The current time is 10:30 PM.

Diya: What is Python?
CodBot: Python is a popular programming language used in AI, machine learning, automation and web development.

Diya: Bye
CodBot: Goodbye, Diya! It was nice talking to you. 👋
```

## 🎯 Internship Task

**Internship:** CodSoft Artificial Intelligence Internship

**Task:** Task 1 - Chatbot with Rule-Based Responses

The project follows the task requirement of creating a chatbot that responds to user inputs using predefined rules and `if-else`/pattern-matching techniques.

## 👩‍💻 Author

**Renesa Pal**
