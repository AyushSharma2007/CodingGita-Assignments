# LEVEL 6
# Q45
s45 = "abcde"
mid45 = len(s45) // 2
print("Q45:")for i in range(len(s45)):
  if i == mid45:
    print(s45[i]) 
  

# Q46
s46 = "PythonCode"
mid46, h1_46, h2_46 = len(s46) // 2, "", ""
for i in range(len(s46)):
    if i < mid46:
      h1_46 += s46[i]
    else: 
      h2_46 += s46[i]
print(f"Q46:\nFirst Half: {h1_46}\nSecond Half: {h2_46}")

# Q47
s47 = "PROGRAM"
n47, mid47, h1_47, m_47, h2_47 = len(s47), len(s47) // 2, "", "", ""
for i in range(n47):
    if n47 % 2 != 0 and i == mid47: 
      m_47 = s47[i]
    elif i < mid47: 
      h1_47 += s47[i]
    else: 
      h2_47 += s47[i]
print(f"Q47:\nFirst Half: {h1_47}")
if m_47: 
  print(f"Middle: {m_47}")
print(f"Second Half: {h2_47}")

# Q48
s48, is_eq48 = "ABCABC", True
mid48 = len(s48) // 2
for i in range(mid48):
    if s48[i] != s48[mid48 + i]: 
      is_eq48 = False
print(f"Q48: {'Equal Halves' if is_eq48 else 'Different Halves'}")

# Q49
s49, is_sym49, n49 = "ABCCBA", True, len("ABCCBA")
for i in range(n49 // 2):
    if s49[i] != s49[n49 - 1 - i]: 
      is_sym49 = False
print(f"Q49: {'Symmetric' if is_sym49 else 'Not Symmetric'}")

# Q50
s50, res50 = "ABCDEFGH", ""
for i in range(len(s50)):
    if i % 2 == 0: 
      res50 += s50[i]
print(f"Q50: {res50}")

# Q51
s51, e51, o51 = "Python", 0, 0
for i in range(len(s51)):
    if i % 2 == 0: 
      e51 += 1
    else: 
      o51 += 1
print(f"Q51: Even Index = {e51}, Odd Index = {o51}")

# Q52
s52, res52 = "ABCDEFGH", ""
for i in range(len(s52)):
    if i % 2 == 0: 
      res52 += s52[i+1]
    else: 
      res52 += s52[i-1]
print(f"Q52: {res52}")
