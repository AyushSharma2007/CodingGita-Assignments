# Q71. Condition Order
# Prediction: 85 -> Pass
# Explanation: Python evaluates `if-elif-else` statements from top to bottom 
# and stops at the very first true condition. Since 85 >= 40 evaluates to True, 
# it prints "Pass" and skips the rest of the block entirely. It never even 
# checks if marks are >= 75.

marks_71 = 85
if marks_71 >= 40:
    print("Pass")
elif marks_71 >= 75:
    print("Very Good")
else:
    print("Fail")


# Q72. Correct the Condition Order
# Predictions:
# 95 -> A
# 85 -> B
# 50 -> Pass
# 30 -> Fail
# Explanation: In an `if-elif` chain, only the first matching condition is executed. 
# If you were to put `marks >= 40` at the top, a score of 95 would trigger "Pass" 
# instead of "A" because it satisfies that lower threshold first. Organizing from 
# highest to lowest ensures numbers are caught in their most precise category.

marks_72 = 85
if marks_72 >= 90:
    print("A")
elif marks_72 >= 75:
    print("B")
elif marks_72 >= 40:
    print("Pass")
else:
    print("Fail")


# Q73. Nested `if` Execution Flow
# Predictions:
# age = 20, has_id = True  -> Entry Allowed
# age = 20, has_id = False -> ID Required
# age = 16, has_id = True  -> Underage

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry Allowed")
    else:
        print("ID Required")
else:
    print("Underage")


# Q74. `match-case` and Default Case
# Predictions:
# 1 -> Add
# 3 -> Delete
# 5 -> Invalid Choice
# Explanation: The `case _` acts as a wildcard or "default" case. It catches any 
# value that didn't match the specific cases defined above it, preventing the 
# program from failing silently if an unexpected input is given.

choice = 5
match choice:
    case 1:
        print("Add")
    case 2:
        print("View")
    case 3:
        print("Delete")
    case _:
        print("Invalid Choice")


# Q75. Final Execution Challenge
# Predictions:
# 82 80 -> Grade B
# 92 80 -> Grade A
# 55 80 -> Pass
# 92 60 -> Not Eligible
# Explanation: The outermost condition (`attendance >= 75`) is checked first 
# because it acts as the main gateway; Python must evaluate this top-level 
# condition before it can step inside to evaluate the nested grade logic.

marks_75 = 82
attendance = 80

if attendance >= 75:
    if marks_75 >= 90:
        print("Grade A")
    elif marks_75 >= 75:
        print("Grade B")
    elif marks_75 >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not Eligible")
