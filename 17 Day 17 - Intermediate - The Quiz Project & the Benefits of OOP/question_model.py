class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


# from data import question_data
#
# class Question:
#     def __init__(self, number):
#         self.number = number
#         self.text = question_data[number]["text"]
#         self.answer = question_data[number]["answer"]
#
##Example
# question = Question(1)
# print(question.text)
# print(question.answer)