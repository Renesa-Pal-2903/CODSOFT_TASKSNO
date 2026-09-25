# CodSoft Artificial Intelligence Internship
# Task 1 - Rule-Based Chatbot

from datetime import datetime


def chatbot():
    print("=" * 55)
    print("             WELCOME TO CODBOT")
    print("=" * 55)
    print("Hello! I am CodBot, a simple rule-based chatbot.")
    print("I can respond to greetings, basic questions and more.")
    print("Type 'bye', 'exit' or 'quit' whenever you want to leave.")
    print()

    # Get user's name
    user_name = input("CodBot: What is your name?\nYou: ").strip()

    if user_name:
        print(f"CodBot: Nice to meet you, {user_name}! 😊")
    else:
        user_name = "User"
        print("CodBot: Nice to meet you! 😊")

    print(f"\nCodBot: How can I help you today, {user_name}?")

    while True:
        user_input = input(f"{user_name if user_name else 'You'}: ").strip().lower()
        user_input = user_input.replace("!", "").replace("?", "").replace(".", "").replace(",", "")
        

        # Remove common punctuation
        user_input = (
            user_input
            .replace("!", "")
            .replace("?", "")
            .replace(".", "")
            .replace(",", "")
        )

        # Exit
        if user_input in ["bye", "exit", "quit", "goodbye"]:
            print(f"CodBot: Goodbye, {user_name}! It was nice talking to you. 👋")
            break

        # Greetings
        elif user_input in [
            "hi",
            "hello",
            "hey",
            "good morning",
            "good afternoon",
            "good evening"
        ]:
            print("CodBot: Hello! 😊 How can I help you?")

        # Chatbot identity
        elif "your name" in user_input or "who are you" in user_input:
            print("CodBot: I am CodBot, a rule-based chatbot created as Task 1 of the CodSoft AI Internship.")

        # How are you
        elif "how are you" in user_input:
            print("CodBot: I'm doing great! Thanks for asking. 😊")

        # Capabilities
        elif "what can you do" in user_input or "help" in user_input:
            print("CodBot: I can respond to greetings, answer basic questions, tell you the date and time, and have a simple conversation.")

        # Date
        elif "date" in user_input or "today" in user_input:
            current_date = datetime.now().strftime("%d %B %Y")
            print(f"CodBot: Today's date is {current_date}.")

        # Time
        elif "time" in user_input:
            current_time = datetime.now().strftime("%I:%M %p")
            print(f"CodBot: The current time is {current_time}.")

        # CodSoft internship
        elif "codsoft" in user_input or "internship" in user_input:
            print("CodBot: This chatbot is developed as Task 1 of the CodSoft Artificial Intelligence Internship.")

        # Python
        elif "python" in user_input:
            print("CodBot: Python is a popular programming language used in AI, machine learning, automation and web development.")

        # User asks chatbot about its purpose
        elif "why were you created" in user_input or "your purpose" in user_input:
            print("CodBot: I was created to demonstrate how a simple rule-based chatbot works using Python.")

        # Positive responses
        elif user_input in ["good", "great", "awesome", "nice", "fine", "ok", "okay", "alright", "sure"]:
            print("CodBot: That's wonderful to hear! 😊 How can I help you further?")

        # Thank you
        elif "thank you" in user_input or "thanks" in user_input:
            print("CodBot: You're welcome! 😊")

        # Simple personal interaction
        elif "i like you" in user_input or "you are nice" in user_input:
            print("CodBot: That's sweet of you! 😊")

        # Default response
        else:
            print("CodBot: I'm sorry, I don't understand that yet. Try asking me something else.")

# Start the chatbot
if __name__ == "__main__":
    chatbot()