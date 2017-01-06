import random
import game_functions

num_problems = int(input("How many problems would you like to attempt?: "))

while True:
    if num_problems < 1:
        print("Invalid number, try again.")
        print()
        num_problems = int(input("How many problems would you like to attempt?: "))
    else:
        break

width = int(input("How wide do you want your digits to be? 5-20: "))

while True:
    if width < 5 or width > 20:
        print("Invalid width, try again.")
        print()
        width = int(input("How wide do you want your digits to be? 5-20: "))
    elif width >= 5 and width <= 20:
        break

print()
print("Here we go!")

good_job_counter = 0

for i in range(num_problems):
    
    print("What is...")
    print()

    num1 = random.randint(0, 9)
    if num1 == 0:
        game_functions.number_0(width)
    elif num1 == 1:
        game_functions.number_1(width)
    elif num1 == 2:
        game_functions.number_2(width)
    elif num1 == 3:
        game_functions.number_3(width)
    elif num1 == 4:
        game_functions.number_4(width)
    elif num1 == 5:
        game_functions.number_5(width)
    elif num1 == 6:
        game_functions.number_6(width)
    elif num1 == 7:
        game_functions.number_7(width)
    elif num1 == 8:
        game_functions.number_8(width)
    elif num1 == 9:
        game_functions.number_9(width)

    print()
    
    plusmin = random.randint(0,1)
    if plusmin == 0:
        game_functions.plus(width)
        operator_string = "+"
    elif plusmin == 1:
        game_functions.minus(width)
        operator_string = "-"

    print()
            
    num2 = random.randint(0, 9)
    if num2 == 0:
        game_functions.number_0(width)
    elif num2 == 1:
        game_functions.number_1(width)
    elif num2 == 2:
        game_functions.number_2(width)
    elif num2 == 3:
        game_functions.number_3(width)
    elif num2 == 4:
        game_functions.number_4(width)
    elif num2 == 5:
        game_functions.number_5(width)
    elif num2 == 6:
        game_functions.number_6(width)
    elif num2 == 7:
        game_functions.number_7(width)
    elif num2 == 8:
        game_functions.number_8(width)
    elif num2 == 9:
        game_functions.number_9(width)

    user_ans = int(input("= "))

    if game_functions.check_answer(num1, num2, user_ans, operator_string) == True:
        print("Correct!")
        print()
        good_job_counter += 1
    else:
        print("Sorry, that's not correct.")
        print()

print("You got", good_job_counter, "out of", num_problems, "correct!")
        


