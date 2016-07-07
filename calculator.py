"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True: 
    requested_operation = raw_input()
    list_of_requested_operation = requested_operation.split(" ")

    for i in range(len(list_of_requested_operation)):
        if i != 0:
            list_of_requested_operation[i] = float(list_of_requested_operation[i])
    
    if list_of_requested_operation[0] == "q":
        break
    elif list_of_requested_operation[0] == "+":
        print add(list_of_requested_operation[1], list_of_requested_operation[2])
    elif list_of_requested_operation[0] == "-":
        print subtract(list_of_requested_operation[1], list_of_requested_operation[2])
    elif list_of_requested_operation[0] == "*":
        print multiply(list_of_requested_operation[1],list_of_requested_operation[2])
    elif list_of_requested_operation[0] == "/":
        print divide(list_of_requested_operation[1], list_of_requested_operation[2])
    elif list_of_requested_operation[0] == "square":
        print square(list_of_requested_operation[1])
    elif list_of_requested_operation[0] == "cube":
        print cube(list_of_requested_operation[1])
    elif list_of_requested_operation[0] == "pow":
       print power(list_of_requested_operation[1], list_of_requested_operation[2])
    elif list_of_requested_operation[0] == "mod":
       print mod(list_of_requested_operation[1], list_of_requested_operation[2])
