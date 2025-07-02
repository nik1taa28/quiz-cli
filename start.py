import random
import signal
import os
import json
from colorama import Fore,Style, init
init(autoreset=True)
class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException
if os.path.exists("scores.json"):
    with open("scores.json", "r") as f:
        scoredata=json.load(f)
else:
    scoredata={}
print(Fore.LIGHTBLACK_EX+ "Welcome to the quiz game!"+ Style.DIM)
username=input("Enter your name: ")
if username in scoredata:
    print(Fore.CYAN+f"📊 Welcome back, {username}! Your past scores: {scoredata[username]}"+Style.RESET_ALL)
else:
    print(Fore.CYAN+f"👋 Hello {username}, this is your first quiz!"+Style.RESET_ALL)

questions = [ {"question": "What is the capital of France?",
        "options": {"A": "Berlin", "B": "Madrid", "C": "Paris", "D": "Rome"},
        "answer": "C"},
        { "question": "What is 5 + 7?",
        "options": {"A": "10", "B": "12", "C": "13", "D": "11"},
        "answer": "B"},
        {
        "question": "Which planet is known as the Red Planet?",
        "options": {"A": "Earth", "B": "Venus", "C": "Mars", "D": "Jupiter"},
        "answer": "C"},
         {
    "question": "Which language is known as the 'language of the web'?",
    "options": {
      "A": "C++",
      "B": "Java",
      "C": "JavaScript",
      "D": "Python"
    },
    "answer": "C",
    "difficulty": "easy"
  },
  {
    "question": "What is the chemical symbol for gold?",
    "options": {
      "A": "Go",
      "B": "Au",
      "C": "Ag",
      "D": "Gd"
    },
    "answer": "B",
    "difficulty": "easy"
  },
  {
    "question": "Who painted the Mona Lisa?",
    "options": {
      "A": "Picasso",
      "B": "Da Vinci",
      "C": "Van Gogh",
      "D": "Rembrandt"
    },
    "answer": "B",
    "difficulty": "medium"
  },
  {
    "question": "Which data structure uses FIFO (First In First Out)?",
    "options": {
      "A": "Stack",
      "B": "Queue",
      "C": "Tree",
      "D": "Graph"
    },
    "answer": "B",
    "difficulty": "medium"
  },
  {
    "question": "In Python, what does the 'len()' function do?",
    "options": {
      "A": "Calculate length",
      "B": "Remove element",
      "C": "Create list",
      "D": "Add items"
    },
    "answer": "A",
    "difficulty": "easy"
  },
  {
    "question": "Which planet has the most moons?",
    "options": {
      "A": "Mars",
      "B": "Saturn",
      "C": "Jupiter",
      "D": "Neptune"
    },
    "answer": "B",
    "difficulty": "medium"
  },
  {
    "question": "What is the time complexity of binary search?",
    "options": {
      "A": "O(n)",
      "B": "O(log n)",
      "C": "O(n log n)",
      "D": "O(1)"
    },
    "answer": "B",
    "difficulty": "medium"
  },
  {
    "question": "Which command is used to initialize a new Git repository?",
    "options": {
      "A": "git start",
      "B": "git init",
      "C": "git new",
      "D": "git begin"
    },
    "answer": "B",
    "difficulty": "easy"
  },
  {
    "question": "Which number is the only even prime?",
    "options": {
      "A": "2",
      "B": "4",
      "C": "6",
      "D": "8"
    },
    "answer": "A",
    "difficulty": "easy"
  },
  {
    "question": "In computer networking, what does HTTP stand for?",
    "options": {
      "A": "High Transfer Text Protocol",
      "B": "HyperText Transfer Protocol",
      "C": "Hyper Transfer Protocol",
      "D": "Host Text Transfer Protocol"
    },
    "answer": "B",
    "difficulty": "medium"
  }
    
    ]
random.shuffle(questions)
signal.signal(signal.SIGALRM, timeout_handler)

score=0
for q in questions:
    print("\n"+ q["question"])
    for m,n in q["options"].items():
        print(f"{m}. {n}")
    signal.alarm(10)
    try:
        userans=input("⏳ You have 10 seconds! Your answer (A/B/C/D): ").strip().upper()
        signal.alarm(0)
        if userans==q["answer"]:
            print(Fore.GREEN+ "Correct!"+ Style.RESET_ALL)
            score+=1
        else:
            cor=q["answer"]
            print(Fore.RED+f"\nWrong! The correct answer was {cor}. {q['options'][cor]}" + Style.RESET_ALL)
    except:
        print(Fore.YELLOW+"\n⏰ Time’s up! No point for this one."+ Style.RESET_ALL)
        signal.alarm(0)

scoredata.setdefault(username, []).append(score)
with open("scores.json", "w") as f:
    json.dump(scoredata,f, indent=2)

print(Fore.LIGHTGREEN_EX+ f"\n🎉 you got {score} out of {len(questions)} correct. "+ Style.RESET_ALL)





    
    