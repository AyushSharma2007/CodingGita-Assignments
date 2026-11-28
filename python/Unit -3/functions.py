# Section A - Basic Function Practice

# Q1. Display a Welcome Message
# Create a function named display_welcome() that displays the welcome message box
# and call the function three times.

def display_welcome():
    print("================================")
    print("   Welcome to Python Programming")
    print("       Let's learn Functions!")
    print("================================")

display_welcome()
display_welcome()
display_welcome()


# Q2. Student Introduction Card
# Create a function named display_student_card(name, age, course) that displays
# the student's details in a formatted student card box.
# Call the function for at least three students: (Rahul, 18, B.Tech), (Priya, 19, BCA), (Aman, 20, B.Sc).

def display_student_card(name, age, course):
    print("+--------------------------------+")
    print("|         STUDENT CARD           |")
    print("+--------------------------------+")
    print(f"| Name  : {name:<23}|")
    print(f"| Age   : {age:<23}|")
    print(f"| Course: {course:<23}|")
    print("+--------------------------------+")

display_student_card("Rahul", 18, "B.Tech")
display_student_card("Priya", 19, "BCA")
display_student_card("Aman", 20, "B.Sc")


# Q3. Square, Cube, and Double
# Create three separate functions: calculate_square(number), calculate_cube(number),
# and calculate_double(number). Each function should calculate and display its result.
# Test cases: 2, 4, 5.

def calculate_square(number):
    print("Square:", number * number)

def calculate_cube(number):
    print("Cube:", number * number * number)

def calculate_double(number):
    print("Double:", number * 2)

calculate_square(2)
calculate_cube(2)
calculate_double(2)

calculate_square(4)
calculate_cube(4)
calculate_double(4)

calculate_square(5)
calculate_cube(5)
calculate_double(5)


# Q4. Simple Interest Calculator
# Create a function named calculate_simple_interest(principal, rate, time).
# Calculate SI = (P * R * T) / 100 and Amount = Principal + SI, then display both values.
# Test cases: (5000, 5, 2), (10000, 7, 3), (2500, 4, 1).

def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    total_amount = principal + simple_interest
    print(f"Principal: {principal}")
    print(f"Rate: {rate}%")
    print(f"Time: {time} years")
    print(f"Simple Interest: {simple_interest:g}")
    print(f"Total Amount: {total_amount:g}")

calculate_simple_interest(5000, 5, 2)
calculate_simple_interest(10000, 7, 3)
calculate_simple_interest(2500, 4, 1)


# Q5. Even or Odd Checker
# Create a function named check_even_odd(number) that displays whether the given
# number is even or odd.
# Test cases: 12, 7, 0, -5.

def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is an Even number.")
    else:
        print(f"{number} is an Odd number.")

check_even_odd(12)
check_even_odd(7)
check_even_odd(0)
check_even_odd(-5)


# Section B - Parameters, Arguments, and Return Values

# Q6. Find the Larger Number
# Create a function named find_largest(number_1, number_2) that returns the larger
# of the two numbers. Outside the function, call it, store the returned value in a
# variable, and display the result. Do not print inside the function.
# Test cases: (25, 40), (90, 15), (12, 12), (-5, -2).

def find_largest(number_1, number_2):
    if number_1 >= number_2:
        return number_1
    else:
        return number_2

largest_1 = find_largest(25, 40)
print("Largest number:", largest_1)
largest_2 = find_largest(90, 15)
print("Largest number:", largest_2)
largest_3 = find_largest(12, 12)
print("Largest number:", largest_3)
largest_4 = find_largest(-5, -2)
print("Largest number:", largest_4)


# Q7. Temperature Converter
# Create two functions: celsius_to_fahrenheit(celsius) using F = (9 / 5) * C + 32
# and fahrenheit_to_celsius(fahrenheit) using C = (5 / 9) * (F - 32).
# Return and display the values outside the functions.
# Test cases: C = 0, 25, 100 | F = 32, 68, 98.6.

def celsius_to_fahrenheit(celsius):
    return (9 / 5) * celsius + 32

def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(25))
print(celsius_to_fahrenheit(100))

print(fahrenheit_to_celsius(32))
print(fahrenheit_to_celsius(68))
print(fahrenheit_to_celsius(98.6))


# Q8. Understand the Difference Between print() and return
# Call calculate_sum_1(a, b) (which prints a + b) and calculate_sum_2(a, b)
# (which returns a + b) with (10, 20), (5, 7), and (100, 250).
# Store each result in a variable, display both, and answer the three questions in comments.

def calculate_sum_1(a, b):
    print(a + b)

def calculate_sum_2(a, b):
    return a + b

res_1 = calculate_sum_1(10, 20)
res_2 = calculate_sum_2(10, 20)
print(res_2)
print("Result from first function:", res_1)
print("Result from second function:", res_2)

res_3 = calculate_sum_1(5, 7)
res_4 = calculate_sum_2(5, 7)
print(res_4)
print("Result from first function:", res_3)
print("Result from second function:", res_4)

res_5 = calculate_sum_1(100, 250)
res_6 = calculate_sum_2(100, 250)
print(res_6)
print("Result from first function:", res_5)
print("Result from second function:", res_6)

# Answers:
# 1. calculate_sum_2 returns a value.
# 2. calculate_sum_1 has no return statement, so Python returns None by default.
# 3. No, print() only displays output on the screen and cannot be stored as a return value.


# Q9. Total Marks and Percentage
# Create a function named calculate_result(mark_1, mark_2, mark_3, mark_4, mark_5)
# that calculates total marks and percentage (each subject out of 100), returns both,
# and displays them outside the function.
# Test cases: (75, 80, 65, 90, 70), (50, 60, 55, 65, 70), (100, 95, 90, 85, 80).

def calculate_result(mark_1, mark_2, mark_3, mark_4, mark_5):
    total_marks = mark_1 + mark_2 + mark_3 + mark_4 + mark_5
    percentage = (total_marks / 500) * 100
    return total_marks, percentage

total, percentage = calculate_result(75, 80, 65, 90, 70)
print("Total Marks:", total)
print(f"Percentage: {percentage}%")

total, percentage = calculate_result(50, 60, 55, 65, 70)
print("Total Marks:", total)
print(f"Percentage: {percentage}%")

total, percentage = calculate_result(100, 95, 90, 85, 80)
print("Total Marks:", total)
print(f"Percentage: {percentage}%")


# Q10. Rectangle Area and Perimeter
# Create a function named rectangle_details(length, breadth) that calculates
# Area = Length * Breadth and Perimeter = 2 * (Length + Breadth), returns both,
# and displays them outside the function.
# Test cases: (10, 5), (8, 4), (7, 7).

def rectangle_details(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter

area, perimeter = rectangle_details(10, 5)
print("Area:", area)
print("Perimeter:", perimeter)

area, perimeter = rectangle_details(8, 4)
print("Area:", area)
print("Perimeter:", perimeter)

area, perimeter = rectangle_details(7, 7)
print("Area:", area)
print("Perimeter:", perimeter)


# Section C - Default and Keyword Arguments

# Q11. Personalized Greeting
# Create a function greet_user(name, message="Welcome to Python!") that displays
# the user's name and greeting message. Call it using both positional arguments,
# the default message, a keyword argument, and one extra name of your choice.

def greet_user(name, message="Welcome to Python!"):
    print(f"Hello {name}!")
    print(message)
    print()

greet_user("Rahul", "Good Morning!")
greet_user("Priya")
greet_user("Aman", message="Keep Learning!")
greet_user("Neha", message="Have a great day!")


# Q12. Electricity Bill Calculator
# Create a function named calculate_electricity_bill(units, rate=7) that returns
# Bill = Units * Rate and displays it outside the function.
# Call it with only units, with units and a custom rate, and with keyword arguments.
# Test cases: (100, default 7), (100, 8), (100, 6), (150, 8), (200, 6).

def calculate_electricity_bill(units, rate=7):
    return units * rate

bill_1 = calculate_electricity_bill(100)
bill_2 = calculate_electricity_bill(100, 8)
bill_3 = calculate_electricity_bill(rate=6, units=100)
print("Bill 1:", bill_1)
print("Bill 2:", bill_2)
print("Bill 3:", bill_3)

print("Bill 4:", calculate_electricity_bill(150, 8))
print("Bill 5:", calculate_electricity_bill(rate=6, units=200))


# Q13. Employee Salary Calculator
# Create a function calculate_salary(basic_salary, bonus=2000, deduction=500) that
# returns Final Salary = Basic Salary + Bonus - Deduction.
# Call it in four ways (only basic, basic + bonus, all three positional, and keyword).
# Explain why parameters with default values must come after non-default parameters.

def calculate_salary(basic_salary, bonus=2000, deduction=500):
    return basic_salary + bonus - deduction

print(calculate_salary(25000))
print(calculate_salary(25000, 3000))
print(calculate_salary(25000, 3000, 1000))
print(calculate_salary(basic_salary=25000, deduction=800, bonus=4000))

# Explanation: Positional arguments are matched left to right. Placing a default
# parameter before a non-default parameter creates ambiguity, so Python raises a SyntaxError.


# Section D - Applying Functions with Previously Learned Topics

# Q14. Number Digit Counter
# Create a function named count_digits(number) that returns the total number of digits
# in the given integer using arithmetic operators and a loop (no string conversion).
# Test cases: 7, 4826, 90000, 0.

def count_digits(number):
    if number == 0:
        return 1
    if number < 0:
        number = -number
    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count

print("Total digits:", count_digits(7))
print("Total digits:", count_digits(4826))
print("Total digits:", count_digits(90000))
print("Total digits:", count_digits(0))


# Q15. Sum of Digits
# Create a function named sum_of_digits(number) that returns the sum of all digits
# using a loop and the % and // operators.
# Test cases: 123, 482, 9005, 7.

def sum_of_digits(number):
    if number < 0:
        number = -number
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

print("Sum of digits:", sum_of_digits(123))
print("Sum of digits:", sum_of_digits(482))
print("Sum of digits:", sum_of_digits(9005))
print("Sum of digits:", sum_of_digits(7))


# Q16. Reverse a Number
# Create a function named reverse_number(number) that returns the reversed integer
# using a loop and arithmetic operators (no string conversion).
# Test cases: 123, 4826, 900, 7.

def reverse_number(number):
    sign = 1
    if number < 0:
        sign = -1
        number = -number
    reversed_value = 0
    while number > 0:
        reversed_value = reversed_value * 10 + (number % 10)
        number //= 10
    return sign * reversed_value

print("Reversed number:", reverse_number(123))
print("Reversed number:", reverse_number(4826))
print("Reversed number:", reverse_number(900))
print("Reversed number:", reverse_number(7))


# Q17. Palindrome Number Checker
# Create a function named is_palindrome(number) that returns True if the number reads
# the same forward and backward, otherwise False (use arithmetic operators and a loop,
# no string conversion). Display a suitable message outside the function.
# Test cases: 121, 1331, 123, 7.

def is_palindrome(number):
    if number < 0:
        return False
    original = number
    reversed_value = 0
    while number > 0:
        reversed_value = reversed_value * 10 + (number % 10)
        number //= 10
    return original == reversed_value

if is_palindrome(121):
    print("121 is a palindrome number.")
else:
    print("121 is not a palindrome number.")

if is_palindrome(1331):
    print("1331 is a palindrome number.")
else:
    print("1331 is not a palindrome number.")

if is_palindrome(123):
    print("123 is a palindrome number.")
else:
    print("123 is not a palindrome number.")

if is_palindrome(7):
    print("7 is a palindrome number.")
else:
    print("7 is not a palindrome number.")


# Q18. Prime Number Checker
# Create a function named is_prime(number) that returns True if the number is prime
# (greater than 1 with exactly two factors: 1 and itself), otherwise False.
# Display a suitable message outside the function.
# Test cases: 2, 17, 21, 1, 0.

def is_prime(number):
    if number <= 1:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True

if is_prime(2):
    print("2 is a prime number.")
else:
    print("2 is not a prime number.")

if is_prime(17):
    print("17 is a prime number.")
else:
    print("17 is not a prime number.")

if is_prime(21):
    print("21 is a prime number.")
else:
    print("21 is not a prime number.")

if is_prime(1):
    print("1 is a prime number.")
else:
    print("1 is not a prime number.")

if is_prime(0):
    print("0 is a prime number.")
else:
    print("0 is not a prime number.")


# Q19. Display Prime Numbers in a Range
# Create a function named display_primes(start, end) that checks every number from
# start to end (inclusive), displays all prime numbers found, and displays their total count
# without using lists.
# Test cases: (1, 10), (10, 30), (20, 25), (14, 16).

def display_primes(start, end):
    count = 0
    print("Prime numbers:", end="")
    for number in range(start, end + 1):
        if number > 1:
            prime = True
            divisor = 2
            while divisor * divisor <= number:
                if number % divisor == 0:
                    prime = False
                    break
                divisor += 1
            if prime:
                print(f" {number}", end="")
                count += 1
    if count == 0:
        print(" No prime numbers")
    else:
        print()
    print("Total prime numbers:", count)

display_primes(1, 10)
display_primes(10, 30)
display_primes(20, 25)
display_primes(14, 16)


# Q20. Student Result Report
# Create a function named display_student_report(name, mark_1, mark_2, mark_3) that
# calculates total marks, percentage (each subject out of 100), decides PASS (>= 40%)
# or FAIL (< 40%), and displays the formatted student report for at least three students.
# Test cases: (Rahul, 75, 80, 65), (Priya, 35, 45, 40), (Aman, 20, 30, 25), (Neha, 100, 100, 100).

def display_student_report(name, mark_1, mark_2, mark_3):
    total = mark_1 + mark_2 + mark_3
    percentage = (total / 300) * 100
    if percentage >= 40:
        result = "PASS"
    else:
        result = "FAIL"
    print("================================")
    print("         STUDENT REPORT")
    print("================================")
    print(f"Name       : {name}")
    print(f"Subject 1  : {mark_1}")
    print(f"Subject 2  : {mark_2}")
    print(f"Subject 3  : {mark_3}")
    print("--------------------------------")
    print(f"Total      : {total} / 300")
    print(f"Percentage : {percentage:.2f}%")
    print(f"Result     : {result}")
    print("================================")

display_student_report("Rahul", 75, 80, 65)
display_student_report("Priya", 35, 45, 40)
display_student_report("Aman", 20, 30, 25)
display_student_report("Neha", 100, 100, 100)
