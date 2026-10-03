#mini AI chatbot(rule based Chat Assistant in python)
import datetime
import time

name= input("Enter your name: ")
presenthours= datetime.datetime.now().hour
if presenthours < 12:
    print("Good Morning!", name)  
elif presenthours < 18:
    print("Good Afternoon!", name)    
else:
    print("Good Evening!", name)

print("Hello! I am your mini AI chatbot.")
print(" How can I assist you today?")
print("Type 'bye' to exit from bot")

#chatbot memory creation[ditionary of responses]
chatbot_memory = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi there! What can I do for you?",   
    "heyya": "Hey! How's it going?",
    "how are you": "I am doing well, thank you for asking!",
    "what is your name": "I am a mini AI chatbot created to assist you.",
    "what can you do": "I can answer your questions and provide information.",
    "happy": "That's great to hear! I'm glad you're happy.",
    "sad": "I'm sorry to hear that. Is there anything I can do to help?",
    "bye": "Goodbye! Have a great day!",
    "motivate": "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
    "inspire" : "The only way to do great work is to love what you do. - Steve Jobs",
    "joke" : "Why don't scientists trust atoms? Because they make up everything!",
    "weather" : "I am not sure about the weather, but you can check a weather app or website for the latest updates.",
}

#ethods/funtions to get response from chatbot memory
def getresponseof(user_input):
    user_input = user_input.lower()
    for eahkey in chatbot_memory:
        if eahkey in user_input:
            return chatbot_memory[eahkey]
    return "I'm sorry, I don't understand. Can you please rephrase your question?"  
#take user input and return response
while True:
    user_input = input("please ask you question:")
    reply = getresponseof(user_input)
    print(" bot_reply: ", reply)
    if "bye" in user_input.lower():
        print("Goodbye! Have a great day!")
        break
