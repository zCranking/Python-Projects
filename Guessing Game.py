# This is a Guessing Game
import time
from _curses import echo
from random import seed
from random import randint
delay = 1.8
print("How to choose a level")
time.sleep(delay)
print("You can choose from 3 different levels.")
time.sleep(delay)
print("Level one is very simple and the number will be a number between 1-10, with three tries.")
time.sleep(delay)
print("The second level will be a number between 0-50 and you will get 5 tries.")
time.sleep(delay)
print("The third level will be a number between 0-100 and you will get 7 tries.")
time.sleep(delay)
level = input("So pick a level between 1,2, and 3. To select which level type the number of the level: ")
if int(level) == 1:
    print(f"Ok so you chose level {level}.")
    for _ in range(1):
        random_number = randint(0,10)
        time.sleep(delay)
        print("Great so if this message pops up then that mean the computer has chosen a number!")
        time.sleep(delay)
    try_1 = input("To guess you just enter a number that you want to try and guess: ")
    time.sleep(delay)
    if int(try_1) > int(random_number):
        print(f"The number is less than {try_1}.")
    elif int(try_1) < int(random_number):
        print(f"The number is greater than {try_1}.")
    elif int(try_1) == 0 :
        print("TURN LOST!")
    else:
        print("YOU GOT IT CORRECT!")
        print("To play it again just rerun the code!")

    time.sleep(delay)
    try_2 = input("This is know your second guess, enter the number you think it could be: ")
    time.sleep(delay)
    if int(try_2) > int(random_number):
        print(f"The number is less than {try_2}.")
    elif int(try_2) < int(random_number):
        print(f"The number is greater than {try_2}. ")
    elif int(try_2) == 0:
        print("TURN LOST!")
    else:
        print("YOU GOT IT CORRECT!")
        print("To play it again just rerun the code!")

    time.sleep(delay)
    try_3 = input("This is now your last chance to guess! Choose the number wisely! Enter the number you think it is: ")
    time.sleep(delay)
    if int(try_3) > int(random_number):
        print(f"The number is less than {try_3}.")
        time.sleep(delay)
        print(f"Sorry you got it wrong the number was {int(random_number)}.")
        time.sleep(delay)
        print("To play it again just rerun the code!")
    elif int(try_3) < int(random_number):
        print(f"The number is greater than {try_3}.")
        time.sleep(delay)
        print(f"Sorry you got it wrong the number was {int(random_number)}.")
        time.sleep(delay)
        print("To play it again just rerun the code!")
    elif int(try_3) == 0:
        print("TURN LOST!")
        time.sleep(delay)
        print("To play it again just rerun the code!")
    elif int(try_3) == int(random_number):
        print(f"YOU GOT IT CORRECT! THE NUMBER WAS {int(random_number)}!")
        time.sleep(delay)
        print("To play it again just rerun the code!")
    else:
        print("This shouldn't be printed if so then please contact aravgupta2019@gmail.com, THANK YOU!")


elif int(level) == 2:
    print(f"Ok so you chose level {level}.")
    for _ in range(1):
        random_number = randint(0, 50)
        time.sleep(delay)
        print("Great so if this message pops up then that mean the computer has chosen a number!")
        time.sleep(delay)
    try_1 = input("To guess you just enter a number that you want to try and guess: ")
    time.sleep(delay)
    if int(try_1) > int(random_number):
        print(f"The number is less than {try_1}.")
    elif int(try_1) < int(random_number):
        print(f"The number is greater than {try_1}.")
    elif int(try_1) == 0:
        print("TURN LOST!")
    else:
        print("YOU GOT IT CORRECT!")
        time.sleep(delay)
        print("To play it again just rerun the code!")

    time.sleep(delay)
    try_2 = input("This is know your second guess, enter the number you think it could be: ")
    time.sleep(delay)
    if int(try_2) > int(random_number):
        print(f"The number is less than {try_2}.")
    elif int(try_2) < int(random_number):
        print(f"The number is greater than {try_2}. ")
    elif int(try_2) == 0:
        print("TURN LOST!")
    else:
        print("YOU GOT IT CORRECT!")
        time.sleep(delay)
        print("To play it again just rerun the code!")

    time.sleep(delay)
    try_3 = input("This is know your third guess, enter the number you think it could be: ")
    time.sleep(delay)
    if int(try_3) > int(random_number):
        print(f"The number is less than {try_3}.")
    elif int(try_3) < int(random_number):
        print(f"The number is greater than {try_3}. ")
    elif int(try_3) == 0:
        print("TURN LOST!")
    else:
        print("YOU GOT IT CORRECT!")
        time.sleep(delay)
        print("To play it again just rerun the code!")

    time.sleep(delay)
    try_4 = input("This is know your fourth guess, enter the number you think it could be: ")
    time.sleep(delay)
    if int(try_4) > int(random_number):
        print(f"The number is less than {try_4}.")
    elif int(try_4) < int(random_number):
        print(f"The number is greater than {try_4}. ")
    elif int(try_4) == 0:
        print("TURN LOST!")
    else:
        print("YOU GOT IT CORRECT!")
        time.sleep(delay)
        print("To play it again just rerun the code!")

    time.sleep(delay)
    try_5 = input("This is now your last chance to guess! Choose the number wisely! Enter the number you think it is: ")
    time.sleep(delay)
    if int(try_5) > int(random_number):
        print(f"The number is less than {try_5}.")
        time.sleep(delay)
        print(f"Sorry you got it wrong the number was {int(random_number)}.")
        time.sleep(delay)
        print("To play it again just rerun the code!")
    elif int(try_5) < int(random_number):
        print(f"The number is greater than {try_5}.")
        time.sleep(delay)
        print(f"Sorry you got it wrong the number was {int(random_number)}.")
        time.sleep(delay)
        print("To play it again just rerun the code!")
    elif int(try_5) == 0:
        print("TURN LOST!")
        time.sleep(delay)
        print("To play it again just rerun the code!")
    elif int(try_5) == int(random_number):
        print(f"YOU GOT IT CORRECT! THE NUMBER WAS {int(random_number)}!")
        time.sleep(delay)
        print("To play it again just rerun the code!")
    else:
        print("This shouldn't be printed if so then please contact aravgupta2019@gmail.com, THANK YOU!")

elif int(level) == 3:
    print(f"Ok so you chose level {level}.")
    for _ in range(1):
        random_number = randint(0, 100)
        time.sleep(delay)
        print("Great so if this message pops up then that mean the computer has chosen a number!")
        time.sleep(delay)
    try_1 = input("To guess you just enter a number that you want to try and guess: ")
    time.sleep(delay)
    if int(try_1) > int(random_number):
        print(f"The number is less than {try_1}.")
    elif int(try_1) < int(random_number):
        print(f"The number is greater than {try_1}.")
    elif int(try_1) == 0:
        print("TURN LOST!")
    else:
        print("YOU GOT IT CORRECT!")
        time.sleep(delay)
        print("To play it again just rerun the code!")

    time.sleep(delay)
    try_2 = input("This is know your second guess, enter the number you think it could be: ")
    time.sleep(delay)
    if int(try_2) > int(random_number):
        print(f"The number is less than {try_2}.")
    elif int(try_2) < int(random_number):
        print(f"The number is greater than {try_2}. ")
    elif int(try_2) == 0:
        print("TURN LOST!")
    else:
        print("YOU GOT IT CORRECT!")
        time.sleep(delay)
        print("To play it again just rerun the code!")

    time.sleep(delay)
    try_3 = input("This is know your third guess, enter the number you think it could be: ")
    time.sleep(delay)
    if int(try_3) > int(random_number):
        print(f"The number is less than {try_3}.")
    elif int(try_3) < int(random_number):
        print(f"The number is greater than {try_3}. ")
    elif int(try_3) == 0:
        print("TURN LOST!")
    else:
        print("YOU GOT IT CORRECT!")
        time.sleep(delay)
        print("To play it again just rerun the code!")

    time.sleep(delay)
    try_4 = input("This is know your fourth guess, enter the number you think it could be: ")
    time.sleep(delay)
    if int(try_4) > int(random_number):
        print(f"The number is less than {try_4}.")
    elif int(try_4) < int(random_number):
        print(f"The number is greater than {try_4}. ")
    elif int(try_4) == 0:
        print("TURN LOST!")
    else:
        print("YOU GOT IT CORRECT!")
        time.sleep(delay)
        print("To play it again just rerun the code!")

    time.sleep(delay)
    try_5 = input("This is know your fifth guess, enter the number you think it could be: ")
    time.sleep(delay)
    if int(try_5) > int(random_number):
        print(f"The number is less than {try_5}.")
    elif int(try_5) < int(random_number):
        print(f"The number is greater than {try_5}. ")
    elif int(try_5) == 0:
        print("TURN LOST!")
    else:
        print("YOU GOT IT CORRECT!")
        time.sleep(delay)
        print("To play it again just rerun the code!")

    time.sleep(delay)
    try_6 = input("This is know your sixth guess, enter the number you think it could be: ")
    time.sleep(delay)
    if int(try_6) > int(random_number):
        print(f"The number is less than {try_6}.")
    elif int(try_6) < int(random_number):
        print(f"The number is greater than {try_6}. ")
    elif int(try_6) == 0:
        print("TURN LOST!")
    else:
        print("YOU GOT IT CORRECT!")
        time.sleep(delay)
        print("To play it again just rerun the code!")

    time.sleep(delay)
    try_7 = input("This is know your seventh guess, enter the number you think it could be: ")
    time.sleep(delay)
    if int(try_7) > int(random_number):
        print(f"The number is less than {try_7}.")
    elif int(try_7) < int(random_number):
        print(f"The number is greater than {try_7}. ")
    elif int(try_7) == 0:
        print("TURN LOST!")
    else:
        print("YOU GOT IT CORRECT!")
        time.sleep(delay)
        print("To play it again just rerun the code!")

    time.sleep(delay)
    try_8 = input("This is now your last chance to guess! Choose the number wisely! Enter the number you think it is: ")
    time.sleep(delay)
    if int(try_8) > int(random_number):
        print(f"The number is less than {try_8}.")
        time.sleep(delay)
        print(f"Sorry you got it wrong the number was {int(random_number)}.")
        time.sleep(delay)
        print("To play it again just rerun the code!")
    elif int(try_8) < int(random_number):
        print(f"The number is greater than {try_8}.")
        time.sleep(delay)
        print(f"Sorry you got it wrong the number was {int(random_number)}.")
        time.sleep(delay)
        print("To play it again just rerun the code!")
    elif int(try_8) == 0:
        print("TURN LOST!")
        time.sleep(delay)
        print("To play it again just rerun the code!")
    elif int(try_8) == int(random_number):
        print(f"YOU GOT IT CORRECT! THE NUMBER WAS {int(random_number)}!")
        time.sleep(delay)
        print("To play it again just rerun the code!")
    else:
        print("This shouldn't be printed if so then please contact aravgupta2019@gmail.com, THANK YOU!")

else:
    print(" You didn't type anything so you will have to rerun the code. THANK YOU!")