from nltk.chat.util import Chat, reflections

pairs = [
    ["hi", ["Hello!", "Hey there!"]],
    ["what is your name?", ["I'm a rule-based chatbot."]],
    ["bye", ["Goodbye!", "See you later!"]],
]

chatbot = Chat(pairs, reflections)
chatbot.converse()
