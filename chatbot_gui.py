import random
import tkinter as tk
from tkinter import scrolledtext, font
from calculator import calculator
from datetime import datetime

# ------------------ File helper functions (unchanged from main.py) ------------------

def save_chat(user_ques, reply):
    current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
    with open("history.txt", "a", encoding="utf-8") as file:
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

# ------------------ Response lists (unchanged from main.py) ------------------

greetings = [
    "😊Hello!", "😊Hi there!", "😊Hey!", "😊Nice to meet you!",
    "😊Hello! How can I help you?", "😊Hi! Hope you're having a great day!",
    "😊Welcome! Ask me anything."
]
goodbye = [
    "👋Goodbye!", "👋See you later!", "👋Have a wonderful day!", "👋Take care!",
    "👋See you soon!", "👋Bye! Keep learning Python!", "👋Hope to chat again."
]
thanks = [
    "👍You're welcome!", "👍Happy to help!", "👍No problem!", "👍Anytime!",
    "👍Glad I could help.", "👍My pleasure!", "👍Feel free to ask more questions."
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
    "🙂My name is PyBot.", "😇I'm PyBot, your Python assistant.", "😊You can call me PyBot."
]
unknown = [
    "🤔Sorry, I don't understand.", "🙂Could you ask in another way?", "😇I'm still learning.",
    "😕I don't have information about that.", "🙂Interesting question! I haven't learned that yet.",
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

# ------------------ Core brain of the bot ------------------
# This is the SAME if/elif chain as main.py. The only difference is that
# instead of living inside a `while True: input()` loop, it lives inside a
# function that the GUI calls every time the user presses Send / Enter.
# It takes the current user_name in and returns (reply, new_user_name) out,
# since a GUI has no "global" loop variable to update by itself.

def get_reply(user_ques, user_name):
    user_ques = user_ques.strip().lower()

    if any(op in user_ques for op in ["+", "-", "*", "/", "%", "**"]):
        reply = calculator(user_ques)

    elif "hi" in user_ques or "hello" in user_ques or "hey" in user_ques or "greetings" in user_ques:
        if user_name:
            reply = f"🤖 Robot: {random.choice(greetings)} {user_name}!"
        else:
            reply = f"🤖 Robot: {random.choice(greetings)}"

    elif any(x in user_ques for x in ["my name is", "i am", "i'm", "call me", "my self is"]):
        phrases = ["my name is", "i am", "i'm", "call me", "my self is"]
        for phrase in phrases:
            if phrase in user_ques:
                user_name = user_ques.replace(phrase, "").strip().title()
                break
        save_name(user_name)
        reply = f"🤖 Robot: Nice to meet you, {user_name}! 😊 I'll remember your name."

    elif "python" in user_ques:
        reply = f"🤖Robot: {random.choice(python_answers)}"

    elif "java" in user_ques:
        reply = f"🤖Robot: {random.choice(java_answers)}"

    elif "ai" in user_ques or "artificial intelligence" in user_ques:
        reply = f"🤖Robot: {random.choice(AI_answers)}"

    elif "thank" in user_ques or "thanks" in user_ques or "thank you" in user_ques or "that's good" in user_ques or "good job" in user_ques or "well done" in user_ques:
        reply = f"🤖Robot: {random.choice(thanks)}"

    elif "who are you" in user_ques or "what is your name" in user_ques or "who you are" in user_ques or "introduce yourself" in user_ques or "your name" in user_ques:
        reply = f"🤖Robot: {random.choice(self_reply)}"

    elif "time" in user_ques:
        now = datetime.now()
        reply = f"🤖Robot: Current Time: {now.strftime('%H:%M:%S')}"

    elif "date" in user_ques:
        today = datetime.now()
        reply = f"🤖Robot: Current Date: {today.strftime('%Y-%m-%d')}"

    elif "fact" in user_ques or "random fact" in user_ques or "tell me a fact" in user_ques or "give me a fact" in user_ques or "share a fact" in user_ques or "facts" in user_ques:
        reply = f"🤖Robot: {random.choice(facts)}"

    elif "bye" in user_ques or "exit" in user_ques or "quit" in user_ques or "goodbye" in user_ques:
        reply = random.choice(goodbye)

    else:
        reply = random.choice(unknown)

    save_chat(user_ques, reply)
    return reply, user_name


# ------------------ Tkinter GUI ------------------

class ChatBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PyBot - Chatbot")
        self.root.geometry("480x620")
        self.root.configure(bg="#1e1e2f")
        self.root.resizable(False, False)

        self.user_name = load_name()  # same load_name() call as main.py

        # ---- Header ----
        header = tk.Frame(root, bg="#141420", height=60)
        header.pack(fill="x", side="top")
        header.pack_propagate(False)
        tk.Label(
            header, text="🤖 PyBot", bg="#141420", fg="#ffffff",
            font=("Segoe UI", 16, "bold")
        ).pack(pady=12)

        # ---- Chat display ----
        self.chat_area = scrolledtext.ScrolledText(
            root, wrap="word", state="disabled", bg="#25253a", fg="#e8e8f0",
            font=("Segoe UI", 11), padx=10, pady=10, borderwidth=0
        )
        self.chat_area.pack(fill="both", expand=True, padx=10, pady=(10, 0))
        self.chat_area.tag_config("user", foreground="#7ecbff", justify="right")
        self.chat_area.tag_config("bot", foreground="#ffd479", justify="left")

        # ---- Input row ----
        input_frame = tk.Frame(root, bg="#1e1e2f")
        input_frame.pack(fill="x", padx=10, pady=10)

        self.entry = tk.Entry(
            input_frame, font=("Segoe UI", 12), bg="#2f2f45", fg="white",
            insertbackground="white", relief="flat"
        )
        self.entry.pack(side="left", fill="x", expand=True, ipady=8, padx=(0, 8))
        self.entry.bind("<Return>", lambda event: self.handle_send())
        self.entry.focus()

        send_btn = tk.Button(
            input_frame, text="Send", command=self.handle_send,
            bg="#4e8cff", fg="white", font=("Segoe UI", 11, "bold"),
            relief="flat", padx=16, cursor="hand2"
        )
        send_btn.pack(side="right")

        # Opening message, same as the two print() lines at the top of main.py
        self.display_bot_message("--------Welcome To the ChatBot---------")
        self.display_bot_message(">>>>You can type 'bye' to leave the chat<<<<<")

    def display_user_message(self, text):
        self.chat_area.config(state="normal")
        self.chat_area.insert("end", f"👤 You: {text}\n\n", "user")
        self.chat_area.config(state="disabled")
        self.chat_area.see("end")

    def display_bot_message(self, text):
        self.chat_area.config(state="normal")
        self.chat_area.insert("end", f"{text}\n\n", "bot")
        self.chat_area.config(state="disabled")
        self.chat_area.see("end")

    def handle_send(self):
        user_ques = self.entry.get().strip()
        if not user_ques:
            return
        self.entry.delete(0, "end")
        self.display_user_message(user_ques)

        reply, self.user_name = get_reply(user_ques, self.user_name)
        self.display_bot_message(reply)

        # same "bye/exit/quit/goodbye" check as main.py's break condition
        if any(word in user_ques.lower() for word in ["bye", "exit", "quit", "goodbye"]):
            self.entry.config(state="disabled")
            self.root.after(1500, self.root.destroy)


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatBotGUI(root)
    root.mainloop()
