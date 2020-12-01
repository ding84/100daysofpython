#!/usr/bin/python3

#
#
# Day 17: Add items from list as class object to another list and print them
#
#

from question_model import Question
from data import question_data

question_bank = []

#short version

# for item in question_data:
#     new_q = Question(item["text"], item["answer"])
#     question_bank.append(new_q)


#longer version

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(question_bank)

print(question_bank[0].text)
print(question_bank[0].answer)

for q in question_bank:
    print(q.text)
    print(q.answer)
    