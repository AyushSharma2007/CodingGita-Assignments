# Q19. Grade Calculator
marks19 = float(input())
if marks19 >= 90:
    print("A")
elif marks19 >= 80:
    print("B")
elif marks19 >= 70:
    print("C")
elif marks19 >= 60:
    print("D")
else:
    print("F")

# Q20. Temperature Category
temp20 = float(input())
if temp20 >= 40:
    print("Very Hot")
elif temp20 >= 30:
    print("Hot")
elif temp20 >= 20:
    print("Warm")
else:
    print("Cold")

# Q21. Traffic Signal
signal = input().strip().lower()
if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Wait")
elif signal == "green":
    print("Go")
else:
    print("Invalid Signal")

# Q22. Electricity Usage Category
units22 = float(input())
if units22 <= 100:
    print("Low Usage")
elif units22 <= 300:
    print("Medium Usage")
elif units22 <= 500:
    print("High Usage")
else:
    print("Very High Usage")

# Q23. Movie Ticket Category
age23 = int(input())
if age23 < 5:
    print("Free Ticket")
elif age23 <= 12:
    print("Child Ticket")
elif age23 <= 59:
    print("Regular Ticket")
else:
    print("Senior Ticket")

# Q24. BMI Category
bmi = float(input())
if bmi < 18.5:
    print("Underweight")
elif bmi < 25.0:
    print("Normal")
elif bmi < 30.0:
    print("Overweight")
else:
    print("Obese")

# Q25. Month Days
month25 = int(input())
if month25 in [1, 3, 5, 7, 8, 10, 12]:
    print("31 Days")
elif month25 in [4, 6, 9, 11]:
    print("30 Days")
elif month25 == 2:
    print("28 or 29 Days")
else:
    print("Invalid Month")

# Q26. Simple Calculator
calc_input = input().split()
num1 = int(calc_input[0])
num2 = int(calc_input[1])
operator = calc_input[2]

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Invalid Operator")

# Q27. Day Number
day27 = int(input())
if day27 == 1:
    print("Monday")
elif day27 == 2:
    print("Tuesday")
elif day27 == 3:
    print("Wednesday")
elif day27 == 4:
    print("Thursday")
elif day27 == 5:
    print("Friday")
elif day27 == 6:
    print("Saturday")
elif day27 == 7:
    print("Sunday")
else:
    print("Invalid Day")

# Q28. Performance Level
score28 = float(input())
if score28 >= 90:
    print("Excellent")
elif score28 >= 75:
    print("Very Good")
elif score28 >= 60:
    print("Good")
elif score28 >= 40:
    print("Average")
else:
    print("Needs Improvement")
