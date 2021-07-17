"""
Name: David Montanez
Reason: YouTube MP4 Downloader
Created: July 13, 2021
Updated: July 13, 2021
"""

import random

## Program
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questionPrompts = [
    "What does CPU stand for",
    "What does RAM stand for",
    "What does GPU stand for",
    "What does PSU stand for"
]

questionAnswers = [
    "central processing unit",
    "random access memory",
    "graphic processing unit",
    "power supply unit"
]

quizQuestion = dict(zip(questionPrompts, questionAnswers))
randomQuestion = random.randint(0, len(questionPrompts) - 1)
question = questionPrompts[randomQuestion]
askedQuestions = set()

def randomQuest(question):

    if(question not in askedQuestions):

        randomQuestion = random.randint(0, len(questionPrompts) - 1)
        question = questionPrompts[randomQuestion]
        askedQuestions.add(question)

        return question

# questions = [
#     Question(randomQuestion, quizAnswers)
#     # Question(questionPrompts[0], "central processing unit"),
#     # Question(questionPrompts[1], "random access memory"),
#     # Question(questionPrompts[2], "graphic processing unit"),
#     # Question(questionPrompts[3], "power supply unit"),
# ]

def runQuiz():
    score = 0
    totalQuestion = 0
    
    # while(totalQuestion != str(len(questionPrompts))):
    while(totalQuestion <= len(questionPrompts)):

        userAnswer = input(f"{randomQuest(question)}?: ").lower()
        totalQuestion += 1

        if(userAnswer == quizQuestion[question]):
            print("You are correct!!\n")
            score += 1
        else:
            print("You are incorrect!!")


    print("\nCongratulations! You finished the quiz!!")
    print(f"You got {score} out of {str(len(questionPrompts))} correct!")

print("Welcome to the Computer Quiz Game!!")
print("Answer these sets of questions and get your final grade at the end!")
runQuiz()