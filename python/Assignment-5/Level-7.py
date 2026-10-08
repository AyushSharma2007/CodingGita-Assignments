# LEVEL 7
# Q53 Second largest digit
t53, m1_53, m2_53 = 58321, -1, -1
for _ in range(20):
    if t53 > 0:
        d = t53 % 10
        if d > m1_53: 
          m2_53 = m1_53; m1_53 = d
        elif d > m2_53 and d != m1_53: 
          m2_53 = d
        t53 //= 10
print(f"Q53: {m2_53}")

# Q54 Longest Consecutive
best54, cur54, last54 = 0, 0, ""
for ch in "aaabbccccd":
    if ch == last54: 
      cur54 += 1
    else: 
      cur54 = 1
    if cur54 > best54: 
      best54 = cur54
    last54 = ch
print(f"Q54: {best54}")

# Q55
s55, t55, c55, l55 = "banana", "a", 0, 0
for ch in s55:
    l55 += 1
    if ch == t55: 
      c55 += 1
print(f"Q55: Count = {c55}, Frequency = {(c55/l55)*100}%")

# Q56
t56, run56 = 58321, 0
print("Q56:")
for _ in range(20):
    if t56 > 0: 
      run56 += t56 % 10
    print(run56)
    t56 //= 10

# Q57
t57, ev57, od57 = 24681, 0, 0
for _ in range(20):
    if t57 > 0:
        if (t57 % 10) % 2 == 0: 
          ev57 += 1
        else: 
          od57 += 1
        t57 //= 10
print(f"Q57: {'More Even' if ev57 > od57 else 'More Odd' if od57 > ev57 else 'Equal'}")

# Q58 Alternating Digit Sum
t58, tot58, sign58 = 12345, 0, 1
for _ in range(20):
    if t58 > 0:
        tot58 += (t58 % 10) * sign58
        sign58 *= -1
        t58 //= 10
print(f"Q58: {tot58}")

# Q59 (Prediction output)
print("Q59:\n2\n6\n12\n20\n30")

# Q60 (Prediction output)
print("Q60:\n5")

# Q61 (Debugged accumulator)
sum61 = 0
for i in range(1, 6): 
  sum61 += i
print(f"Q61: {sum61}")
