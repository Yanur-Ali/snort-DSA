# list of qs
# store the ans
# random pick qs
# ask qs
# check
# keep track
# display score

import random

questions = {
    "What is the biggest planet?" : "jupiter",
    "What is the sum of two even numbers?" : "even",
    "What is the Sun made of?" : "hot gas",
    "What is the dwarf planet called?" : "pluto",
    "What is the ans of 10*35?" : "350",
    "What is the colour of the sky?" : "blue",
    "What is the sound that cats make?" : "meow",
    "What is the colour of water?" : "colourless",
    "What is the  no. 5 multiplied by 5 equals?" : "25",
    "What is the nearest planet?" : "mercury",

}

def python_trivia_game():
    print("Hello...")
    questions_list = list(questions.keys())
    total_questions = 3
    score = 0

    selected_questions = random.sample(questions_list, total_questions)
    
    for idx, question in enumerate(selected_questions):
        print(f"{idx + 1}. {question}")
        user_answer = input("Your answer: ").lower().strip()
        correct_answer = questions[question]

        if user_answer == correct_answer.lower():
            print("correct!!\n")
            score += 1

        else:
            print(f"wrong. correction - {correct_answer}.\n")

    print(f"Game Over. final score is - {score}/{total_questions}")

python_trivia_game()
