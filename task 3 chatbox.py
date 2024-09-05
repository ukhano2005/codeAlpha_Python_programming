import nltk
from nltk.chat.util import Chat, reflections

# Sample conversation pairs (patterns and responses)
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hello|hey",
        ["Hello! How are you doing today?",]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot. You can call me ChatBot!",]
    ],
    [
        r"how are you ?",
        ["I'm just a program, but I'm doing great! How about you?",]
    ],
    [
        r"sorry (.*)",
        ["No problem!", "It's all good!"]
    ],
    [
        r"I am (.*) good",
        ["Great to hear that!", "Glad you are doing well!"]
    ],
    [
        r"what can you do ?",
        ["I can chat with you! Ask me anything.",]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day!",]
    ],
]

# Initialize the chatbot with pairs and reflections
def chatbot():
    print("Hi! I am a chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Run the chatbot
chatbot()
