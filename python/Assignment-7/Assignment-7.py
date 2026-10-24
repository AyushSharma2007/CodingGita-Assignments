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

# Q41. Count the Digits
n = int(input("Q41 number: "))
count = 0
if n == 0:
    count = 1
while n > 0:
    count += 1
    n = n // 10
print(count)

# Q42. Find the Sum of Digits
n = int(input("Q42 number: "))
total = 0
while n > 0:
    total += n % 10
    n = n // 10
print(total)

# Q43. Reverse a Number
n = int(input("Q43 number: "))
rev = 0
if n == 0:
    print(0)
else:
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    print(rev)

# Q44. Find the Product of Digits
n = int(input("Q44 number: "))
prod = 1
if n == 0:
    prod = 0
while n > 0:
    prod *= n % 10
    n = n // 10
print(prod)

# Q45. Print Digits from Right to Left
n = int(input("Q45 number: "))
if n == 0:
    print(0)
while n > 0:
    print(n % 10)
    n = n // 10

# Q46. Find the First and Last Digit
n = int(input("Q46 number: "))
last_digit = n % 10
first_digit = n
while first_digit >= 10:
    first_digit = first_digit // 10
print("First digit:", first_digit)
print("Last digit:", last_digit)

# Q47. Count Even Digits
n = int(input("Q47 number: "))
count = 0
if n == 0:
    count = 1
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        count += 1
    n = n // 10
print(count)

# Q48. Count Odd Digits
n = int(input("Q48 number: "))
count = 0
while n > 0:
    digit = n % 10
    if digit % 2 != 0:
        count += 1
    n = n // 10
print(count)

# Q49. Find the Sum of Even Digits
n = int(input("Q49 number: "))
total = 0
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        total += digit
    n = n // 10
print(total)

# Q50. Find the Largest Digit
n = int(input("Q50 number: "))
max_digit = 0
if n == 0:
    max_digit = 0
while n > 0:
    digit = n % 10
    if digit > max_digit:
        max_digit = digit
    n = n // 10
print(max_digit)

# Q51. Find the Smallest Digit
n = int(input("Q51 number: "))
min_digit = 9
if n == 0:
    min_digit = 0
while n > 0:
    digit = n % 10
    if digit < min_digit:
        min_digit = digit
    n = n // 10
print(min_digit)

# Q52. Check Whether a Number Is a Palindrome
n = int(input("Q52 number: "))
orig = n
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10
if orig == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

# Q53. Count How Many Times a Digit Appears
n = int(input("Q53 number: "))
d = int(input("Q53 digit: "))
count = 0
if n == 0 and d == 0:
    count = 1
while n > 0:
    if n % 10 == d:
        count += 1
    n = n // 10
print(count)

# Q54. Check Whether All Digits Are the Same
n = int(input("Q54 number: "))
last_digit = n % 10
all_same = True
while n > 0:
    if n % 10 != last_digit:
        all_same = False
    n = n // 10
if all_same:
    print("Yes")
else:
    print("No")

# Q55. Compare the Sum of First and Last Digits with the Middle Digits' Sum
n = int(input("Q55 number: "))
last_digit = n % 10
n = n // 10
middle_sum = 0
while n >= 10:
    middle_sum += n % 10
    n = n // 10
first_digit = n
print("First and last digits sum:", first_digit + last_digit)
print("Middle digits sum:", middle_sum)

# Q56. Print Factorial Values from 1! to N!
n = int(input("Q56 N: "))
i = 1
fact = 1
while i <= n:
    fact = fact * i
    print(fact)
    i += 1

# Q57. Check Whether a Number Is a Factorial Value
n = int(input("Q57 N: "))
i = 1
fact = 1
while fact < n:
    i += 1
    fact = fact * i
if fact == n:
    print("Yes")
else:
    print("No")

# Q58. Find the Largest Factorial Not Greater Than N
n = int(input("Q58 N: "))
i = 1
fact = 1
while fact * (i + 1) <= n:
    i += 1
    fact = fact * i
print(fact)

# Output Guessing Section (Q59 - Q78)

# Q59 Output:
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3

# Q60 Output:
# 1 2 
# 1 2 

# Q61 Output:
# * 
# * * 
# * * * 

# Q62 Output:
# 1 2 3 
# 2 3 
# 3 

# Q63 Output:
# 1 2 End
# 1 2 End
# 1 2 End

# Q64 Output:
# 2
# 3
# 3
# 4
# Finished

# Q65 Output:
# A 1
# A 2
# B 1
# B 2
# B 3

# Q66 Output:
# 1 1
# 1 2

# Q67 Output:
# 11
# 33

# Q68 Output:
# X
# 1 X
# 1 2 X

# Q69 Output:
# 1 1
# 1 2
# 2 1
# 2 2
# 3 1
# 3 2

# Q70 Output:
# 1 2 |
# 1 2 |

# Q71 Output:
# 1 1
# 1 2
# 2 1
# 2 2

# Q72 Output:
# 1 1
# Next row
# 2 1
# Next row
# 3 1
# Next row

# Q73 Output:
# 1 1
# 1 3
# 1 4
# 2 1
# 2 3
# 2 4

# Q74 Output:
# 2 4 5 6 

# Q75 Output:
# 1 3 Row
# 1 3 Row
# 1 3 Row

# Q76 Output:
# 1 2
# 1 3
# 2 1
# 2 3
# 3 1
# 3 2

# Q77 Output:
# 1 1
# 1 3
# 2 1
# 2 3

# Q78 Output:
# 1 3 4 End
# 2 6 8 End
# 3 9 End
# Done

# Statement-Based Programming Problems

# Q79. Check Whether a Number Is Prime
n = int(input("Q79 N: "))
if n <= 1:
    print("Not Prime")
else:
    is_prime = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            is_prime = False
        i += 1
    if is_prime:
        print("Prime")
    else:
        print("Not Prime")

# Q80. Find the HCF (GCD) of Two Numbers
a = int(input("Q80 A: "))
b = int(input("Q80 B: "))
while b != 0:
    temp = b
    b = a % b
    a = temp
print(a)

# Q81. Find the LCM of Two Numbers
a = int(input("Q81 A: "))
b = int(input("Q81 B: "))
max_val = a
if b > a:
    max_val = b
while True:
    if max_val % a == 0 and max_val % b == 0:
        print(max_val)
        break
    max_val += 1

# Q82. Check Whether a Number Is Perfect
n = int(input("Q82 N: "))
if n <= 1:
    print("Not Perfect")
else:
    total = 0
    i = 1
    while i < n:
        if n % i == 0:
            total += i
        i += 1
    if total == n:
        print("Perfect")
    else:
        print("Not Perfect")

# Q83. Check Whether a Number Is a Strong Number
n = int(input("Q83 N: "))
orig = n
total_fact = 0
while n > 0:
    digit = n % 10
    if digit == 0 or digit == 1: fact = 1
    elif digit == 2: fact = 2
    elif digit == 3: fact = 6
    elif digit == 4: fact = 24
    elif digit == 5: fact = 120
    elif digit == 6: fact = 720
    elif digit == 7: fact = 5040
    elif digit == 8: fact = 40320
    elif digit == 9: fact = 362880
    total_fact += fact
    n = n // 10
if orig == total_fact:
    print("Strong")
else:
    print("Not Strong")

# Q84. Check Whether a Number Is an Armstrong Number
n = int(input("Q84 N: "))
orig = n
count = 0
temp = n
while temp > 0:
    count += 1
    temp = temp // 10

temp = n
arm_sum = 0
while temp > 0:
    digit = temp % 10
    arm_sum += digit ** count
    temp = temp // 10

if orig == arm_sum:
    print("Armstrong")
else:
    print("Not Armstrong")

# Q85. Convert a Decimal Number to Binary
n = int(input("Q85 N: "))
if n == 0:
    print(0)
else:
    binary = 0
    place = 1
    while n > 0:
        binary = binary + (n % 2) * place
        place *= 10
        n = n // 2
    print(binary)

# Q86. Find the Sum of a Number's Divisors
n = int(input("Q86 N: "))
i = 1
total = 0
while i <= n:
    if n % i == 0:
        total += i
    i += 1
print(total)

# Q87. Print a Number Triangle
n = int(input("Q87 N: "))
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1

# Q88. Print a Hollow Rectangle
r = int(input("Q88 R: "))
c = int(input("Q88 C: "))
i = 1
while i <= r:
    j = 1
    while j <= c:
        if i == 1 or i == r or j == 1 or j == c:
            print("*", end=" ")
        else:
            print(" ", end=" ")
        j += 1
    print()
    i += 1

# Q89. Print a Right-Aligned Triangle
n = int(input("Q89 N: "))
i = 1
while i <= n:
    j = 1
    while j <= n - i:
        print(" ", end=" ")
        j += 1
    k = 1
    while k <= i:
        print("*", end=" ")
        k += 1
    print()
    i += 1

# Q90. Print a Multiplication Grid
n = int(input("Q90 N: "))
i = 1
while i <= n:
    j = 1
    while j <= n:
        print(i * j, end=" ")
        j += 1
    print()
    i += 1

# Q91. Print the Fibonacci Series up to a Limit
n = int(input("Q91 N: "))
a = 0
b = 1
while a <= n:
    print(a, end=" ")
    temp = a + b
    a = b
    b = temp
print()

# Q92. Print All Prime Numbers up to N
n = int(input("Q92 N: "))
num = 2
while num <= n:
    is_prime = True
    i = 2
    while i * i <= num:
        if num % i == 0:
            is_prime = False
        i += 1
    if is_prime:
        print(num, end=" ")
    num += 1
print()

# Q93. Print All Armstrong Numbers up to N
n = int(input("Q93 N: "))
num = 0
while num <= n:
    temp = num
    count = 0
    if temp == 0:
        count = 1
    while temp > 0:
        count += 1
        temp = temp // 10
        
    temp = num
    arm_sum = 0
    while temp > 0:
        digit = temp % 10
        arm_sum += digit ** count
        temp = temp // 10
        
    if arm_sum == num:
        print(num, end=" ")
    num += 1
print()

# Q94. Print All Perfect Numbers up to N
n = int(input("Q94 N: "))
num = 1
while num <= n:
    total = 0
    i = 1
    while i < num:
        if num % i == 0:
            total += i
        i += 1
    if total == num:
        print(num, end=" ")
    num += 1
print()

# Q95. Find All Pairs Whose Sum Is N
n = int(input("Q95 N: "))
a = 1
while a < n:
    b = n - a
    if a < b:
        print(str(a) + " + " + str(b))
    a += 1

# Q96. Print All Two-Digit Numbers with a Given Digit Sum
s = int(input("Q96 S: "))
num = 10
while num <= 99:
    digit_sum = (num // 10) + (num % 10)
    if digit_sum == s:
        print(num, end=" ")
    num += 1
print()

# Q97. Find All Common Divisors of Two Numbers
a = int(input("Q97 A: "))
b = int(input("Q97 B: "))
i = 1
while i <= a and i <= b:
    if a % i == 0 and b % i == 0:
        print(i, end=" ")
    i += 1
print()

# Q98. Find Prime Factor Pairs
n = int(input("Q98 N: "))
a = 2
found = False
while a * a <= n:
    if n % a == 0:
        b = n // a
        
        is_prime_a = True
        i = 2
        while i * i <= a:
            if a % i == 0:
                is_prime_a = False
            i += 1
            
        is_prime_b = True
        j = 2
        while j * j <= b:
            if b % j == 0:
                is_prime_b = False
            j += 1
            
        if is_prime_a and is_prime_b:
            print(str(a) + " * " + str(b))
            found = True
    a += 1

if not found:
    print("No prime factor pair")
while reverse_start >= 0:
    print(reverse_start)
    reverse_start -= reverse_step
