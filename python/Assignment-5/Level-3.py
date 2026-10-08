# LEVEL 3
# Q15
fact15 = 1
for i in range(1, 6): 
  fact15 *= i
print(f"Q15: {fact15}")

# Q16
fact16 = 1
print("Q16:")
for i in range(1, 6):
    fact16 *= i
print(f"{i}! = {fact16}")

# Q17
prod17 = 1
for i in range(2, 11, 2): 
  prod17 *= i
print(f"Q17: {prod17}")

# Q18
prod18 = 1
for i in range(1, 8, 2): 
  prod18 *= i
print(f"Q18: {prod18}")

# Q19
prod19 = 1
for i in range(8, 1, -2): 
  prod19 *= i
print(f"Q19: {prod19}")

# Q20
sum20 = 0
for i in range(1, 6): 
  sum20 += i**2
print(f"Q20: {sum20}")

# Q21
sum21 = 0
for i in range(1, 5): 
  sum21 += i**3
print(f"Q21: {sum21}")

# Q22
f22, sum22 = 1, 0
for i in range(1, 5):
    f22 *= i
    sum22 += f22
print(f"Q22: {sum22}")
