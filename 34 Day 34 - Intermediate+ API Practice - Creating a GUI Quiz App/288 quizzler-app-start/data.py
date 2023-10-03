# question_data = [
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "Q1 The HTML5 standard was published in 2014.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "Q2 The HTML5 standard was published in 2014.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
# ]

import requests
# import html
link = "https://opentdb.com/api.php"
params = {
    "amount":10,
    "type":"boolean",
}
response = requests.get(link,params=params)
response.raise_for_status()
question_data = response.json()["results"]
