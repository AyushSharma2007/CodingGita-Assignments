# Q1. Solid Square
size = int(input("Q1 size: "))
for i in range(size):
    for j in range(size):
        print("*", end="")
    print()

# Q2. Solid Rectangle
r = int(input("Q2 rows: "))
c = int(input("Q2 cols: "))
for i in range(r):
    for j in range(c):
        print("*", end="")
    print()

# Q3. Increasing Star Triangle
size = int(input("Q3 size: "))
for i in range(1, size + 1):
    for j in range(i):
        print("*", end="")
    print()

# Q4. Increasing Number Triangle
size = int(input("Q4 size: "))
for i in range(1, size + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Q5. Repeated Number Triangle
size = int(input("Q5 size: "))
for i in range(1, size + 1):
    for j in range(i):
        print(i, end="")
    print()

# Q6. Repeated Alphabet Triangle
size = int(input("Q6 size: "))
for i in range(1, size + 1):
    for j in range(i):
        print(chr(64 + i), end="")
    print()

# Q7. Alphabet Triangle
size = int(input("Q7 size: "))
for i in range(1, size + 1):
    for j in range(1, i + 1):
        print(chr(64 + j), end="")
    print()

# Q8. Continuous Number Triangle
size = int(input("Q8 size: "))
num = 1
for i in range(1, size + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# Q9. Alternating 0-1 Triangle
size = int(input("Q9 size: "))
for i in range(1, size + 1):
    for j in range(1, i + 1):
        if (i + j) % 2 == 0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()

# Q10. Decreasing Star Triangle
size = int(input("Q10 size: "))
for i in range(size, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# Q11. Decreasing Number Triangle
size = int(input("Q11 size: "))
for i in range(size, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Q12. Decreasing Alphabet Triangle
size = int(input("Q12 size: "))
for i in range(size, 0, -1):
    for j in range(1, i + 1):
        print(chr(64 + j), end="")
    print()

# Q13. Right-Aligned Half Pyramid
size = int(input("Q13 size: "))
for i in range(1, size + 1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()

# Q14. Inverted Right-Aligned Half Pyramid
size = int(input("Q14 size: "))
for i in range(size, 0, -1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()

# Q15. Star Pyramid
size = int(input("Q15 size: "))
for i in range(1, size + 1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# Q16. Inverted Star Pyramid
size = int(input("Q16 size: "))
for i in range(size, 0, -1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# Q17. Solid Diamond
size = int(input("Q17 size: "))
for i in range(1, size + 1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()
for i in range(size - 1, 0, -1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# Q18. Rhombus
size = int(input("Q18 size: "))
for i in range(1, size + 1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(size):
        print("*", end="")
    print()

# Q19. Mirrored Number Pattern
size = int(input("Q19 size: "))
for i in range(1, size + 1):
    for j in range(1, i + 1):
        print(j, end="")
    for k in range(2 * (size - i)):
        print(" ", end="")
    for j in range(i, 0, -1):
        print(j, end="")
    print()

# Q20. Centered Number Pyramid
size = int(input("Q20 size: "))
for i in range(1, size + 1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(1, i + 1):
        print(k, end=" ")
    print()

# Q21. Palindromic Number Pyramid
size = int(input("Q21 size: "))
for i in range(1, size + 1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(1, i + 1):
        print(k, end="")
    for k in range(i - 1, 0, -1):
        print(k, end="")
    print()

# Q22. Alphabet Palindrome Pyramid
size = int(input("Q22 size: "))
for i in range(1, size + 1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(1, i + 1):
        print(chr(64 + k), end="")
    for k in range(i - 1, 0, -1):
        print(chr(64 + k), end="")
    print()

# Q23. Reverse-Starting Alphabet Triangle
size = int(input("Q23 size: "))
for i in range(1, size + 1):
    start = size - i + 1
    for j in range(i):
        print(chr(64 + start + j), end=" ")
    print()

# Q24. Increasing and Decreasing Star Triangle
size = int(input("Q24 size: "))
for i in range(1, size + 1):
    for j in range(i):
        print("*", end="")
    print()
for i in range(size - 1, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# Q25. Number Hourglass
size = int(input("Q25 size: "))
for i in range(size, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
for i in range(2, size + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Q26. Alphabet Hourglass
size = int(input("Q26 size: "))
for i in range(size, 0, -1):
    for j in range(1, i + 1):
        print(chr(64 + j), end="")
    print()
for i in range(2, size + 1):
    for j in range(1, i + 1):
        print(chr(64 + j), end="")
    print()

# Q27. Alternating Star and Hash Grid
size = int(input("Q27 size: "))
for i in range(1, size + 1):
    for j in range(1, size + 1):
        if (i + j) % 2 == 0:
            print("*", end="")
        else:
            print("#", end="")
    print()

# Q28. Binary Checkerboard
size = int(input("Q28 size: "))
for i in range(1, size + 1):
    for j in range(1, size + 1):
        if (i + j) % 2 == 0:
            print("1", end="")
        else:
            print("0", end="")
    print()

# Q29. Multiplication Grid
size = int(input("Q29 size: "))
for i in range(1, size + 1):
    for j in range(1, size + 1):
        print(i * j, end=" ")
    print()

# Q30. Alternating-Direction Rows
size = int(input("Q30 size: "))
for i in range(1, size + 1):
    if i % 2 != 0:
        for j in range(1, i + 1):
            print(j, end="")
    else:
        for j in range(i, 0, -1):
            print(j, end="")
    print()

# Q31. Number Diamond
size = int(input("Q31 size (half): "))
for i in range(1, size + 1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(1, i + 1):
        print(k, end="")
    for k in range(i - 1, 0, -1):
        print(k, end="")
    print()
for i in range(size - 1, 0, -1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(1, i + 1):
        print(k, end="")
    for k in range(i - 1, 0, -1):
        print(k, end="")
    print()

# Q32. Concentric Number Square
size = int(input("Q32 size: "))
for i in range(1, 2 * size):
    for j in range(1, 2 * size):
        dist_top = i - 1
        dist_bottom = 2 * size - 1 - i
        dist_left = j - 1
        dist_right = 2 * size - 1 - j
        min_dist = dist_top
        if dist_bottom < min_dist: min_dist = dist_bottom
        if dist_left < min_dist: min_dist = dist_left
        if dist_right < min_dist: min_dist = dist_right
        print(size - min_dist, end=" ")
    print()

# Q33. Hollow Square
size = int(input("Q33 size: "))
for i in range(1, size + 1):
    for j in range(1, size + 1):
        if i == 1 or i == size or j == 1 or j == size:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Q34. Hollow Rectangle
r = int(input("Q34 rows: "))
c = int(input("Q34 cols: "))
for i in range(1, r + 1):
    for j in range(1, c + 1):
        if i == 1 or i == r or j == 1 or j == c:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Q35. Hollow Number Square
size = int(input("Q35 size: "))
for i in range(1, size + 1):
    for j in range(1, size + 1):
        if i == 1 or i == size or j == 1 or j == size:
            print("1", end="")
        else:
            print("0", end="")
    print()

# Q36. Hollow Right-Angled Triangle
size = int(input("Q36 size: "))
for i in range(1, size + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == size:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Q37. Hollow Inverted Triangle
size = int(input("Q37 size: "))
for i in range(size, 0, -1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == size:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Q38. Hollow Pyramid
size = int(input("Q38 size: "))
for i in range(1, size + 1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1 or i == size:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Q39. Hollow Diamond
size = int(input("Q39 size: "))
for i in range(1, size + 1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
for i in range(size - 1, 0, -1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Q40. X Pattern
size = int(input("Q40 odd size: "))
for i in range(1, size + 1):
    for j in range(1, size + 1):
        if i == j or j == (size - i + 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Q41. Cross Pattern
size = int(input("Q41 odd size: "))
mid = size // 2 + 1
for i in range(1, size + 1):
    for j in range(1, size + 1):
        if i == mid or j == mid:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Q42. Star Cross with Four Arms
size = int(input("Q42 odd size: "))
for i in range(1, size + 1):
    for j in range(1, size + 1):
        if i == j or j == (size - i + 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Q43. Butterfly Pattern
size = int(input("Q43 size: "))
for i in range(1, size + 1):
    for j in range(i):
        print("*", end="")
    for j in range(2 * (size - i)):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()
for i in range(size, 0, -1):
    for j in range(i):
        print("*", end="")
    for j in range(2 * (size - i)):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

# Q44. Hollow Hourglass
size = int(input("Q44 size: "))
for i in range(size, 0, -1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1 or i == size:
            print("*", end="")
        else:
            print(" ", end="")
    print()
for i in range(2, size + 1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1 or i == size:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Q45. Alphabet Diamond
size = int(input("Q45 size: "))
for i in range(1, size + 1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(1, i + 1):
        print(chr(64 + k), end="")
    for k in range(i - 1, 0, -1):
        print(chr(64 + k), end="")
    print()
for i in range(size - 1, 0, -1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(1, i + 1):
        print(chr(64 + k), end="")
    for k in range(i - 1, 0, -1):
        print(chr(64 + k), end="")
    print()

# Q46. Pascal's Triangle
size = int(input("Q46 size: "))
for i in range(1, size + 1):
    for j in range(size - i):
        print(" ", end="")
    val = 1
    for k in range(1, i + 1):
        print(val, end=" ")
        val = val * (i - k) // k
    print()

# Q47. Heart Pattern
size = int(input("Q47 size (e.g. 6): "))
for i in range(size // 2, size, 2):
    for j in range(1, size - i, 2):
        print(" ", end="")
    for j in range(1, i + 1):
        print("*", end="")
    for j in range(1, size - i + 1):
        print(" ", end="")
    for j in range(1, i + 1):
        print("*", end="")
    print()
for i in range(size, 0, -1):
    for j in range(i, size):
        print(" ", end="")
    for j in range(1, (i * 2)):
        print("*", end="")
    print()

# Q48. Hollow Heart
size = int(input("Q48 size: "))
for i in range(size // 2, size, 2):
    for j in range(1, size - i, 2):
        print(" ", end="")
    for j in range(1, i + 1):
        if j == 1 or j == i: print("*", end="")
        else: print(" ", end="")
    for j in range(1, size - i + 1):
        print(" ", end="")
    for j in range(1, i + 1):
        if j == 1 or j == i: print("*", end="")
        else: print(" ", end="")
    print()
for i in range(size, 0, -1):
    for j in range(i, size):
        print(" ", end="")
    for j in range(1, (i * 2)):
        if j == 1 or j == (i * 2) - 1: print("*", end="")
        else: print(" ", end="")
    print()

# Q49. Star-and-Space Center Pattern
size = int(input("Q49 odd size: "))
mid = size // 2 + 1
for i in range(1, size + 1):
    for j in range(1, size + 1):
        if i == j or j == (size - i + 1) or i == mid:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Q50. Custom Symbol Square
size = int(input("Q50 size: "))
sym = input("Q50 symbol: ")
for i in range(size):
    for j in range(size):
        print(sym, end="")
    print()

# Q51. User-Sized Hollow Rectangle
r = int(input("Q51 rows: "))
c = int(input("Q51 cols: "))
for i in range(1, r + 1):
    for j in range(1, c + 1):
        if i == 1 or i == r or j == 1 or j == c:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Q52. Create Your Own Pattern
size = int(input("Q52 size: "))
for i in range(1, size + 1):
    for j in range(1, i + 1):
        print(i * j, end=" ")
    print()

# Q53. Number Increasing Reverse Pyramid
size = int(input("Q53 size: "))
for i in range(size, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Q54. Square Fill Pattern
size = int(input("Q54 size: "))
for i in range(size):
    for j in range(size):
        print("* ", end="")
    print()

# Q55. Left Half Pyramid
size = int(input("Q55 size: "))
for i in range(1, size + 1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()

# Q56. Reverse Right Half Pyramid
size = int(input("Q56 size: "))
for i in range(size, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# Q57. Left Half Pyramid - Increasing
size = int(input("Q57 size: "))
for i in range(1, size + 1):
    for j in range(i):
        print("*", end="")
    print()

# Q58. Reverse Left Half Pyramid
size = int(input("Q58 size: "))
for i in range(size, 0, -1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()

# Q59. Triangle Star Pattern
size = int(input("Q59 size: "))
for i in range(1, size + 1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()

# Q60. Mirror-Image Number Triangle
size = int(input("Q60 size: "))
for i in range(1, size + 1):
    for j in range(1, i):
        print(" ", end="")
    for k in range(i, size + 1):
        print(k, end=" ")
    print()

# Q61. Hollow Reverse Triangle
size = int(input("Q61 size: "))
for i in range(size, 0, -1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(1, i + 1):
        if k == 1 or k == i or i == size:
            print("* ", end="")
        else:
            print("  ", end="")
    print()

# Q62. Hollow Diamond Pyramid
size = int(input("Q62 size: "))
for i in range(1, size + 1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
for i in range(size - 1, 0, -1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Q63. Hollow Hourglass Pattern
size = int(input("Q63 size: "))
for i in range(size, 0, -1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1 or i == size:
            print("*", end="")
        else:
            print(" ", end="")
    print()
for i in range(2, size + 1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1 or i == size:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Q64. Right Pascal's Triangle
size = int(input("Q64 size: "))
for i in range(1, size + 1):
    for j in range(i):
        print("*", end="")
    print()
for i in range(size - 1, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# Q65. Pattern Size Challenge
# Dynamically tested using the above implementations based on user inputs.

# Q66. Count Digits
n = int(input("Q66 number: "))
if n < 0:
    n = -n
count = 0
if n == 0:
    count = 1
else:
    while n > 0:
        count += 1
        n = n // 10
print(count)

# Q67. Sum of Digits
n = int(input("Q67 number: "))
total = 0
while n > 0:
    total += n % 10
    n = n // 10
print(total)

# Q68. Product of Digits
n = int(input("Q68 number: "))
product = 1
if n == 0:
    product = 0
while n > 0:
    product *= n % 10
    n = n // 10
print(product)

# Q69. Reverse a Number
n = int(input("Q69 number: "))
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10
print(rev)

# Q70. Palindrome Number
n = int(input("Q70 number: "))
orig = n
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10
print(orig == rev)

# Q71. Prime Number
n = int(input("Q71 number: "))
is_prime = True
if n < 2:
    is_prime = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
print(is_prime)

# Q72. Primes from 1 to N
n = int(input("Q72 N: "))
for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
    if is_prime:
        print(num, end=" ")
print()

# Q73. First N Fibonacci Numbers
n = int(input("Q73 N: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    temp = a + b
    a = b
    b = temp
print()

# Q74. GCD of Two Numbers
a = int(input("Q74 a: "))
b = int(input("Q74 b: "))
while b != 0:
    temp = b
    b = a % b
    a = temp
print(a)

# Q75. LCM of Two Numbers
a = int(input("Q75 a: "))
b = int(input("Q75 b: "))
temp_a = a
temp_b = b
while temp_b != 0:
    t = temp_b
    temp_b = temp_a % temp_b
    temp_a = t
gcd = temp_a
print((a * b) // gcd)

# Q76. Length of a String
s = input("Q76 string: ")
count = 0
for char in s:
    count += 1
print(count)

# Q77. Print Each Character
s = input("Q77 string: ")
for char in s:
    print(char)

# Q78. Count Vowels
s = input("Q78 string: ")
vowels = 0
for char in s:
    if char in "aeiouAEIOU":
        vowels += 1
print(vowels)

# Q79. Count Consonants
s = input("Q79 string: ")
consonants = 0
for char in s:
    if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
        if char not in "aeiouAEIOU":
            consonants += 1
print(consonants)

# Q80. Convert to Uppercase
s = input("Q80 string: ")
out = ""
for char in s:
    if char >= 'a' and char <= 'z':
        out += chr(ord(char) - 32)
    else:
        out += char
print(out)

# Q81. Convert to Lowercase
s = input("Q81 string: ")
out = ""
for char in s:
    if char >= 'A' and char <= 'Z':
        out += chr(ord(char) + 32)
    else:
        out += char
print(out)

# Q82. Reverse a String
s = input("Q82 string: ")
out = ""
for char in s:
    out = char + out
print(out)

# Q83. Palindrome String
s = input("Q83 string: ")
rev = ""
for char in s:
    rev = char + rev
print(s == rev)

# Q84. Count a Specific Character
s = input("Q84 string: ")
count = 0
for char in s:
    if char == 'a' or char == 'A':
        count += 1
print(count)

# Q85. Remove All Spaces
s = input("Q85 string: ")
out = ""
for char in s:
    if char != " ":
        out += char
print(out)

# Q86. Count Words
s = input("Q86 string: ")
words = 0
in_word = False
for char in s:
    if char != " ":
        if not in_word:
            words += 1
            in_word = True
    else:
        in_word = False
print(words)

# Q87. Replace All 'a' with 'e'
s = input("Q87 string: ")
out = ""
for char in s:
    if char == 'a':
        out += 'e'
    else:
        out += char
print(out)

# Q88. Check for a Character
s = input("Q88 string: ")
ch = input("Q88 char: ")
found = False
for char in s:
    if char == ch:
        found = True
print(found)

# Q89. Compare Two Strings
s1 = input("Q89 string1: ")
s2 = input("Q89 string2: ")
equal = True
if len(s1) != len(s2):
    equal = False
else:
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            equal = False
print(equal)

# Q90. Count Digits in a String
s = input("Q90 string: ")
digits = 0
for char in s:
    if char >= '0' and char <= '9':
        digits += 1
print(digits)

# Q91. Count Uppercase Letters
s = input("Q91 string: ")
up = 0
for char in s:
    if char >= 'A' and char <= 'Z':
        up += 1
print(up)

# Q92. Count Lowercase Letters
s = input("Q92 string: ")
low = 0
for char in s:
    if char >= 'a' and char <= 'z':
        low += 1
print(low)

# Q93. Remove All Vowels
s = input("Q93 string: ")
out = ""
for char in s:
    if char not in "aeiouAEIOU":
        out += char
print(out)

# Q94. Remove All Digits
s = input("Q94 string: ")
out = ""
for char in s:
    if not (char >= '0' and char <= '9'):
        out += char
print(out)

# Q95. Toggle Character Case
s = input("Q95 string: ")
out = ""
for char in s:
    if char >= 'a' and char <= 'z':
        out += chr(ord(char) - 32)
    elif char >= 'A' and char <= 'Z':
        out += chr(ord(char) + 32)
    else:
        out += char
print(out)

# Q96. Multiplication Tables from 1 to N
n = int(input("Q96 N: "))
k = int(input("Q96 K: "))
for i in range(1, n + 1):
    for j in range(1, k + 1):
        print(str(i) + " x " + str(j) + " = " + str(i * j))

# Q97. Number and Its Divisors
n = int(input("Q97 N: "))
for i in range(1, n + 1):
    print(str(i) + ":", end="")
    for j in range(1, i + 1):
        if i % j == 0:
            print(" " + str(j), end="")
    print()

# Q98. Count Divisors for Every Number
n = int(input("Q98 N: "))
for i in range(1, n + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    print(str(i) + ": " + str(count))

# Q99. Perfect Numbers in a Range
n = int(input("Q99 N: "))
for i in range(2, n + 1):
    total = 0
    for j in range(1, i):
        if i % j == 0:
            total += j
    if total == i:
        print(i)

# Q100. Prime Numbers in a Range — Count Each Check
n = int(input("Q100 N: "))
for i in range(2, n + 1):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
    if is_prime:
        print(i, end=" ")
print()

# Q101. Pairs of Digits with a Target Sum
num_str = input("Q101 number: ")
target = int(input("Q101 target: "))
for i in range(len(num_str)):
    for j in range(i + 1, len(num_str)):
        if int(num_str[i]) + int(num_str[j]) == target:
            print(num_str[i] + " " + num_str[j])

# Q102. Digit Pairs with a Fixed Difference
num_str = input("Q102 number: ")
d = int(input("Q102 difference: "))
for i in range(len(num_str)):
    for j in range(i + 1, len(num_str)):
        diff = int(num_str[i]) - int(num_str[j])
        if diff < 0:
            diff = -diff
        if diff == d:
            print(num_str[i] + " " + num_str[j])

# Q103. Repeated Digits in a Number
num_str = input("Q103 number: ")
done = ""
for i in range(len(num_str)):
    already = False
    for char in done:
        if char == num_str[i]:
            already = True
    if not already:
        count = 0
        for j in range(len(num_str)):
            if num_str[j] == num_str[i]:
                count += 1
        if count > 1:
            print(num_str[i])
            done += num_str[i]

# Q104. Count Equal Digit Pairs
num_str = input("Q104 number: ")
count = 0
for i in range(len(num_str)):
    for j in range(i + 1, len(num_str)):
        if num_str[i] == num_str[j]:
            count += 1
print(count)

# Q105. Common Characters in Two Strings
s1 = input("Q105 first string: ")
s2 = input("Q105 second string: ")
done = ""
for i in range(len(s1)):
    already = False
    for char in done:
        if char == s1[i]:
            already = True
    if not already:
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                print(s1[i])
                done += s1[i]
                break

# Q106. Check Whether Two Strings Share a Character
s1 = input("Q106 first: ")
s2 = input("Q106 second: ")
shared = False
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            shared = True
print(shared)

# Q107. Seating Plan
rows = int(input("Q107 rows: "))
seats = int(input("Q107 seats per row: "))
for i in range(1, rows + 1):
    print("Row " + str(i) + ":", end="")
    for j in range(1, seats + 1):
        print(" " + str(j), end="")
    print()

# Q108. Student Marks and Class Total
students = int(input("Q108 Students: "))
tests = int(input("Q108 Tests: "))
class_total = 0
for i in range(1, students + 1):
    student_total = 0
    for j in range(1, tests + 1):
        mark = int(input("Mark for student " + str(i) + ", test " + str(j) + ": "))
        student_total += mark
    print("Student " + str(i) + " total: " + str(student_total))
    class_total += student_total
print("Class total: " + str(class_total))

# Q109. Daily Rainfall Summary
days = int(input("Q109 Days: "))
stations = int(input("Q109 Stations: "))
for i in range(1, days + 1):
    day_total = 0
    for j in range(1, stations + 1):
        rain = int(input("Rain for day " + str(i) + ", station " + str(j) + ": "))
        day_total += rain
    print("Day " + str(i) + " total: " + str(day_total))

# Q110. Largest of Several Numbers in Each Group
groups = int(input("Q110 Groups: "))
nums = int(input("Q110 Numbers per group: "))
for i in range(groups):
    largest = -999999999
    for j in range(nums):
        val = int(input("Number: "))
        if val > largest:
            largest = val
    print(largest)

# Q111. Sum of Numbers by Group and Position
g1_1 = int(input("Group 1, Num 1: "))
g1_2 = int(input("Group 1, Num 2: "))
g1_3 = int(input("Group 1, Num 3: "))
g2_1 = int(input("Group 2, Num 1: "))
g2_2 = int(input("Group 2, Num 2: "))
g2_3 = int(input("Group 2, Num 3: "))
print("Group sums: " + str(g1_1+g1_2+g1_3) + " " + str(g2_1+g2_2+g2_3))
print("Position sums: " + str(g1_1+g2_1) + " " + str(g1_2+g2_2) + " " + str(g1_3+g2_3))

# Q112. Number Pair Comparison Table
n = int(input("Q112 N: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i + j, end=" ")
    print()

# Q113. Count Zeroes in a Number Sequence
n = int(input("Q113 N: "))
zeroes = 0
for i in range(n):
    val = int(input("Number: "))
    if val == 0:
        zeroes += 1
print(zeroes)

# Q114. Print Row and Column Coordinates
r = int(input("Q114 R: "))
c = int(input("Q114 C: "))
for i in range(r):
    for j in range(c):
        print("(" + str(i) + ", " + str(j) + ")", end=" ")
    print()

# Q115. Find Every Occurrence of a Substring
text = input("Q115 text: ")
pattern = input("Q115 pattern: ")
for i in range(len(text) - len(pattern) + 1):
    match = True
    for j in range(len(pattern)):
        if text[i + j] != pattern[j]:
            match = False
    if match:
        print(i, end=" ")
print()

# Q116. Count Matching Character Pairs
s = input("Q116 string: ")
count = 0
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            count += 1
print(count)

# Q117. Check Whether Two Strings Are Anagrams
s1 = input("Q117 string 1: ")
s2 = input("Q117 string 2: ")
if len(s1) != len(s2):
    print(False)
else:
    anagram = True
    checked = ""
    for i in range(len(s1)):
        char = s1[i]
        already = False
        for c in checked:
            if c == char:
                already = True
        if not already:
            c1 = 0
            c2 = 0
            for j in range(len(s1)):
                if s1[j] == char: c1 += 1
                if s2[j] == char: c2 += 1
            if c1 != c2:
                anagram = False
            checked += char
    print(anagram)

# Q118. Print Character Frequency Without a Dictionary
s = input("Q118 string: ")
done = ""
for i in range(len(s)):
    char = s[i]
    already = False
    for c in done:
        if c == char:
            already = True
    if not already:
        count = 0
        for j in range(len(s)):
            if s[j] == char:
                count += 1
        print(char + ": " + str(count))
        done += char

# Q119. Find Repeated Adjacent Characters
s = input("Q119 string: ")
if len(s) > 0:
    current = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current:
            count += 1
        else:
            if count >= 2:
                print(current + ": " + str(count))
            current = s[i]
            count = 1
    if count >= 2:
        print(current + ": " + str(count))

# Q120. Compare Two Words Position by Position
s1 = input("Q120 string 1: ")
s2 = input("Q120 string 2: ")
diff = 0
for i in range(len(s1)):
    if s1[i] != s2[i]:
        diff += 1
print(diff)

# Q121. Print All Pythagorean Triples up to N
n = int(input("Q121 N: "))
for a in range(1, n):
    for b in range(a + 1, n):
        for c in range(b + 1, n + 1):
            if a*a + b*b == c*c:
                print(str(a) + " " + str(b) + " " + str(c))

# Q122. Find Numbers Equal to the Sum of Their Proper Divisors
n = int(input("Q122 N: "))
for i in range(2, n + 1):
    total = 0
    for j in range(1, i):
        if i % j == 0:
            total += j
    if total == i:
        print(i)

# Q123. Print Unique Products in Increasing Factor Order
n = int(input("Q123 N: "))
for i in range(1, n + 1):
    for j in range(i, n + 1):
        prod = i * j
        is_first = True
        for x in range(1, i):
            for y in range(x, n + 1):
                if x * y == prod:
                    is_first = False
        if is_first:
            print(prod, end=" ")
print()

# Q124. Find All Pairs of Prime Numbers with a Given Sum
n = int(input("Q124 N: "))
for i in range(2, n // 2 + 1):
    j = n - i
    prime_i = True
    for x in range(2, int(i**0.5) + 1):
        if i % x == 0: prime_i = False
    if prime_i:
        prime_j = True
        for y in range(2, int(j**0.5) + 1):
            if j % y == 0: prime_j = False
        if prime_j:
            print(str(i) + " " + str(j))

# Q125. Check a Magic-Sum Pattern
n = int(input("Q125 odd N: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i + j, end=" ")
    print()
print("Row sums:", end="")
for i in range(1, n + 1):
    row_sum = 0
    for j in range(1, n + 1):
        row_sum += (i + j)
    print(" " + str(row_sum), end="")
print()

# Q126. Count Peaks in a Number Sequence
n = int(input("Q126 N: "))
prev2 = -1
prev1 = -1
peaks = 0
for i in range(n):
    curr = int(input("Number: "))
    if i >= 2:
        if prev1 > prev2 and prev1 > curr:
            peaks += 1
    prev2 = prev1
    prev1 = curr
print(peaks)

# Q127. Find Repeated Digit Sums
num_str = input("Q127 number: ")
found = False
for i in range(len(num_str)):
    for j in range(i + 1, len(num_str)):
        sum1 = int(num_str[i]) + int(num_str[j])
        for x in range(len(num_str)):
            for y in range(x + 1, len(num_str)):
                if (i == x and j == y) or (i == y and j == x):
                    continue
                if int(num_str[x]) + int(num_str[y]) == sum1:
                    found = True
if found:
    print("Repeated pair sums exist")

# Q128. Number Pattern from Row and Column
n = int(input("Q128 N: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        diff = i - j
        if diff < 0:
            diff = -diff
        print(diff, end=" ")
    print()

# Q129. Compare Digits with Their Neighbours
num_str = input("Q129 number: ")
count = 0
for i in range(1, len(num_str) - 1):
    if int(num_str[i]) > int(num_str[i-1]) and int(num_str[i]) > int(num_str[i+1]):
        count += 1
print(count)

# Q130. Count Increasing Digit Pairs
num_str = input("Q130 number: ")
count = 0
for i in range(len(num_str)):
    for j in range(i + 1, len(num_str)):
        if int(num_str[i]) < int(num_str[j]):
            count += 1
print(count)

# Q131. Character Frequency Compression Without a Dictionary
s = input("Q131 string: ")
done = ""
for i in range(len(s)):
    char = s[i]
    already = False
    for c in done:
        if c == char:
            already = True
    if not already:
        count = 0
        for j in range(len(s)):
            if s[j] == char:
                count += 1
        print(char + str(count), end="")
        done += char
print()
