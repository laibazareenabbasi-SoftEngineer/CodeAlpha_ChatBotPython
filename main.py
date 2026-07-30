import random
from calculator import calculator
from datetime import datetime
print("--------Welcome To the ChatBot---------")
print(">>>>You can Exit.Type 'bye' and leave the chatot<<<<<")

def save_chat(user_ques, reply):
    current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    with open("history.txt", "a",encoding="utf-8") as file:
        file.write(f"[{current_time}]\n")
        file.write(f"User: {user_ques}\n")
        file.write(f"Bot: {reply}\n\n")
def save_name(name):
    with open("memory.txt", "w", encoding="utf-8") as file:
        file.write(name)

def load_name():
    try:
        with open("memory.txt", "r", encoding="utf-8") as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

greetings = [
    "😊Hello!",
    "😊Hi there!",
    "😊Hey!",
    "😊Nice to meet you!",
    "😊Hello! How can I help you?",
    "😊Hi! Hope you're having a great day!",
    "😊Welcome! Ask me anything."
]
goodbye = [
    "👋Goodbye!",
    "👋See you later!",
    "👋Have a wonderful day!",
    "👋Take care!",
    "👋See you soon!",
    "👋Bye! Keep learning Python!",
    "👋Hope to chat again."
]
thanks = [
    "👍You're welcome!",
    "👍Happy to help!",
    "👍No problem!",
    "👍Anytime!",
    "👍Glad I could help.",
    "👍My pleasure!",
    "👍Feel free to ask more questions."
]
python_answers = [
    "Python is one of the easiest programming languages to learn.",
    "Python is used for AI, web development, automation, and data science.",
    "Python is an interpreted language.",
    "Python was created by Guido van Rossum.",
    "Python has simple and readable syntax.",
    "Python is widely used in machine learning."
]
java_answers = [
    "Java is an object-oriented programming language.",
    "Java runs on the Java Virtual Machine (JVM).",
    "Java is platform-independent.",
    "Java is widely used for Android development.",
    "Java follows the 'Write Once, Run Anywhere' principle."
]
AI_answers = [
    "AI stands for Artificial Intelligence.",
    "AI enables computers to learn and solve problems.",
    "Machine Learning is a branch of AI.",
    "ChatGPT is an example of an AI application."
]
self_reply = [
    "🙂My name is PyBot.",
    "😇I'm PyBot, your Python assistant.",
    "😊You can call me PyBot."
]
unknown = [
    "🤔Sorry, I don't understand.",
    "🙂Could you ask in another way?",
    "😇I'm still learning.",
    "😕I don't have information about that.",
    "🙂Interesting question! I haven't learned that yet.",
    "😊Can you ask something related to programming?"
]
facts = [
    "🐍 Python was created by Guido van Rossum in 1991.",
    "🌍 There are more than 7,000 languages spoken around the world.",
    "💻 The first computer bug was an actual moth found in a computer.",
    "🚀 The first person in space was Yuri Gagarin in 1961.",
    "🌊 About 71% of the Earth's surface is covered by water.",
    "🧠 The human brain contains about 86 billion neurons.",
    "☀️ The Sun is a star, not a planet.",
    "🌙 The Moon has no atmosphere.",
    "⚡ Lightning is hotter than the surface of the Sun.",
    "🐧 Linux is open-source and free to use.",
    "🌐 The World Wide Web was invented by Tim Berners-Lee.",
    "📱 Android is based on the Linux kernel.",
    "🤖 AI stands for Artificial Intelligence.",
    "💾 SSDs are generally faster than HDDs.",
    "🔐 HTTPS encrypts communication between your browser and websites."
]
user_name = load_name()
while True:
    user_ques = input("👤 You: ").strip().lower()

    if any(op in user_ques for op in ["+", "-", "*", "/", "%", "**"]):
        reply = calculator(user_ques)
        print(reply)
        save_chat(user_ques, reply)

    
    elif "hi" in user_ques or "hello" in user_ques or "hey" in user_ques or "greetings" in user_ques:
          if user_name:
            reply = f"🤖 Robot: {random.choice(greetings)} {user_name}!"
          else:
            reply = f"🤖 Robot: {random.choice(greetings)}"
          # NOTE: these two lines used to be indented only under the "else" above,
          # so a returning user (whose name we already know) never got a reply printed
          # or saved to history. Moving them here (outside the if/else) fixes that.
          print(reply)
          save_chat(user_ques, reply)

    elif any(x in user_ques for x in ["my name is", "i am", "i'm", "call me", "my self is"]):
        phrases = ["my name is", "i am", "i'm", "call me", "my self is"]
        for phrase in phrases:
            if phrase in user_ques:
                user_name = user_ques.replace(phrase, "").strip().title()
                break
        save_name(user_name)

        reply = f"🤖 Robot: Nice to meet you, {user_name}! 😊 I'll remember your name."
        print(reply)
        save_chat(user_ques, reply)

    elif "python" in user_ques:
        reply=f"🤖Robot: {random.choice(python_answers)}"
        print(reply)
        save_chat(user_ques, reply)
        
    elif "java" in user_ques:
        reply=f"🤖Robot: {random.choice(java_answers)}"
        print(reply)
        save_chat(user_ques, reply)

    elif "ai" in user_ques or "artificial intelligence" in user_ques:
        reply=f"🤖Robot: {random.choice(AI_answers)}"   
        print(reply)
        save_chat(user_ques, reply)

    elif "thank" in user_ques or "thanks" in user_ques or "thank you" in user_ques or "that's good" in user_ques or "good job" in user_ques or "well done" in user_ques:
        reply=f"🤖Robot: {random.choice(thanks)}"
        print(reply)
        save_chat(user_ques, reply)

    elif "who are you" in user_ques or "what is your name" in user_ques or "who you are" in user_ques or "introduce yourself" in user_ques or "your name" in user_ques:
        reply=f"🤖Robot: {random.choice(self_reply)}"
        print(reply)
        save_chat(user_ques, reply)

    elif "time" in user_ques:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        reply=f"🤖Robot: Current Time: {current_time}"
        print(reply)
        save_chat(user_ques, reply)
    elif "date" in user_ques:
        today = datetime.now()
        reply=f"🤖Robot: Current Date: {today.strftime('%Y-%m-%d')}"
        print(reply)
        save_chat(user_ques, reply)

    elif "fact" in user_ques or "random fact" in user_ques or "tell me a fact" in user_ques or "give me a fact" in user_ques or "share a fact" in user_ques or "facts" in user_ques:
        reply=f"🤖Robot: {random.choice(facts)}"
        print(reply)
        save_chat(user_ques, reply)

    elif "bye" in user_ques or "exit" in user_ques or "quit" in user_ques or "goodbye" in user_ques:
        reply=random.choice(goodbye)
        print(reply)
        save_chat(user_ques, reply)
        break

    else:
        reply=random.choice(unknown)
        print(reply)
        save_chat(user_ques, reply)
