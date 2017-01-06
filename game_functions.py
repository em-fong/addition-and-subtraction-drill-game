# function:   horizontal_line
# input:      a width value (integer)
# processing: prints a single horizontal line of the desired size
# output:     does not return anything

def horizontal_line(integer):
    print("*" * integer)

# function:   vertical_line
# input:      a shift value and a height value (both integers)
# processing: generates a single vertical line of the desired height.  the line is
#             offset from the left side of the screen using the shift value
# output:     does not return anything

def vertical_line(shift, height):
    for i in range(height):
        print(shift * " ", "*")


# function:   two_vertical_lines
# input:      a width value and a height value (both integers)
# processing: generates two vertical lines.  the first line is along the left side of
#             the screen. the second line is offset using the "width" value supplied
# output:     does not return anything

def two_vertical_lines(width, height):
    for i in range(height):
        if width <= 2:
            print("*", end="")
            print(width * "", end="")
            print("*")
        else:
            print("*", end="")
            print(width * " ", end="")
            print("*")
            
# function:   number_0
# input:      a width value (integer)
# processing: prints the number 0 as it would appear on a digital display
#             using the supplied width value
# output:     returns nothing

def number_0(width):

    print(width * " ", end="")
    horizontal_line(5)
    
    print(width * " ", end="")
    print("*", 3 * " ", "*", sep="")

    print(width * " ", end="")
    print("*", 3 * " ", "*", sep="")
    
    print(width * " ", end="")
    print("*", 3 * " ", "*", sep="")
    
    print(width * " ", end="")
    horizontal_line(5)

# function:   number_1
# input:      a width value (integer)
# processing: prints the number 1 as it would appear on a digital display
#             using the supplied width value
# output:     returns nothing

def number_1(width):
    vertical_line(width, 5)

# function:   number_2
# input:      a width value (integer)
# processing: prints the number 2 as it would appear on a digital display
#             using the supplied width value
# output:     returns nothing

def number_2(width):
    gap_width = width + 4
    
    print(width * " ", end="")
    horizontal_line(5)

    print(gap_width * " " + "*")
    
    print(width * " ", end="")
    horizontal_line(5)
    
    print(width * " ", end="")
    print("*")
    
    print(width * " ", end="")
    horizontal_line(5)

# function:   number_3
# input:      a width value (integer)
# processing: prints the number 3 as it would appear on a digital display
#             using the supplied width value
# output:     returns nothing

def number_3(width):
    gap_width = width + 4
    
    print(width * " ", end="")
    horizontal_line(5)
    
    print(gap_width * " " + "*")
    
    print(width * " ", end="")
    horizontal_line(5)
    
    print(gap_width * " " + "*")
    
    print(width * " ", end="")
    horizontal_line(5)

# function:   number_4
# input:      a width value (integer)
# processing: prints the number43 as it would appear on a digital display
#             using the supplied width value
# output:     returns nothing

def number_4(width):

    for i in range(2):
        print(width * " ", end="")
        print("*", 3 * " ", "*", sep="")

    print(width * " ", end="")
    horizontal_line(5)
    
    vertical_line(width + 3, 2)

# function:   number_5
# input:      a width value (integer)
# processing: prints the number 5 as it would appear on a digital display
#             using the supplied width value
# output:     returns nothing
    
def number_5(width):
    gap_width = width + 4
    
    print(width * " ", end="")
    horizontal_line(5)
    
    print(width * " ", end="")
    print("*")
    
    print(width * " ", end="")
    horizontal_line(5)
    
    print(gap_width * " " + "*")
    
    print(width * " ", end="")
    horizontal_line(5)

# function:   number_6
# input:      a width value (integer)
# processing: prints the number 6 as it would appear on a digital display
#             using the supplied width value
# output:     returns nothing

def number_6(width):
    gap_width = width + 4
    
    print(width * " ", end="")
    horizontal_line(5)
    
    print(width * " ", end="")
    print("*")
    
    print(width * " ", end="")
    horizontal_line(5)
    
    print(width * " ", end="")
    print("*", 3 * " ", "*", sep="")
    
    print(width * " ", end="")
    horizontal_line(5)

# function:   number_7
# input:      a width value (integer)
# processing: prints the number 37as it would appear on a digital display
#             using the supplied width value
# output:     returns nothing

def number_7(width):
    print(width * " ", end="")
    horizontal_line(5)
    
    vertical_line(width + 3, 4)

# function:   number_8
# input:      a width value (integer)
# processing: prints the number 8 as it would appear on a digital display
#             using the supplied width value
# output:     returns nothing

def number_8(width):
    
    print(width * " ", end="")
    horizontal_line(5)
    
    print(width * " ", end="")
    print("*", 3 * " ", "*", sep="")
    
    print(width * " ", end="")
    horizontal_line(5)
    
    print(width * " ", end="")
    print("*", 3 * " ", "*", sep="")
    
    print(width * " ", end="")
    horizontal_line(5)
    
# function:   number_9 
# input:      a width value (integer)
# processing: prints the number 9 as it would appear on a digital display
#             using the supplied width value
# output:     returns nothing

def number_9(width):

    gap_width = width + 4
    
    print(width * " ", end="")
    horizontal_line(5)
    
    print(width * " ", end="")
    print("*", 3 * " ", "*", sep="")
    
    print(width * " ", end="")
    horizontal_line(5)
    
    print(gap_width * " " + "*")

    print(gap_width * " " + "*")
    
# function:   plus
# input:      a width value (integer)
# processing: prints the addition sign as it would appear on a digital display
#             using the supplied width value
# output:     returns nothing

def plus(width):
    gap_width = width + 1

    print(gap_width * " ", "*")
    
    print(gap_width * " ", "*")
    
    print(width * " ", end="")
    horizontal_line(5)
    
    print(gap_width * " ", "*")
    
    print(gap_width * " ", "*")

# function:   minus
# input:      a width value (integer)
# processing: prints the subtration sign as it would appear on a digital display
#             using the supplied width value
# output:     returns nothing

def minus(width):
    print()

    print()

    print(width * " ", end="")
    horizontal_line(5)

    print()

    print()


# function:   check_answer
# input:      two numbers (number1 & number2, both integers); an answer (an integer)
#             and an operator (+ or -, expressed as a String)
# processing: determines if the supplied expression is correct.  for example, if the operator
#             is "+", number1 = 1, number2 = 2 and answer = 3 then the expression is correct
#             (1 + 2 = 3).
# output:     returns True if the expression is correct, False if it is not correct

def check_answer(num1, num2, ans, operator_string):
    if operator_string == "+":
        if ans == num1 + num2:
            return True
        else:
            return False
    else:
        if ans == num1 - num2:
            return True
        else:
            return False


