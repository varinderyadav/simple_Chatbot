from datetime import datetime
def chatbot():
    print(" Chatbot: Hello! I,m your friendly chatbot. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if user_input in ["bye", "exit", "quit"]:
            print(" Chatbot: Goodbye! Have a great day! ")
            break

        elif user_input in ["hi", "hello", "hey","hey bro","hi bro",]:
            print(" Chatbot: Hello there! How can I help you today?")

        
        elif user_input in ["your name","tell me your name","name"]:
            print(" Chatbot: I'm ChatBot, your Python-coded friend. (DEVELOPED BY VARINDER YADAV)")

        elif "how are you" in user_input:
            print(" Chatbot: I'm doing great, thanks for asking! How about you?")

        elif "time" in user_input:
            
            now = datetime.now().strftime("%H:%M:%S")
            print(f" Chatbot: The current time is {now}.")

        elif "weather" in user_input:
            print(" Chatbot: I can't check the weather yet, but it's always sunny in Python world! ")

        elif "what is python" in user_input:
            print('''Python is a high-level, interpreted programming language known for its simplicity and readability.
             It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.''')    
        
        elif "what is java" in user_input:
            print('''  Java is a high-level, object-oriented programming language designed to be platform-independent through the Java Virtual Machine (JVM).
                     It is widely used for building web, desktop, and mobile applications due to its portability and robustness.
                     ''')
            
        # Default response
        else:
            print(" Chatbot: I'm not sure about that. Can you ask something else? Ask me some basic question?")

if __name__ == "__main__":
    chatbot()
