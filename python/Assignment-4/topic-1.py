# Q1. Positive Number
number1 = int(input())
if number1 > 0:
    print("Positive Number")

# Q2. Voting Eligibility Check
age = int(input())
if age >= 18:
    print("Eligible to Vote")

# Q3. Temperature Warning
temperature = float(input())
if temperature > 40:
    print("High Temperature")

# Q4. Divisible by 5
number4 = int(input())
if number4 % 5 == 0:
    print("Divisible by 5")

# Q5. Free Delivery
order_amount = float(input())
if order_amount >= 1000:
    print("Free Delivery")

# Q6. Character Check
char = input()
if char == "A":
    print("You entered A")

# Q7. Password Length Check
password = input()
if len(password) >= 8:
    print("Strong Length")

# Q8. Number of Digits
number8 = int(input())
if 100 <= number8 <= 999:
    print("Three Digit Number")
