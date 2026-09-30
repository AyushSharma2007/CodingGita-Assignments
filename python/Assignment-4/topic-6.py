# Q44. Greatest of Three Numbers
nums_input = input().split()
a = int(nums_input[0])
b = int(nums_input[1])
c = int(nums_input[2])

if a == b == c:
    print("All are Equal")
elif a == b and a > c:
    print("A and B are Equal and Greatest")
elif a == c and a > b:
    print("A and C are Equal and Greatest")
elif b == c and b > a:
    print("B and C are Equal and Greatest")
elif a > b and a > c:
    print("A is Greatest")
elif b > a and b > c:
    print("B is Greatest")
else:
    print("C is Greatest")


# Q45. Student Result with Grade
student_input = input().split()
marks45 = float(student_input[0])
attendance45 = float(student_input[1])

if attendance45 >= 75:
    if marks45 >= 90:
        print("Grade A")
    elif marks45 >= 75:
        print("Grade B")
    elif marks45 >= 60:
        print("Grade C")
    elif marks45 >= 40:
        print("Grade D")
    else:
        print("Grade F")
else:
    print("Not Eligible")


# Q46. Employee Bonus
bonus_input = input().split()
salary = float(bonus_input[0])
rating = int(bonus_input[1])

if salary >= 30000:
    if rating == 5:
        print("Bonus: 20%")
    elif rating == 4:
        print("Bonus: 15%")
    elif rating == 3:
        print("Bonus: 10%")
    else:
        print("Bonus: 5%")
else:
    print("Not Eligible for Bonus")


# Q47. Bus Ticket Category
bus_input = input().split()
age47 = int(bus_input[0])
distance = float(bus_input[1])

if age47 < 5:
    print("Free")
elif age47 <= 59:
    if distance <= 10:
        print("Regular - Short Distance")
    else:
        print("Regular - Long Distance")
else:
    print("Senior")


# Q48. Product Purchase Validation
product_input = input().split()
stock = int(product_input[0])
payment_status = product_input[1]

if stock > 0:
    if payment_status == "paid":
        print("Order Confirmed")
    elif payment_status == "pending":
        print("Payment Pending")
    else:
        print("Invalid Payment Status")
else:
    print("Out of Stock")


# Q49. Travel Ticket Validation
travel_input = input().split()
age49 = int(travel_input[0])
ticket_type = travel_input[1]

if age49 < 5:
    print("Free Travel")
elif age49 <= 59:
    if ticket_type == "AC":
        print("AC Ticket")
    elif ticket_type == "Sleeper":
        print("Sleeper Ticket")
    else:
        print("Invalid Ticket Type")
else:
    print("Senior Passenger")
