"""
Name: David Montanez
Reason: YouTube MP4 Downloader
Created: July 12, 2021
Updated: July 12, 2021
"""

import random

## Program
class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

# def getRandomQuestion():
#     questions = ["What does CPU stand for", "What does RAM stand for", "What does GPU stand for"]
#     answers = ["central processing unit", "random access memory", "graphic processing unit"]

#     quizQuestions = dict(zip(questions, answers))
#     randomQuestion = random.randint(0, len(questions) - 1)
#     questionsAnswers = questions[randomQuestion]

#     return questionsAnswers

questions = ["What does CPU stand for", "What does RAM stand for", "What does GPU stand for", "What does PSU stand for"]
answers = ["central processing unit", "random access memory", "graphic processing unit", "power supply unit"]

print("Welcome to the Computer Quiz Game!!")
print("Answer these sets of questions and get your final grade at the end!")

# score = 4
# while(score != 0):
#     questions = ["What does CPU stand for", "What does RAM stand for", "What does GPU stand for", "What does PSU stand for"]
#     answers = ["central processing unit", "random access memory", "graphic processing unit", "power supply unit"]

#     quizQuestions = dict(zip(questions, answers))
#     randomQuestion = random.randint(0, len(questions) - 1)
#     questionsAnswers = questions[randomQuestion]
#     askedQuestion = set()

#     if(questionsAnswers not in askedQuestion):
#         userAnswer = input(f"{questionsAnswers}?: ").lower()
#         askedQuestion.add(questionsAnswers)


#     # if(userAnswer == quizQuestions[questionsAnswers]):
#     #     print("You are correct!!\n")
#     # else:
#     #     print("You are incorrect!!")
#     #     score -= 1

#             # askedQuestion.add(questionsAnswers)



#     # askedQuestion = set()
#     # question = getRandomQuestion()

#     # userAnswer = input(f"{question}?: ")
#     # askedQuestion.add(question)

#     # if(question in askedQuestion):

# print("Congratulations! You have finished the quiz!")
# print(f"You scored {score} out of 10!!")