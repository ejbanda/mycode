#!/usr/bin/env python3
import html



trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

def inputCheck(answer):
    if(answer == 'a' or answer == 'b' or answer == 'c' or answer == 'd'):
        return 0
    if(answer == 'A' or answer == 'B' or answer == 'C' or answer == 'D'):
        return 1
    return -1

print(f'Question: {trivia["question"]}')
print(f'A: {html.unescape(trivia["correct_answer"])}')
print(f'B: {html.unescape(trivia["incorrect_answers"][0])}')
print(f'C: {html.unescape(trivia["incorrect_answers"][1])}')
print(f'D: {html.unescape(trivia["incorrect_answers"][2])}')

user_input = input("Your answer: ")
check_response = -1

while(check_response == -1):
    check_response = inputCheck(user_input)
    if(check_response == 0):
        user_input = user_input.upper()
    if(check_response == -1):
        user_input = input("Guess again: ")

if(user_input == 'A'):
    print("You are right")
else:
    print("WRONG")
