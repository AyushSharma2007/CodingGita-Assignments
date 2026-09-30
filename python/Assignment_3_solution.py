
# ASSIGNMENT 3 - ALL SOLUTIONS (Q1 TO Q70

# Topic-1: Comparison Operators

# Q1. Predict the Output
# Output:
# True
# False
# False
# True
# True
# False

# Q2. Compare Expressions
# Output:
# True
# False
# False
# True
# True
# Note: == compares equality; = assigns values to variables.

# Q3. Comparison with Arithmetic
# Output:
# True
# True
# False
# True

# Q4. String Comparison
# Output:
# True
# False
# True
# Note: String comparison is case-sensitive ("P" != "p").

# Topic-2: Assignment Operators

# Q5. Trace the Value
# Step trace:
# x = 20
# x += 10 -> 30
# x -= 5  -> 25
# x *= 2  -> 50
# x //= 5 -> 10
# Final output: 10

# Q6. Assignment Operator Practice
marks = 50
marks += 10
marks -= 5
marks *= 2
print(marks)

# Topic-3: Membership Operators with Strings

# Q7. Basic Membership
# Output:
# True
# False
# False

# Q8. Character Membership
word = "computer"
print("p" in word)
print("x" in word)
print("c" not in word)

# Q9. Case Sensitivity in Membership
# Output:
# True
# False
# True
# False
# Reason: Membership checks match character case strictly.

# Q10. Membership with User Input
text = input("Enter text: ")
print("a" in text)

# Q11. Email Symbol Check
email = input("Enter email: ")
print("@" in email)

# Topic-4: ASCII and Unicode

# Q12. Find Character Codes
print(ord("A"))  # 65
print(ord("a"))  # 97
print(ord("Z"))  # 90
print(ord("z"))  # 122
print(ord("0"))  # 48
print(ord("9"))  # 57
print(ord("@"))  # 64

# Q13. Convert Codes to Characters
print(chr(65))  # A
print(chr(66))  # B
print(chr(97))  # a
print(chr(98))  # b
print(chr(48))  # 0
print(chr(57))  # 9
print(chr(64))  # @

# Q14. Uppercase and Lowercase
# 1. ord("a") is larger (97 > 65)
# 2. Difference is 32 (97 - 65 = 32)
# 3. Yes, diff between ord("b") and ord("B") is also 32 (98 - 66 = 32)

# Q15. Character Code Program
ch = input("Enter a character: ")
print(ord(ch))

# Q16. Next Character
char_in = input("Enter an uppercase letter: ")
print(chr(ord(char_in) + 1))

# Q17. Character Comparison and Unicode
# Output:
# True
# True
# True
# True
# Reason: Characters are compared by Unicode points (ord('A')=65 < ord('B')=66, etc.)

# Q18. Unicode Character Challenge
print(chr(9731))  # ☃
print(chr(9829))  # ♥
print(chr(8377))  # ₹
print(ord("☃"))   # 9731
print(ord("♥"))   # 9829
print(ord("₹"))   # 8377

# Topic-5: String Indexing

# Q19. Basic Indexing
text_py = "PYTHON"
print(text_py[0])
print(text_py[1])
print(text_py[-1])
print(text_py[-2])

# Q20. Positive and Negative Indexing
text_comp = "COMPUTER"
print(text_comp[0])   # C
print(text_comp[3])   # P
print(text_comp[-1])  # R
print(text_comp[-3])  # T

# Q21. Predict the Output
# Output:
# P
# T
# N
# O

# Q22. Indexing a User Input
user_word = input("Enter a word: ")
print(user_word[0], "and", user_word[-1])

# Q23. Think Carefully About Indexing
# word = "PROGRAM"
# word[0]  -> 'P'
# word[2]  -> 'O'
# word[-1] -> 'M'
# word[-4] -> 'G'

# Topic-6: String Slicing

# Q24. Basic Slicing
# Output:
# PYT
# THO
# YTHON

# Q25. Start and Stop
# Output:
# PROG
# RAMMING
# PROGRAMMING

# Q26. Negative Slicing
# Output:
# PUTER
# COMPU
# OMPU

# Q27. Step in Slicing
# Output:
# PTO
# YHN
# NOHTYP

# Q28. Reverse a String
rev_str = input("Enter string: ")
print(rev_str[::-1])

# Q29. Alternate Characters
alt_str = input("Enter string: ")
print(alt_str[::2])

# Q30. Extract First and Last Three Characters
three_str = input("Enter string: ")
print(three_str[:3], three_str[-3:])

# Q31. Slicing Challenge
# text[2:8:2]  -> 'CEG'   (start: 2, stop: 8, step: 2)
# text[8:2:-2] -> 'IGE'   (start: 8, stop: 2, step: -2)
# text[::-2]   -> 'JHFDB' (start: -1 / end, stop: beginning, step: -2)

# Q32. Slice Without Counting from the Beginning
text_batch = "BTECH-CSE-2026"
print(text_batch[:5])
print(text_batch[6:9])
print(text_batch[-4:])

# Topic-7: String split()

# Q33. Basic split()
# Output: ['Python', 'is', 'easy']
# Whitespace (spaces) separates the words by default.

# Q34. Custom Separator
# Output: ['apple', 'banana', 'mango']

# Q35. Separator Not Present
# Output: ['Python is easy']
# Reason: Comma ',' does not exist in the string, so no split occurs.

# Q36. Split a Full Name
full_name_input = input("Enter full name: ")
w1, w2, w3 = full_name_input.split()
print(w1)
print(w2)
print(w3)

# Q37. Multiple Inputs Using split()
first_name, last_name = input("Enter two names: ").split()
print("First Name:", first_name)
print("Last Name:", last_name)

# Q38. Three Numeric Inputs
n1, n2, n3 = input("Enter 3 integers: ").split()
print(int(n1) + int(n2) + int(n3))

# Q39. Student Record
record = input("Enter record: ")
name, age, course, city = record.split(",")
print("Name:", name)
print("Age:", age)
print("Course:", course)
print("City:", city)

# Q40. Email Analyzer
email_in = input("Enter email: ")
username, domain = email_in.split("@")
print("Username:", username)
print("Domain:", domain)

# Q41. Sentence Analyzer
sentence_in = input("Enter sentence: ")
words_list = sentence_in.split()
print("First word:", words_list[0])
print("Last word:", words_list[-1])
print("Total words:", len(words_list))

# Topic-8: Escape Sequences

# Q42. New Line
print("Hello\nWorld")

# Q43. Tab
print("Name:\tRahul\nAge:\t20\nCity:\tAhmedabad")

# Q44. Backslash
print("C:\\Python\\Programs")

# Q45. Single Quote
print("It\'s Python")

# Q46. Double Quote
print("He said \"Hello\"")

# Q47. Predict the Output
# Output:
# Python
# Programming

# Q48. Combined Escape Sequences
print("Student Details\n\nName:\tRahul\nAge:\t20\nCourse:\tB.Tech")

# Topic-9: print(), sep, end, and f-Strings

# Q49. sep
# Output:
# 2026-09-09

# Q50. end
# Output:
# Hello Python

# Q51. sep and end
print("10", "20", "30", sep="-")
print("40", "50", "60", sep="-")

# Q52. Student Introduction
s_name = input("Name: ")
s_age = input("Age: ")
s_city = input("City: ")
s_course = input("Course: ")
print(f"Name: {s_name}\nAge: {s_age}\nCity: {s_city}\nCourse: {s_course}")

# Q53. Formatted Price
price_val = float(input("Enter price: "))
print(f"{price_val:.2f}")

# Topic-10: Debugging

# Q54. String and Integer
# Error: age is a string; cannot add string and integer.
age_fixed = int(input("Enter age: "))
print("Age after 5 years:", age_fixed + 5)

# Q55. Incorrect Quotes
# Error: Unescaped single quote ends string prematurely.
print("It's Python")  # or print('It\'s Python')

# Q56. Incorrect Slicing Syntax
# Error: Slicing uses colons (:), not commas (,).
text_slice = "Python"
print(text_slice[1:4])

# Q57. Incorrect split() Separator
# Error: .split(',') looks for a comma, but input has a space.
a_fixed, b_fixed = input().split()

# Q58. String Addition vs Numeric Addition
# Program prints: 1020 (string concatenation)
# Fix:
num_a, num_b = input().split()
print(int(num_a) + int(num_b))

# Q59. Escape Sequence Debugging
# Problem: \n and \t act as newline and tab escape sequences.
# Fix:
print("C:\\new\\test")  # or print(r"C:\new\test")

# Topic-11: Integrated Problems


# Q60. Student Result Information
st_name = input("Name: ")
m1, m2, m3 = input("Marks: ").split()
tot = int(m1) + int(m2) + int(m3)
avg = tot / 3
print(f"Name: {st_name}")
print(f"Total: {tot}")
print(f"Average: {avg:.2f}")

# Q61. Student ID Analyzer
full_id = input("Enter ID: ")
deg, batch_yr, br, r_str = full_id.split("-")
roll_num = int(full_id[-3:])
print(f"Degree: {deg}")
print(f"Batch: {batch_yr}")
print(f"Branch: {br}")
print(f"Roll Number: {roll_num}")

# Q62. Username Generator
name_three = input("Enter full name: ")
w_first, w_mid, w_last = name_three.split()
username_gen = w_first.lower() + "." + w_last.lower()
print(username_gen)

# Q63. Sentence Information
sen_input = input("Enter sentence: ")
words_all = sen_input.split()
print("First word:", words_all[0])
print("Last word:", words_all[-1])
print("Total words:", len(words_all))

# Q64. Email Analyzer + Membership
em_input = input("Enter email: ")
at_present = "@" in em_input
em_user, em_domain = em_input.split("@")
print(f"@ Present: {at_present}")
print(f"Username: {em_user}")
print(f"Domain: {em_domain}")

# Q65. Character Analyzer
single_char = input("Enter character: ")
char_code = ord(single_char)
print(f"Character: {single_char}")
print(f"Code: {char_code}")
print(f"Previous: {chr(char_code - 1)}")
print(f"Next: {chr(char_code + 1)}")

# Q66. Product Bill
prod_name = input("Product: ")
p_price = float(input("Price: "))
p_qty = int(input("Quantity: "))
p_disc = float(input("Discount: "))
sub_tot = p_price * p_qty
disc_amt = sub_tot * p_disc / 100
fin_tot = sub_tot - disc_amt
print(f"Product: {prod_name}")
print(f"Price: {p_price:.2f}")
print(f"Quantity: {p_qty}")
print(f"Subtotal: {sub_tot:.2f}")
print(f"Discount: {disc_amt:.2f}")
print(f"Final Total: {fin_tot:.2f}")

# Q67. Date Analyzer
date_raw = input("Enter date: ")
d_day, d_month, d_year = date_raw.split("-")
print(f"Day: {d_day}")
print(f"Month: {d_month}")
print(f"Year: {d_year}")
print(date_raw[-4:])

# Q68. String Transformation Challenge
str_two = input("Enter two words: ")
word_one, word_two = str_two.split()
print(f"First Word: {word_one}")
print(f"Second Word: {word_two}")
print(f"First Word Reversed: {word_one[::-1]}")
print(f"Second Word Reversed: {word_two[::-1]}")

# Q69. Final Challenge — Student Code Formatter
id_code_in = input("Enter ID: ")
c_deg, c_batch, c_branch, c_roll = id_code_in.split("-")
code_str = f"{c_deg}/{c_branch}/{c_roll}"
print(f"Degree: {c_deg}")
print(f"Batch: {c_batch}")
print(f"Branch: {c_branch}")
print(f"Roll: {c_roll}")
print(f"Code: {code_str}")

# Q70. Final String + Input/Output Challenge
orig_full_name = input("Enter full name: ")
name_parts = orig_full_name.split()
f_part = name_parts[0]
l_part = name_parts[-1]
f_up = f_part[:3].upper()
l_low = l_part[1:4].lower()
rev_name = orig_full_name[::-1]

print(f"Original: {orig_full_name}")
print(f"First Name: {f_part}")
print(f"Last Name: {l_part}")
print(f"First Name (Upper Part): {f_up}")
print(f"Last Name (Lower Part): {l_low}")
print(f"Full Name Reversed: {rev_name}")
