# LEVEL 9
# Q68 Number Profile
t68, d68, sum68, max68, min68, ev68, od68 = 58321, 0, 0, -1, 10, 0, 0
for _ in range(20):
    if t68 > 0:
        d = t68 % 10
        d68 += 1
        sum68 += d
        if d > max68: 
          max68 = d
        if d < min68: 
          min68 = d
        if d % 2 == 0: 
          ev68 += 1
        else: 
          od68 += 1
        t68 //= 10
print(f"Q68:\nDigits: {d68}\nSum: {sum68}\nLargest: {max68}\nSmallest: {min68}\nEven Digits: {ev68}\nOdd Digits: {od68}")

# Q69 String Balance Challenge
s69, tot69, v69, c69, up69, low69, eidx69 = "Hello World", 0, 0, 0, 0, 0, 0
for ch in s69:
    if tot69 % 2 == 0: 
      eidx69 += 1
    tot69 += 1
    if ch != " ":
        if ch in "aeiouAEIOU": 
          v69 += 1
        elif (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'): 
          c69 += 1
        
        if ch >= 'A' and ch <= 'Z': 
          up69 += 1
        if ch >= 'a' and ch <= 'z': 
          low69 += 1
        
print(f"Q69:\nTotal Characters: {tot69}\nVowels: {v69}\nConsonants: {c69}\nUppercase: {up69}\nLowercase: {low69}\nEven Index Characters: {eidx69}")
