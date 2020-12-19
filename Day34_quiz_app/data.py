import requests

params = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
}

content = requests.get(url="https://opentdb.com/api.php", params=params)
content.raise_for_status()
data = content.json()
question_data = data["results"]

# question_data = [
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The HTML5 standard was published in 2014.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#       ...
#     }
# ]
