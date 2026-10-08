# LEVEL 2

# Q7
sum7 = 0
for i in range(5, 11): 
  sum7 += i
print(f"Q7: {sum7}")

# Q8
c8 = 0
for i in range(1, 11):
    if i % 3 == 0: 
      c8 += 1
print(f"Q8: {c8}")

# Q9
sum9 = 0
for i in range(1, 21):
    if i % 4 == 0: 
      sum9 += i
print(f"Q9: {sum9}")

# Q10
c10 = 0
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0: 
      c10 += 1
print(f"Q10: {c10}")

# Q11
sum11 = 0
for i in range(1, 11):
    if i % 3 != 0: 
      sum11 += i
print(f"Q11: {sum11}")

# Q12
e12, o12 = 0, 0
for i in range(1, 11):
    if i % 2 == 0: 
      e12 += 1
    else: 
      o12 += 1
print(f"Q12: Even = {e12}, Odd = {o12}")

# Q13
run13 = 0
print("Q13:")
for i in range(1, 6):
    run13 += i; 
    print(run13)

# Q14
run14 = 1
print("Q14:")
for i in range(1, 6):
    run14 *= i 
    print(run14)
