# auto_reply_bot_v2.py

def auto_reply(user_input):
    user_input = user_input.lower()

    # Predefined responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm doing well, thank you! 😊"
    elif "what is your name" in user_input:
        return "I'm your Auto Reply Bot!"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Take care! 👋"
    elif "help" in user_input:
        return "Sure! I can answer your basic queries. Try asking me anything."

    # Default answer for unknown questions
    elif "?" in user_input:
        return "Hmm... that's an interesting question! Let me learn and get back to you. 🤔"
    
    else:
        return "I see. Thanks for sharing that with me!"

# Run the bot
print("🤖 Auto Reply Bot Ready! Type 'bye' to exit.")
while True:
    user_msg = input("You: ")
    print("Bot:", auto_reply(user_msg))
    if user_msg.lower() in ["bye", "goodbye"]:
        break


import random

# Dictionary of responses
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!", "Hi! How can I help you today?"],
    "how_are_you": ["I'm just a bot, but I'm doing great!", "I'm fine, thank you!", "All systems running smoothly!"],
    "bye": ["Goodbye!", "See you later!", "Take care! 👋"],
    "thanks": ["You're welcome!", "Glad I could help!", "Anytime! 😊"],
    "default": ["I'm not sure how to respond to that.", "Can you rephrase?", "Hmm... I didn't get that."]
}

# Function to determine response
def auto_reply(user_input):
    msg = user_input.lower()

    if any(word in msg for word in ["hello", "hi", "hey"]):
        return random.choice(responses["greeting"])
    elif "how are you" in msg:
        return random.choice(responses["how_are_you"])
    elif "thank" in msg:
        return random.choice(responses["thanks"])
    elif any(word in msg for word in ["bye", "goodbye", "exit"]):
        return random.choice(responses["bye"])
    else:
        return random.choice(responses["default"])


# Bot starts
print("🤖 Auto Reply Bot is running. Type 'bye' or 'exit' to end.")

while True:
    user = input("You: ")
    reply = auto_reply(user)
    print("Bot:", reply)
    if "bye" in user.lower() or "exit" in user.lower():
        break

