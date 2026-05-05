class ChatBot:
    def get_response(self,message):

        message=message.lower()

        if "hello" in message:
            return "Hi! How can I help you?"
        elif "name" in message:
            return "I am your assistant chatbot"
        elif "help" in message:
            return "You can ask me about services or support"
        elif "bye" in message:
            return "Goodbye"
        else:
            return "Sorry, I don't understand"
 
bot=ChatBot()
while True:
    user_input = input("you: ")
    if user_input.lower() == "exit":
        print("good bye")
        break
    response = bot.get_response(user_input)
    print("bot: ", response)