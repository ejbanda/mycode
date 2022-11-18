#!/usr/bin/env python3

round = 0

while True:
    round += 1
    print('Finish the movie title, "Monty Python\'s The Life of ______"')

    answer = input("Your guess--> ").capitalize()

    if answer == 'Brian':
        print('Correct')
        break
    elif answer == 'Shrubbery':
        print('You gave the super secret answer!')
        break
    elif round == 3:
        print("Sorry, the answer was Brian.")
        break
    else:
        print("Sorry! Try again!")

