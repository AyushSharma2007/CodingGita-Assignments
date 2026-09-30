# Q58. Student ID Validation
student_id = input()
parts = student_id.split("-")
if len(parts) >= 3 and parts[2] == "CSE":
    print("CSE Student")
else:
    print("Non-CSE Student")

# Q59. Email Domain Checker
email = input()
email_parts = email.split("@")
if len(email_parts) == 2 and email_parts[1] == "gmail.com":
    print("Gmail User")
else:
    print("Other Email Provider")

# Q60. Username Generator Validation
full_name = input().split()
if len(full_name) >= 2:
    username = full_name[0] + "." + full_name[-1]
    if "." in username:
        print("Valid Username Format")
    else:
        print("Invalid Username Format")
else:
    print("Invalid Username Format")

# Q61. Number Digit Analyzer
num_str = input().strip()
length = len(num_str)
if length == 1:
    print("One Digit")
elif length == 2:
    print("Two Digits")
elif length == 3:
    print("Three Digits")
else:
    print("Four or More Digits")

# Q62. Shopping Bill Category
bill_input = input().split()
price = float(bill_input[0])
quantity = int(bill_input[1])
subtotal = price * quantity

if subtotal >= 5000:
    discount_pct = 20
elif subtotal >= 2000:
    discount_pct = 10
else:
    discount_pct = 0

discount_amount = (discount_pct / 100) * subtotal
final_amount = subtotal - discount_amount
print(f"Subtotal: {int(subtotal)}, Discount: {discount_pct}%, Final: {final_amount:.2f}")

# Q63. Electricity Bill Category
units = int(input())
if units <= 100:
    rate = 5
elif units <= 300:
    rate = 7
else:
    rate = 10

bill = units * rate
print(f"Rate: ₹{rate}, Bill: ₹{bill}")

# Q64. ATM Menu
print("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
choice_input = input().split()
choice = int(choice_input[0])
balance = 10000

match choice:
    case 1:
        print(f"Balance: {balance}")
    case 2:
        deposit_amt = int(choice_input[1])
        balance += deposit_amt
        print(f"Deposit Successful, Balance: {balance}")
    case 3:
        withdraw_amt = int(choice_input[1])
        if withdraw_amt <= balance:
            balance -= withdraw_amt
            print(f"Withdrawal Successful, Balance: {balance}")
        else:
            print("Insufficient Balance")
    case 4:
        pass
    case _:
        print("Invalid Choice")

# Q65. Restaurant Ordering System
order_input = input().split()
item = int(order_input[0])
qty = int(order_input[1])

price_item = 0
match item:
    case 1:
        price_item = 250
    case 2:
        price_item = 150
    case 3:
        price_item = 200
    case 4:
        price_item = 120

total_cost = price_item * qty
if total_cost >= 500:
    discount_val = total_cost * 0.10
else:
    discount_val = 0.0

final_cost = total_cost - discount_val
print(f"Total: {total_cost}, Discount: {discount_val:.2f}, Final: {final_cost:.2f}")

# Q66. Exam Result Analyzer
exam_result = input().split()
m1 = float(exam_result[0])
m2 = float(exam_result[1])
m3 = float(exam_result[2])
attendance_pct = float(exam_result[3])

if attendance_pct >= 75:
    avg_marks = (m1 + m2 + m3) / 3
    if avg_marks >= 90:
        print("Outstanding")
    elif avg_marks >= 75:
        print("Very Good")
    elif avg_marks >= 60:
        print("Good")
    elif avg_marks >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not Eligible")

# Q67. Cab Fare Calculator
cab_input = input().split()
distance_km = float(cab_input[0])
ride_type = cab_input[1]

rate_per_km = 0
match ride_type:
    case "normal":
        rate_per_km = 15
    case "premium":
        rate_per_km = 25

base_fare = distance_km * rate_per_km
if distance_km > 20:
    surcharge = base_fare * 0.10
else:
    surcharge = 0

final_fare = base_fare + surcharge
print(f"Fare: {final_fare:.2f}")

# Q68. College Admission System
admission_in = input().split()
score = float(admission_in[0])
percentage = float(admission_in[1])
category = admission_in[2]

is_eligible = False
match category:
    case "general":
        if score >= 80 and percentage >= 75:
            is_eligible = True
    case "obc":
        if score >= 70 and percentage >= 70:
            is_eligible = True
    case "sc":
        if score >= 60 and percentage >= 60:
            is_eligible = True

if is_eligible:
    print("Admission Eligible")
else:
    print("Admission Not Eligible")
