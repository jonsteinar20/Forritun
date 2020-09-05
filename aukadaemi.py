# Create a program that takes an integer as input, lets call it turns.
# This integer should indicate how many times the user wants to input a new integer.
# Next the program should let the user input turns many integers.
# The program should then print how many negative integers the user input.

turn = int(input("Turns: "))
negative = 0

for i in range(1, turn+1):
    turn = int(input("Your integer: "))
    if turn < 0:
        negative += 1
print(negative)