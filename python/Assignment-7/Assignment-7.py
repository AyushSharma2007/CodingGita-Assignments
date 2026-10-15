################# Type - 1 ###################

#### level - 1

# 1. 

    # 1
    # 2
    # 3
    # 4 

# 2.
    # 2 4 6 8

# 3.
    # 5 4 3 2 1 

# 4.
    # Finished

# 5.
    # 2 3 4 5
    
    
#### Level - 2

# 6.
    # 1 2 3 Done
    
# 7. 
    # 1 4 7 

# 8.
    # 7 4 1 -2


#### Level - 3

# 9. 
    #  10

# 10.
    # 16

# 11.
    # 2 1 0

# 12.
    # 58 5 0


#### Level - 4

# 13.
    # 2 4 6 

# 14.
    # odd even odd even odd 

# 15. 
    # 1 2 4 8

# 16. 
    # 5 3 1  stop: -1
    
    
#### Level - 5

# 17.
    # A
    # AA
    # AAA
    # AAAA

# 18.
    # PY
    # PYT
    # PYTT
    # PYTTT
    # PYTTTT

# 19.
    # 3 (WHILE LOOP DOESNT RUN AT ALL)
    
# 20.
    # B - since the condition for the while loop to run is always True.
    
    
##### Reflection Questions

# 1. Why must a loop variable often be updated inside a while loop?
# To ensure the loop eventually terminates. If the loop variable isn't updated, the condition will never become false, causing an infinite loop.

# 2. Can a while loop execute zero times? Give an example from this worksheet.
# Yes, if the condition evaluates to False on the very first check, the loop is entirely skipped. Q4 (count = 7; while count < 5) and Q19 (x = 3; while x > 10) are examples of this.

# 3. What is the difference between updating a variable before print() and after print()?
# Updating the variable before print() modifies the value first, meaning the first printed value is the newly updated one (e.g., Q5 starts at 2). Updating after print() displays the current value before it gets changed for the next iteration (e.g., Q1 starts at 1).

# 4. How can you recognize a possible infinite loop by reading the code?
# By checking the loop variable's initial value, the condition, and how it is updated. If the update moves the variable's value away from making the condition false (like subtracting when the condition waits for it to reach a higher maximum, as seen in Q20), or if there is no update at all, it's an infinite loop.

# 5. Why should you trace the condition again after every update?
# Because the variable's value changes during the loop execution. Sometimes a variable can dip below or shoot past a threshold mid-loop, and tracing helps predict exactly when the loop will evaluate as False upon the next check at the top.
