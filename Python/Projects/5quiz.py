import random

# Define the list of questions and answers
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Kolkata","New Delhi", "Chennai"],
        "answer": "New Delhi"
    },
    {
        "question": "What is the national bird of India?",
        "options": ["Peacock", "Crow", "Pigeon", "Sparrow"],
        "answer": "Peacock"
    },
    {
        "question": "Who is the current president of India?",
        "options": ["Narendra Modi", "Ram Nath Kovind", "Rahul Gandhi", "Sonia Gandhi"],
        "answer": "Ram Nath Kovind"
    },
    {
        "question": "Who wrote the state anthem of Karnataka?",
        "options": ["Siddaramaiah", "Kuvempu", "B.S. Yediyurappa", "Sarvepalli Radhakrishnan"],
        "answer": "Kuvempu"
    },
    {
        "question": "What is the national animal of India?",
        "options": ["Tiger", "Lion", "Leopard", "Elephant"],
        "answer": "Tiger"
    }
]

def play_game(questions):
    score = 0
    random.shuffle(questions)
    for q in questions:
        print(q["question"])
        for i, option in enumerate(q["options"]):
            print(f"{i+1}. {option}")
        user_answer = input("Enter your answer (1-4): ")
        if user_answer.isdigit() and int(user_answer) in range(1, 5):
            if q["options"][int(user_answer)-1] == q["answer"]:
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")
        else:
            print("Invalid answer!")
    print(f"Your score is {score}/{len(questions)}")

if __name__ == "__main__":
    play_game(questions)
