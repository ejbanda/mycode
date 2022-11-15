#!/usr/bin/env python3
import random
wordbank= ["indentation", "spaces"]

tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']


wordbank.append(4)

num = input("Enter a number between 1 and 21: ")
num = int(num) - 1 
num_rand = random.randint(0, len(tlgstudents) - 1)


student_name = tlgstudents[num]
student_rand = tlgstudents[num_rand]

print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")
print(f"RANDOM: {student_rand} always uses {wordbank[2]} {wordbank[1]} to indent.")
