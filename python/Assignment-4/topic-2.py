# Q9. Even or Odd
number9 = int(input())
if number9 % 2 == 0:
    print("Even")
else:
    print("Odd")

# Q10. Pass or Fail
marks = float(input())
if marks >= 40:
    print("Pass")
else:
    print("Fail")

# Q11. Adult or Minor
age11 = int(input())
if age11 >= 18:
    print("Adult")
else:
    print("Minor")

# Q12. Number Sign
number12 = int(input())
if number12 > 0:
    print("Positive")
else:
    print("Non-Positive")

# Q13. Divisible by 3
number13 = int(input())
if number13 % 3 == 0:
    print("Divisible by 3")
else:
    print("Not Divisible by 3")

# Q14. Login Password
correct_password = "python123"
password14 = input()
if password14 == correct_password:
    print("Login Successful")
else:
    print("Invalid Password")

# Q15. Username Check
username = input()
if username == "admin":
    print("Welcome Admin")
else:
    print("Invalid Username")

# Q16. Greater Between Two Numbers
num1, num2 = map(int, input().split())
if num1 > num2:
    print(num1)
elif num2 > num1:
    print(num2)
else:
    print("Both are Equal")

# Q17. Hot or Comfortable
temp17 = float(input())
if temp17 > 30:
    print("Hot")
else:
    print("Comfortable")

# Q18. Shopping Discount Eligibility
amount18 = float(input())
if amount18 >= 5000:
    print("Discount Available")
else:
    print("No Discount")
