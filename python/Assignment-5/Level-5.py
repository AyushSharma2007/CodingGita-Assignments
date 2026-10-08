# LEVEL 5
# Q37
s37 = "Python"
print("Q37:") 
for i in range(len(s37)):
  print(i, s37[i])

# Q38
s38, c38 = "Hello World", 0
for _ in s38: 
  c38 += 1
print(f"Q38: {c38}")

# Q39
s39, v39, c39 = "Hello World", 0, 0
for ch in s39:
    if ch in "aeiouAEIOU": 
      v39 += 1
    elif (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'): 
      c39 += 1
print(f"Q39: Vowels = {v39}, Consonants = {c39}")

# Q40
s40, freq40 = "banana", 0
for ch in s40:
    if ch == "a": 
      freq40 += 1
print(f"Q40: {freq40}")

# Q41
s41, pos41 = "programming", -1
for i in range(len(s41)):
    if s41[i] == "g" and pos41 == -1: 
      pos41 = i
print(f"Q41: {pos41}")

# Q42
s42, up42, low42 = "PyThOn", 0, 0
for ch in s42:
    if ch >= 'A' and ch <= 'Z': 
      up42 += 1
    elif ch >= 'a' and ch <= 'z': 
      low42 += 1
print(f"Q42: Uppercase = {up42}, Lowercase = {low42}")

# Q43
print("Q43:") 
for ch in "ABC":
  print(ch, ord(ch)) 
  
# Q44
s44, res44 = "education", ""
for ch in s44:
    if ch not in "aeiouAEIOU": 
      res44 += ch
print(f"Q44: {res44}")
