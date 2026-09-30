
# ASSIGNMENT - 2 (COMPLETE SOLUTIONS)

print("--- TOPIC 1: TYPE CASTING ---")

# Q1
age = "25"
age_int = int(age)
print("Q1:", age_int, type(age_int))

# Q2
marks = "75.5"
marks_float = float(marks)
print("Q2:", marks_float, type(marks_float))

# Q3
number = 50
number_float = float(number)
print("Q3:", number_float, type(number_float))

# Q4
marks_q4 = 85.9
marks_int_q4 = int(marks_q4)
print("Q4:", marks_int_q4)

# Q5
roll_number = 101
roll_str = str(roll_number)
print("Q5:", roll_str, type(roll_str))

# Q6
v1 = int("18")
v2 = float("92.5")
v3 = str(100)
v4 = int(45.8)
print("Q6:", v1, type(v1), v2, type(v2), v3, type(v3), v4, type(v4))

# Q7
a = "20"
b = int(a)
c = 10.8
d = int(c)
e = 25
f = str(e)
print("Q7:")
print(b)
print(d)
print(f)
print(type(b))
print(type(d))
print(type(f))

# Q8 (Corrected)
age_q8 = "19"
new_age = int(age_q8) + 1
print("Q8 Age:", new_age)

# Q9
marks_q9 = "85"
final_marks = int(marks_q9) + 5
print("Q9 Final Marks:", final_marks)

# Q10
price_q10 = "1499.50"
total_amount_q10 = float(price_q10) + 99.50
print("Q10 Total Amount:", total_amount_q10)


print("\n--- TOPIC 2: ARITHMETIC OPERATORS ---")

# Q11
a11 = 20
b11 = 6
print("Q11 Addition:", a11 + b11)
print("Q11 Subtraction:", a11 - b11)
print("Q11 Multiplication:", a11 * b11)
print("Q11 Division:", a11 / b11)
print("Q11 Floor division:", a11 // b11)
print("Q11 Remainder:", a11 % b11)
print("Q11 Power:", a11 ** b11)

# Q12
a12 = 17
b12 = 5
print("Q12 / (Float Div):", a12 / b12)
print("Q12 // (Floor Div):", a12 // b12)
print("Q12 % (Remainder):", a12 % b12)

# Q13
res13 = 10 + 5 * 2
print("Q13 Default:", res13)
res13_forced = (10 + 5) * 2
print("Q13 Addition First:", res13_forced)

# Q14
res14 = 20 - 4 * 3 + 2
print("Q14 Default:", res14)
res14_paren = (20 - (4 * 3)) + 2
print("Q14 With Parentheses:", res14_paren)

# Q15
print("Q15 Power 1:", 2 ** 3)
print("Q15 Power 2:", 3 ** 2)
print("Q15 Power 3:", 10 ** 2)
side = 5
area_sq = side ** 2
print("Q15 Square Area:", area_sq)

# Q16
nb = 80
pen = 20
pencil = 10
print("Q16 Total Amount:", nb + pen + pencil)

# Q17
nb_cost = 3 * 50
pen_cost = 2 * 15
calc_cost = 1 * 500
total_bill_q17 = nb_cost + pen_cost + calc_cost
print("Q17 Notebook Cost:", nb_cost)
print("Q17 Pen Cost:", pen_cost)
print("Q17 Calculator Cost:", calc_cost)
print("Q17 Total Bill:", total_bill_q17)

# Q18
students = 47
print("Q18 Complete Groups:", students // 5)
print("Q18 Students Left:", students % 5)

# Q19
py_m = 85
ma_m = 78
ph_m = 92
total_m19 = py_m + ma_m + ph_m
avg_m19 = total_m19 / 3
print("Q19 Total Marks:", total_m19)
print("Q19 Average Marks:", avg_m19)

# Q20
eng = 78
math20 = 85
py20 = 92
phys20 = 81
chem20 = 74
tot20 = eng + math20 + py20 + phys20 + chem20
pct20 = (tot20 / 500) * 100
print("Q20 Total Marks:", tot20)
print("Q20 Percentage:", pct20)


print("\n--- TOPIC 3: DIGIT EXTRACTION ---")

# Q21
num21 = 583
print("Q21 Ones Digit:", num21 % 10)

# Q22
num22 = 583
print("Q22 Tens Digit:", (num22 // 10) % 10)

# Q23
num23 = 583
print("Q23 Hundreds Digit:", num23 // 100)

# Q24
num24 = 746
print("Q24 Ones Digit:", num24 % 10)
print("Q24 Tens Digit:", (num24 // 10) % 10)
print("Q24 Hundreds Digit:", num24 // 100)

# Q25
num25 = 5829
print("Q25 Ones Digit:", num25 % 10)
print("Q25 Tens Digit:", (num25 // 10) % 10)
print("Q25 Hundreds Digit:", (num25 // 100) % 10)
print("Q25 Thousands Digit:", num25 // 1000)

# Q26
num26 = 583
d_ones26 = num26 % 10
d_tens26 = (num26 // 10) % 10
d_hund26 = num26 // 100
print("Q26 Sum of Digits:", d_hund26 + d_tens26 + d_ones26)

# Q27
num27 = 4726
d_ones27 = num27 % 10
d_tens27 = (num27 // 10) % 10
d_hund27 = (num27 // 100) % 10
d_thou27 = num27 // 1000
print("Q27 Sum of Digits:", d_thou27 + d_hund27 + d_tens27 + d_ones27)

# Q28
num28 = 234
p_ones = num28 % 10
p_tens = (num28 // 10) % 10
p_hund = num28 // 100
print("Q28 Product of Digits:", p_hund * p_tens * p_ones)

# Q29
num29 = 583
r_ones29 = num29 % 10
r_tens29 = (num29 // 10) % 10
r_hund29 = num29 // 100
rev29 = (r_ones29 * 100) + (r_tens29 * 10) + r_hund29
print("Q29 Original Number:", num29)
print("Q29 Reversed Number:", rev29)

# Q30
num30 = 4726
r_ones30 = num30 % 10
r_tens30 = (num30 // 10) % 10
r_hund30 = (num30 // 100) % 10
r_thou30 = num30 // 1000
rev30 = (r_ones30 * 1000) + (r_tens30 * 100) + (r_hund30 * 10) + r_thou30
print("Q30 Original Number:", num30)
print("Q30 Reversed Number:", rev30)

# Q31
num31 = 5834
pl_ones = num31 % 10
pl_tens = (num31 // 10) % 10
pl_hund = (num31 // 100) % 10
pl_thou = num31 // 1000
print("Q31 Thousands Place:", pl_thou * 1000)
print("Q31 Hundreds Place:", pl_hund * 100)
print("Q31 Tens Place:", pl_tens * 10)
print("Q31 Ones Place:", pl_ones * 1)

# Q32
num32 = 583
diff_hund = num32 // 100
diff_ones = num32 % 10
print("Q32 Difference:", diff_hund - diff_ones)

# Q33 (Corrected)
num33 = 583
ones33 = num33 % 10
print("Q33 Ones Digit:", ones33)

# Q34
num34 = 9365
print("Q34 Thousands Digit:", num34 // 1000)
print("Q34 Hundreds Digit:", (num34 // 100) % 10)
print("Q34 Tens Digit:", (num34 // 10) % 10)
print("Q34 Ones Digit:", num34 % 10)

# Q35
hundreds35 = 5
tens35 = 8
ones35 = 3
built_num = (hundreds35 * 100) + (tens35 * 10) + ones35
print("Q35 Number:", built_num)


print("\n--- TOPIC 4: REAL-LIFE ARITHMETIC PROBLEMS ---")

# Q36
p36 = 10000
r36 = 5
t36 = 2
si = (p36 * r36 * t36) / 100
print("Q36 Simple Interest:", si)

# Q37
length = 15
width = 8
print("Q37 Area:", length * width)
print("Q37 Perimeter:", 2 * (length + width))

# Q38
pi = 3.14
rad = 7
print("Q38 Circle Area:", pi * (rad ** 2))

# Q39
celsius = 35
fahrenheit = (celsius * 9 / 5) + 32
print("Q39 Fahrenheit:", fahrenheit)

# Q40
tot_sec40 = 367
print("Q40 Minutes:", tot_sec40 // 60)
print("Q40 Seconds:", tot_sec40 % 60)

# Q41
tot_sec41 = 7384
hrs41 = tot_sec41 // 3600
rem_sec41 = tot_sec41 % 3600
mins41 = rem_sec41 // 60
secs41 = rem_sec41 % 60
print("Q41 Hours:", hrs41)
print("Q41 Minutes:", mins41)
print("Q41 Seconds:", secs41)

# Q42
basic_sal = 25000
hra = 5000
travel_al = 2500
tax_ded = 3000
gross = basic_sal + hra + travel_al
net = gross - tax_ded
print("Q42 Gross Salary:", gross)
print("Q42 Net Salary:", net)

# Q43
dist = 120
mileage = 20
fuel_price = 100
fuel_req = dist / mileage
tot_fuel_cost = fuel_req * fuel_price
print("Q43 Fuel required:", fuel_req)
print("Q43 Total fuel cost:", tot_fuel_cost)

# Q44
price44 = float("2500")
disc44 = float("10")
disc_amt44 = (price44 * disc44) / 100
final_p44 = price44 - disc_amt44
print("Q44 Discount amount:", disc_amt44)
print("Q44 Final price:", final_p44)


print("\n--- TOPIC 5: TYPE CASTING + ARITHMETIC OPERATORS ---")

# Q45
p45 = int("1200")
q45 = int("4")
print("Q45 Price:", p45)
print("Q45 Quantity:", q45)
print("Q45 Total Price:", p45 * q45)

# Q46
py_m46 = int("85")
ma_m46 = int("78")
ph_m46 = int("91")
tot46 = py_m46 + ma_m46 + ph_m46
print("Q46 Total marks:", tot46)
print("Q46 Average marks:", tot46 / 3)

# Q47
price47 = float("1500")
qty47 = int("2")
tax_rt47 = float("5")
subtot47 = price47 * qty47
tax_amt47 = (subtot47 * tax_rt47) / 100
print("Q47 Subtotal:", subtot47)
print("Q47 Tax amount:", tax_amt47)
print("Q47 Final bill:", subtot47 + tax_amt47)

# Q48
cost48 = 2000
d_rate48 = 15
gst_rate48 = 18
disc_amt48 = (cost48 * d_rate48) / 100
price_disc48 = cost48 - disc_amt48
gst_amt48 = (price_disc48 * gst_rate48) / 100
final_p48 = price_disc48 + gst_amt48
print("Q48 Discount amount:", disc_amt48)
print("Q48 Price after discount:", price_disc48)
print("Q48 GST amount:", gst_amt48)
print("Q48 Final price:", final_p48)

# Q49 (Corrected)
price49 = "500"
quantity49 = 3
total49 = int(price49) * quantity49
print("Q49 Total:", total49)

# Q50 (Corrected)
m1_50 = "80"
m2_50 = "75"
m3_50 = "90"
tot50 = int(m1_50) + int(m2_50) + int(m3_50)
print("Q50 Total Marks:", tot50)


print("\n--- TOPIC 6: OUTPUT PREDICTION AND CONCEPTUAL PRACTICE ---")

# Q51
a51 = "50"
b51 = int(a51)
print("Q51:")
print(a51)
print(b51)
print(type(a51))
print(type(b51))

# Q52
num52 = 99.99
res52 = int(num52)
print("Q52:", num52)
print("Q52:", res52)  # Decimal part truncated

# Q53
a53 = 12
b53 = 5
print("Q53 + :", a53 + b53)
print("Q53 - :", a53 - b53)
print("Q53 * :", a53 * b53)
print("Q53 / :", a53 / b53)
print("Q53 //:", a53 // b53)
print("Q53 % :", a53 % b53)

# Q54
print("Q54 (10 + 5 * 2)   =", 10 + 5 * 2)
print("Q54 ((10 + 5) * 2) =", (10 + 5) * 2)
print("Q54 (20 / 5 + 3)   =", 20 / 5 + 3)
print("Q54 (20 / (5 + 3)) =", 20 / (5 + 3))

# Q55
num55 = 684
a55 = num55 % 10       # ones digit
b55 = num55 // 10
c55 = b55 % 10         # tens digit
d55 = num55 // 100     # hundreds digit
print("Q55 Ones (a):", a55)
print("Q55 Tens (c):", c55)
print("Q55 Hundreds (d):", d55)


print("\n--- TOPIC 7: MIXED DEBUGGING & FINAL CHALLENGE ---")

# Q56 (Corrected)
student_name56 = "Ravi"
marks56 = "85"
total56 = int(marks56) + 5
print("Q56 Student:", student_name56)
print("Q56 Marks:", total56)
print("Q56 Type:", type(total56))

# Q57 (Corrected)
num57 = 746
ones57 = num57 % 10
tens57 = (num57 // 10) % 10
hundreds57 = num57 // 100
print("Q57 Ones:", ones57)
print("Q57 Tens:", tens57)
print("Q57 Hundreds:", hundreds57)

# Q58 (Corrected)
price58 = "2000"
discount58 = "15"
p58 = float(price58)
d58 = float(discount58)
disc_amt58 = p58 * d58 / 100
final_p58 = p58 - disc_amt58
print("Q58 Discount:", disc_amt58)
print("Q58 Final Price:", final_p58)

# Q59 (Corrected)
student_name59 = "Rahul"
m1_59 = "85"
m2_59 = "90"
m3_59 = "78"
tot59 = int(m1_59) + int(m2_59) + int(m3_59)
avg59 = tot59 / 3
print("Q59 Student:", student_name59)
print("Q59 Total Marks:", tot59)
print("Q59 Average:", avg59)
print("Q59 Marks Type:", type(tot59))

# Q60 Final Challenge
# Part A
num60 = 5836
ones60 = num60 % 10
tens60 = (num60 // 10) % 10
hund60 = (num60 // 100) % 10
thou60 = num60 // 1000
sum60 = thou60 + hund60 + tens60 + ones60
rev60 = (ones60 * 1000) + (tens60 * 100) + (hund60 * 10) + thou60

print("\nQ60 Part A:")
print("Thousands digit:", thou60)
print("Hundreds digit:", hund60)
print("Tens digit:", tens60)
print("Ones digit:", ones60)
print("Sum of digits:", sum60)
print("Reversed number:", rev60)

# Part B
p_str = "1250"
q_str = "4"
d_str = "10"
p60 = float(p_str)
q60 = int(q_str)
d60 = float(d_str)

subtotal60 = p60 * q60
disc_amt60 = (subtotal60 * d60) / 100
final_amt60 = subtotal60 - disc_amt60

print("\nQ60 Part B:")
print("Subtotal:", subtotal60)
print("Discount amount:", disc_amt60)
print("Final amount:", final_amt60)
