################# Type - 1 ###################

#### level - 1

# 1. 

    # 1
    # 2
    # 3
    # 4 

# 2.
    # 2 4 6 8

# 3.
    # 5 4 3 2 1 

# 4.
    # Finished

# 5.
    # 2 3 4 5
    
    
#### Level - 2

# 6.
    # 1 2 3 Done
    
# 7. 
    # 1 4 7 

# 8.
    # 7 4 1 -2


#### Level - 3

# 9. 
    #  10

# 10.
    # 16

# 11.
    # 2 1 0

# 12.
    # 58 5 0


#### Level - 4

# 13.
    # 2 4 6 

# 14.
    # odd even odd even odd 

# 15. 
    # 1 2 4 8

# 16. 
    # 5 3 1  stop: -1
    
    
#### Level - 5

# 17.
    # A
    # AA
    # AAA
    # AAAA

# 18.
    # PY
    # PYT
    # PYTT
    # PYTTT
    # PYTTTT

# 19.
    # 3 (WHILE LOOP DOESNT RUN AT ALL)
    
# 20.
    # B - since the condition for the while loop to run is always True.
    
    
##### Reflection Questions

# 1. Why must a loop variable often be updated inside a while loop?
# To ensure the loop eventually terminates. If the loop variable isn't updated, the condition will never become false, causing an infinite loop.

# 2. Can a while loop execute zero times? Give an example from this worksheet.
# Yes, if the condition evaluates to False on the very first check, the loop is entirely skipped. Q4 (count = 7; while count < 5) and Q19 (x = 3; while x > 10) are examples of this.

# 3. What is the difference between updating a variable before print() and after print()?
# Updating the variable before print() modifies the value first, meaning the first printed value is the newly updated one (e.g., Q5 starts at 2). Updating after print() displays the current value before it gets changed for the next iteration (e.g., Q1 starts at 1).

# 4. How can you recognize a possible infinite loop by reading the code?
# By checking the loop variable's initial value, the condition, and how it is updated. If the update moves the variable's value away from making the condition false (like subtracting when the condition waits for it to reach a higher maximum, as seen in Q20), or if there is no update at all, it's an infinite loop.

# 5. Why should you trace the condition again after every update?
# Because the variable's value changes during the loop execution. Sometimes a variable can dip below or shoot past a threshold mid-loop, and tracing helps predict exactly when the loop will evaluate as False upon the next check at the top.


# Type 2: Basic While Loop Problems — Statement Based (Python Version)

# Level 1: Basic Counting


# Q21. Print Numbers from 1 to N
# Task: Take a positive integer N and print all numbers from 1 to N, each on a new line.
# Input: 5
# Expected Output:
# 1
# 2
# 3
# 4
# 5

target_n = 5
current_num = 1

while current_num <= target_n:
    print(current_num)
    current_num += 1


# Q22. Print Numbers from N to 1
# Task: Take a positive integer N and print the numbers in descending order, from N to 1.
# Input: 5
# Expected Output:
# 5
# 4
# 3
# 2
# 1
count_down_n = 5

while count_down_n >= 1:
    print(count_down_n)
    count_down_n -= 1


# Q23. Print Even Numbers up to N
# Task: Take a positive integer N and print all even numbers from 2 up to N. If N is odd, stop at the last even number below it.
# Input: 10
# Expected Output:
# 2
# 4
# 6
# 8
# 10

even_limit = 10
even_starter = 2

while even_starter <= even_limit:
    print(even_starter)
    even_starter += 2


# Q24. Print Odd Numbers up to N
# Task: Take a positive integer N and print all odd numbers from 1 up to N.
# Input: 9
# Expected Output:
# 1
# 3
# 5
# 7
# 9

odd_limit = 9
odd_starter = 1

while odd_starter <= odd_limit:
    print(odd_starter)
    odd_starter += 2


# Q25. Print Multiples of a Number
# Task: Take two positive integers, K and N. Print the multiples of K that are less than or equal to N.
# Input:
# K = 3
# N = 15
# Expected Output:
# 3
# 6
# 9
# 12
# 15

k = 3
max_multiple_limit = 15
current_multiple = k

while current_multiple <= max_multiple_limit:
    print(current_multiple)
    current_multiple += k


# Level 2: Counting with Small Changes


# Q26. Multiplication Table
# Task: Take an integer N and print its multiplication table from N × 1 to N × 10.
# Input: 4
# Expected Output:
# 4 x 1 = 4
# 4 x 2 = 8
# ...
# 4 x 10 = 40

table_number = 4
multiplier = 1

while multiplier <= 10:
    print(f"{table_number} x {multiplier} = {table_number * multiplier}")
    multiplier += 1


# Q27. Count by a Given Step
# Task: Take two positive integers, START and STEP. Starting from START, print the next five values, adding STEP after each value. Print exactly five numbers.
# Input:
# START = 2
# STEP = 3
# Expected Output:
# 2
# 5
# 8
# 11
# 14

start_value = 2
step_value = 3
print_count = 1

while print_count <= 5:
    print(start_value)
    start_value += step_value
    print_count += 1


# Q28. Sum of Numbers from 1 to N
# Task: Take a positive integer N and calculate the sum of all integers from 1 to N. Print only the final sum.
# Input: 5
# Expected Output: 15

sum_limit = 5
total_sum = 0
number_to_add = 1

while number_to_add <= sum_limit:
    total_sum += number_to_add
    number_to_add += 1
    
print(total_sum)


# Q29. Sum of Even Numbers up to N
# Task: Take a positive integer N and calculate the sum of all even numbers from 2 up to N.
# Input: 10
# Expected Output: 30

even_sum_limit = 10
total_even_sum = 0
even_adder = 2

while even_adder <= even_sum_limit:
    total_even_sum += even_adder
    even_adder += 2
    
print(total_even_sum)


# Q30. Sum of Odd Numbers up to N
# Task: Take a positive integer N and calculate the sum of all odd numbers from 1 up to N.
# Input: 7
# Expected Output: 16

odd_sum_limit = 7
total_odd_sum = 0
odd_adder = 1

while odd_adder <= odd_sum_limit:
    total_odd_sum += odd_adder
    odd_adder += 2
    
print(total_odd_sum)


# Level 3: Simple Repeated Calculations

# Q31. Calculate the Total Cost
# Task: A shop sells one notebook for PRICE rupees. Take the price of one notebook and the number of notebooks purchased, QUANTITY. Calculate the total cost using repeated addition.
# Input:
# PRICE = 20
# QUANTITY = 4
# Expected Output: 80

price_per_item = 20
item_quantity = 4
total_cost = 0
items_counted = 1

while items_counted <= item_quantity:
    total_cost += price_per_item
    items_counted += 1
    
print(total_cost)


# Q32. Calculate Total Savings
# Task: A student saves the same amount of money every day. Take DAILY_SAVING and DAYS. Calculate the total amount saved after that many days using a loop.
# Input:
# DAILY_SAVING = 25
# DAYS = 6
# Expected Output: 150

daily_saving = 25
total_days = 6
final_savings = 0
current_day = 1

while current_day <= total_days:
    final_savings += daily_saving
    current_day += 1
    
print(final_savings)


# Q33. Calculate a Number Raised to a Power
# Task: Take two non-negative integers, BASE and POWER. Calculate BASE raised to POWER using repeated multiplication. Assume POWER is between 0 and 8.
# Input:
# BASE = 3
# POWER = 4
# Expected Output: 81

base_num = 3
power_num = 4
result_power = 1
multiply_count = 1

while multiply_count <= power_num:
    result_power *= base_num
    multiply_count += 1
    
print(result_power)


# Q34. Calculate Factorial
# Task: Take a non-negative integer N and calculate its factorial. The factorial of N is the product of all integers from 1 to N. Remember that 0! = 1.
# Input: 5
# Expected Output: 120

fact_number = 5
factorial_result = 1
fact_counter = 1

while fact_counter <= fact_number:
    factorial_result *= fact_counter
    fact_counter += 1
    
print(factorial_result)


# Q35. Find the Sum from START to END
# Task: Take two integers, START and END, where START is less than or equal to END. Calculate the sum of all integers from START through END, including both endpoints.
# Input:
# START = 3
# END = 7
# Expected Output: 25

range_start = 3
range_end = 7
range_sum = 0

while range_start <= range_end:
    range_sum += range_start
    range_start += 1
    
print(range_sum)


# Level 4: Read the Condition Carefully

# Q36. Count Down by Two
# Task: Take a positive even integer N. Print numbers from N down to 2, decreasing by 2 each time.
# Input: 10
# Expected Output:
# 10
# 8
# 6
# 4
# 2

count_by_two_start = 10

while count_by_two_start >= 2:
    print(count_by_two_start)
    count_by_two_start -= 2


# Q37. Repeatedly Divide by Two
# Task: Take a positive integer N. Print the value of N after repeatedly applying integer division by 2. Continue while the value is greater than 0. Print each new value after dividing.
# Input: 20
# Expected Output:
# 10
# 5
# 2
# 1
# 0

divide_target = 20

while divide_target > 0:
    divide_target = divide_target // 2 
    print(divide_target)


# Q38. Count How Many Steps Are Needed
# Task: Start with a positive integer N. In each step, subtract 3 from the number. Continue until the value becomes less than or equal to 0. Print the number of steps taken.
# Input: N = 11
# Expected Output: 4

step_number = 11
step_count = 0

while step_number > 0:
    step_number -= 3
    step_count += 1
    
print(step_count)


# Q39. Save Until the Target Is Reached
# Task: A student already has SAVED rupees and adds DAILY_AMOUNT rupees each day. Calculate how many days are needed for the savings to become greater than or equal to TARGET. Assume SAVED is less than TARGET and DAILY_AMOUNT is positive.
# Input:
# SAVED = 20
# DAILY_AMOUNT = 15
# TARGET = 70
# Expected Output: 4

already_saved = 20
daily_amount_add = 15
saving_target = 70
days_needed = 0

while already_saved < saving_target:
    already_saved += daily_amount_add
    days_needed += 1
    
print(days_needed)


# Q40. Print a Number Sequence in Reverse Steps
# Task: Take two positive integers, START and STEP, where START is divisible by STEP. Print values starting from START, subtracting STEP each time, and stop after printing 0.
# Input:
# START = 20
# STEP = 5
# Expected Output:
# 20
# 15
# 10
# 5
# 0

reverse_start = 20
reverse_step = 5

while reverse_start >= 0:
    print(reverse_start)
    reverse_start -= reverse_step
