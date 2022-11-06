from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    text = item["text"]
    answer = item["answer"]
    question = Question(text, answer)
    question_bank.append(question)


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()





##My variant
# score = 0
# question_number = 1
# game_contining = True
# while game_contining:
#     for question in question_data:
#         question_text = question["text"]
#         answer_text = question["answer"]
#         print(f"Q.{question_number}: {question_text} True or False?")
#         user_answer = input()
#
#         if user_answer.lower() == answer_text.lower():
#             print("You got right!")
#             print(f"The correct answer was {answer_text}")
#             score += 1
#             print(f"Your current score is: {score}/{question_number}\n\n")
#         else:
#             print("That`s wrong")
#             print(f"The correct answer was {answer_text}")
#             print(f"Your current score is: {score}/{question_number}\n\n")
#             game_contining = False
#             break
#
#         question_number += 1
