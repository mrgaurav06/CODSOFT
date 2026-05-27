import datetime


print("*******SIMPLE AI CHATBOT******")


name = input("Enter your name: ")

print("\nHello", name + "!")
print("I am your virtual assistant.")
print("Type 'bye' anytime to exit.\n")

while True:

    user = input("You: ").lower()

    # Greetings
    if user == "hi" or user == "hello":
        print("Bot: Hello", name + "! How are you?")

    elif user == "good morning":
        print("Bot: Good morning! Have a great day.")

    elif user == "good evening":
        print("Bot: Good evening!")

    # Health and feelings
    elif user == "how are you":
        print("Bot: I am doing well. What about you?")

    elif user == "i am fine":
        print("Bot: That's great to hear!")

    elif user == "i am sad":
        print("Bot: Don't worry. Everything will be okay.")

    elif user == "i am tired":
        print("Bot: Take some rest and stay hydrated.")

    elif user == "exam stress":
        print("Bot: Stay calm and prepare step by step.")

    # About chatbot
    elif user == "what is your name":
        print("Bot: My name is AI ChatBot.")

    elif user == "who created you":
        print("Bot: I was created by Gaurav Chalakh for the CodSoft internship.")

    elif user == "what can you do":
        print("Bot: I can answer simple questions and chat with users.")

    # Time and date
    elif user == "time":
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    elif user == "date":
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", current_date)

    # Weather and temperature
    elif user == "what is temperature now":
        print("Bot: The current temperature is around 30 degree Celsius.")

    elif user == "weather":
        print("Bot: The weather seems sunny today.")

    elif user == "is it raining":
        print("Bot: I don't think it's raining right now.")

    # AI and programming questions
    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif user == "what is python":
        print("Bot: Python is a popular programming language.")

    elif user == "what is machine learning":
        print("Bot: Machine Learning is a branch of AI that allows systems to learn from data.")

    # Fun section
    elif user == "tell me a joke":
        print("Bot: Why was the computer cold? Because it forgot to close its Windows!")

    elif user == "favorite color":
        print("Bot: I like blue color.")

    elif user == "favorite food":
        print("Bot: I don't eat food, but pizza smells amazing!")

    # Motivation
    elif user == "motivate me":
        print("Bot: Success comes from consistency and hard work.")

    # Simple math
    elif user == "2 + 2":
        print("Bot: 2 + 2 = 4")

    elif user == "10 * 5":
        print("Bot: 10 * 5 = 50")

    # Help section
    elif user == "help":
        print("Bot: You can ask me about time, date, weather, AI, jokes, or simple questions.")

    # Thank you
    elif user == "thank you":
        print("Bot: You're welcome", name + "!")

    # Exit
    elif user == "bye":
        print("Bot: Goodbye", name + "! Have a nice day.")
        break

    # Unknown input
    else:
        print("Bot: Sorry, I didn't understand that.")