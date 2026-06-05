import random

# --- Bot Personality ---
BOT_NAME = "Nova"

# --- Memory ---
user_data = {
    "name": None
}

# --- Intents (structured AI style) ---
intents = {
    "greeting": {
        "keywords": ["hello", "hi", "hey"],
        "responses": ["Hello! 😊", "Hi there!", "Hey! How can I help you?"]
    },
    "how_are_you": {
        "keywords": ["how are you", "how do you feel"],
        "responses": ["I'm doing great! 😄", "All good here, thanks for asking!"]
    },
    "help": {
        "keywords": ["help", "what can you do"],
        "responses": [
            "🤖 I can help you with:\n"
            "- Greetings (hello, hi)\n"
            "- Talking about how you feel\n"
            "- Remembering your name\n"
            "- Basic questions\n\n"
            "💬 Try typing: hello, how are you, my name is ..."
        ]

    },
    "name_query": {
        "keywords": ["what is my name", "do you know my name"],
        "responses": []
    },
    "identity": {
        "keywords": ["your name", "who are you"],
        "responses": [f"I'm {BOT_NAME}, your virtual assistant 🤖"]
    }
}

# --- Helper: find intent ---
def get_intent(user_input):
    best_match = None
    best_score = 0

    for intent, data in intents.items():
        score = 0
        for word in data["keywords"]:
            if word in user_input:
                score += 1

        if score > best_score:
            best_score = score
            best_match = intent

    return best_match, best_score

# --- Bot ---
def chatbot():
    print(f"🤖 Bot: Hey! I'm {BOT_NAME}, your upgraded assistant.")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower().strip()

        # Exit
        if user in ["bye", "exit", "quit"]:
            print("Bot: Goodbye! 👋")
            break

        # Save name
        if "my name is" in user:
            name = user.replace("my name is", "").strip()
            user_data["name"] = name
            print(f"Bot: Nice to meet you, {name}! 😊")
            continue

        # Intent detection
        intent, score = get_intent(user)

        # If name question
        if intent == "name_query":
            if user_data["name"]:
                print(f"Bot: Your name is {user_data['name']} 😊")
            else:
                print("Bot: I don't know your name yet. Tell me: my name is ...")
            continue

        # Valid intent response
        if intent and score > 0:
            response = random.choice(intents[intent]["responses"])
            
            # personalize
            if user_data["name"]:
                response = response.replace("you", user_data["name"])

            print("Bot:", response)
        else:
            print("Bot: I'm not sure I understand 🤔 Try 'help'")

chatbot()