from flask import Flask
from random import choice

app = Flask(__name__)

flashcards = {
    "computer_science": [
        {"id": 1, "question": "What is a variable?", "answer": "..."},
        {"id": 2, "question": "What is a function?", "answer": "..."}
    ],
    "english": [
        {"id": 1, "question": "Define metaphor", "answer": "..."},
        {"id": 2, "question": "What is alliteration?", "answer": "..."}
    ]
}

@app.route('/')
def home():
    return "Hello, this is your flashcard app!"

@app.route('/flashcards/<subject>')
def show_subject_cards(subject):
    thisSubjFlashcards = flashcards[subject]
    flashcard = choice(thisSubjFlashcards)
    # Render the same template but with different data
    print(f"{flashcard["question"]}")
    ans = input("What is your answer?\n")
    if ans in flashcard["answer"]:


if __name__ == '__main__':
    app.run(debug=True)