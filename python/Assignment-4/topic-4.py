# Q29. College Admission Eligibility
admission_input = input().split()
marks = float(admission_input[0])
attendance = float(admission_input[1])

if marks >= 60 and attendance >= 75:
    print("Eligible")
else:
    print("Not Eligible")

# Q30. Scholarship Eligibility
scholarship_input = input().split()
marks_scholarship = float(scholarship_input[0])
income = float(scholarship_input[1])

if marks_scholarship >= 85 or income < 300000:
    print("Scholarship Available")
else:
    print("No Scholarship")

# Q31. Weekend Check
day = input().strip()
if day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Weekday")

# Q32. Online Exam Access
login_input = input().split()
username = login_input[0]
password = login_input[1]

if username == "student" and password == "python123":
    print("Access Granted")
else:
    print("Access Denied")

# Q33. Delivery Availability
city = input().strip()
if city == "Ahmedabad" or city == "Gandhinagar":
    print("Delivery Available")
else:
    print("Delivery Unavailable")

# Q34. Number Range Check
number = int(input())
if 10 <= number <= 50:
    print("Inside Range")
else:
    print("Outside Range")

# Q35. Secure Transaction
transaction_input = input().split()
amount = float(transaction_input[0])
otp = transaction_input[1]

if amount <= 50000 and otp == "1234":
    print("Transaction Approved")
else:
    print("Transaction Declined")
