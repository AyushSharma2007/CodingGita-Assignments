# Q36. Login with Role
login_input = input().split()
username = login_input[0]
password = login_input[1]

if username == "admin":
    if password == "admin123":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")


# Q37. Driving License Eligibility
license_input = input().split()
age = int(license_input[0])
test_status = license_input[1]

if age >= 18:
    if test_status == "pass":
        print("License Approved")
    else:
        print("Test Not Passed")
else:
    print("Age Not Eligible")


# Q38. ATM Withdrawal
atm_input = input().split()
balance = float(atm_input[0])
withdrawal = float(atm_input[1])

if withdrawal <= balance:
    if withdrawal % 100 == 0:
        print("Withdrawal Successful")
    else:
        print("Enter Amount in Multiples of 100")
else:
    print("Insufficient Balance")


# Q39. Exam Result with Attendance
exam_input = input().split()
attendance = float(exam_input[0])
marks = float(exam_input[1])

if attendance >= 75:
    if marks >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not Eligible Due to Attendance")


# Q40. Bank Account Verification
bank_input = input().split()
account_type = bank_input[0]
account_balance = float(bank_input[1])

if account_type == "savings":
    if account_balance >= 1000:
        print("Minimum Balance Maintained")
    else:
        print("Minimum Balance Not Maintained")
else:
    print("Unsupported Account")


# Q41. Online Shopping Eligibility
shopping_input = input().split()
order_amount = float(shopping_input[0])
payment_method = shopping_input[1]

if order_amount >= 500:
    if payment_method == "card":
        print("Card Payment Accepted")
    elif payment_method == "upi":
        print("UPI Payment Accepted")
    else:
        print("Unsupported Payment Method")
else:
    print("Minimum Order Amount Not Reached")


# Q42. Hostel Room Allocation
hostel_input = input().split()
year = int(hostel_input[0])
student_attendance = float(hostel_input[1])

if year in [2, 3, 4]:
    if student_attendance >= 75:
        print("Room Eligible")
    else:
        print("Attendance Too Low")
else:
    print("Not Eligible by Year")


# Q43. Internet Plan Upgrade
plan_input = input().split()
current_plan = plan_input[0]
monthly_usage = float(plan_input[1])

if current_plan == "basic":
    if monthly_usage > 100:
        print("Recommend Upgrade")
    else:
        print("Basic Plan Is Sufficient")
else:
    print("Already on Higher Plan")
