# LEVEL 4 - (Using fixed 20-iterations to avoid 'while' and string conversion)

# Q23
t23, c23 = 58321, 0
for _ in range(20):
    if t23 > 0: 
      c23 += 1 
      t23 //= 10
print(f"Q23: {c23}")

# Q24
t24, sum24 = 58321, 0
for _ in range(20):
    if t24 > 0: 
      sum24 += t24 % 10
      t24 //= 10
print(f"Q24: {sum24}")

# Q25
t25, prod25 = 234, 1
for _ in range(20):
    if t25 > 0: 
      prod25 *= (t25 % 10) 
      t25 //= 10
print(f"Q25: {prod25}")

# Q26
t26, ev26 = 58321, 0
for _ in range(20):
    if t26 > 0:
        if (t26 % 10) % 2 == 0: 
          ev26 += 1
        t26 //= 10
print(f"Q26: {ev26}")

# Q27
t27, sumev27 = 58321, 0
for _ in range(20):
    if t27 > 0:
        if (t27 % 10) % 2 == 0: 
          sumev27 += (t27 % 10)
        t27 //= 10
print(f"Q27: {sumev27}")

# Q28
t28, max28 = 58321, -1
for _ in range(20):
    if t28 > 0:
        d = t28 % 10
        if d > max28: 
          max28 = d
        t28 //= 10
print(f"Q28: {max28}")

# Q29
t29, min29 = 58321, 10
for _ in range(20):
    if t29 > 0:
        d = t29 % 10
        if d < min29: 
          min29 = d
        t29 //= 10
print(f"Q29: {min29}")

# Q30
t30, rev30 = 58321, 0
for _ in range(20):
    if t30 > 0: 
      rev30 = (rev30 * 10) + (t30 % 10) 
      t30 //= 10
print(f"Q30: {rev30}")

# Q31
orig31, t31, rev31 = 1221, 1221, 0
for _ in range(20):
    if t31 > 0: 
      rev31 = (rev31 * 10) + (t31 % 10) 
      t31 //= 10
print(f"Q31: {'Palindrome' if orig31 == rev31 else 'Not Palindrome'}")

# Q32
t32, targ32, c32 = 1223342, 2, 0
for _ in range(20):
    if t32 > 0:
        if t32 % 10 == targ32: 
          c32 += 1
        t32 //= 10
print(f"Q32: {c32}")

# Q33
t33, first33 = 58321, 0
for _ in range(20):
    if t33 > 0: 
      first33 = t33 % 10 
      t33 //= 10
print(f"Q33: {first33}")

# Q34
t34, max34, min34 = 58321, -1, 10
for _ in range(20):
    if t34 > 0:
        d = t34 % 10
        if d > max34: 
          max34 = d
        if d < min34: 
          min34 = d
        t34 //= 10
print(f"Q34: {max34 - min34}")

# Q35
t35, pos35 = 58321, 1
print("Q35:")
for _ in range(20):
    if t35 > 0:
        print(t35 % 10, pos35)
        t35 //= 10
        pos35 += 1

# Q36
orig36, t36, arm36 = 153, 153, 0
for _ in range(3):
    if t36 > 0: 
      arm36 += (t36 % 10)**3
      t36 //= 10
print(f"Q36: {'Armstrong' if orig36 == arm36 else 'Not Armstrong'}")
