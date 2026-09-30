# Q69. Debug the Condition
# Fix: Cast the input to an integer to allow mathematical comparison.
age = int(input())

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")


# Q70. Debug the Nested Condition
# Fix: Added the inner 'else' block to handle scores between 40 and 74.
marks = int(input())

if marks >= 40:
    if marks >= 90:
        print("A")
    elif marks >= 75:
        print("B")
    else:
        print("Pass")
else:
    print("Fail")


Explanation for Q70 :-
The original program fails for marks between 40 and 74 (such as 50) because it enters the outer if marks >= 40: block but finds no matching condition inside it. It checks for >= 90 and >= 75, but has no fallback for values below 75, resulting in no output. Adding an else block to the nested conditions fixes this by handling the remaining passing grades.
