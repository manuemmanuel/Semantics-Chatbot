import streamlit as st
from ChatterBot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new instance of a ChatBot
chatbot = ChatBot("MyChatBot")

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English language corpus data
trainer.train("chatterbot.corpus.english")

def get_bot_response(user_input):
    # Get a response from the chatbot based on the user's input
    response = chatbot.get_response(user_input)
    return str(response)

def main():
    st.title("ChatterBot Chatbot")

    user_input = st.text_input("You: ")

    if st.button("Send"):
        if user_input:
            # Get the bot's response based on user input
            bot_response = get_bot_response(user_input)

            # Display the bot's response
            st.write(f"Bot: {bot_response}")

if __name__ == "__main__":
    main()
