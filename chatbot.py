import random

def get_response(user_input):
    user_input = user_input.lower()
    
    # Basic responses based on keywords
    responses = {
        "hello": ["Hi there!", "Hello!", "Greetings!", "Howdy!"],
        "how are you": ["I'm just a program, but thanks for asking!", "Doing well, how about you?", "I'm here to chat!"],
        "what is your name": ["I'm a simple chatbot!", "You can call me Chatbot!", "I'm nameless, but I'm here to help!"],
        "bye": ["Goodbye!", "See you later!", "Take care!"],
        "help": ["Sure! How can I assist you?", "I'm here to help! What do you need?", "Feel free to ask me anything!"]
    }
    
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    return "I'm not sure how to respond to that."

def chatbot():
    print("Welcome to Chatbot! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
