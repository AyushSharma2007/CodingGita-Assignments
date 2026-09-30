"""
Assignment-1 Solutions & Debugging Reference
"""

# 
# Topic 1: Variables and Variable Naming
# 

#   Question 1  
# Issue: No issue; valid variable declaration and printing.
name = "Raju"
print("Name:", name)

#   Question 2  
# Issue: 'Student_name' had a capitalized 'S', which violates case sensitivity since it was declared as 'student_name'.
student_name = "Aman"
print("Student Name:", student_name)

#   Question 3  
# Issue: Variable names cannot contain spaces ('student name'). Replaced with an underscore.
student_name = "Rahul"
print("Student Name:", student_name)

#   Question 4  
# Issue: Variable names cannot begin with a number ('1student_name').
student_name = "Ravi"
print("Student Name:", student_name)

#   Question 5  
# Issue: Variable names cannot contain hyphens ('student-name') as '-' is the subtraction operator.
student_name = "Rohan"
print("Student Name:", student_name)

#   Question 6  
# Issue: No issue; valid variable assignments and print statements.
student_name = "Neha"
student_age = 19
print("Name:", student_name)
print("Age:", student_age)

#   Question 7  
# Issue: No issue; Python is case-sensitive, so 'Student_Name' and 'student_name' are two distinct valid variables.
Student_Name = "Karan"
student_name = "Raj"
print("Student 1:", Student_Name)
print("Student 2:", student_name)

#   Question 8  
# Issue: 'student age' contained a space and in print 'student_age' was called. Replaced space with underscore.
student_name = "Priya"
student_age = 19
print("Name:", student_name)
print("Age:", student_age)

#   Question 9  
# Issue: Variable name '2name' started with a digit. Renamed to 'name_2'.
name_2 = "Amit"
student_age = 18
print("Name:", name_2)
print("Age:", student_age)

#   Question 10  
# Issue: 'studentName' in print() did not match the declared variable 'student_name'.
college_name = "ABC College"
student_name = "Meera"
print("College:", college_name)
print("Student:", student_name)

#   Question 11  
# Issue: No issue; variables properly initialized and printed.
first_name = "Raj"
last_name = "Patel"
print("Full Name:", first_name, last_name)

#   Question 12  
# Issue: 'first name' contained a space in variable assignment.
first_name = "Raj"
last_name = "Patel"
print("Full Name:", first_name, last_name)


# 
# Topic 2: print() Practice
# 

#   Question 13: Student Introduction  
name = "Rahul Raj"
age = 18
course = "B.Tech"
city = "Patna"
print(f"My name is {name}. I am {age} years old. I am studying {course} and I live in {city}.")

#   Question 14: Student Details  
name = "Aman Kumar"
roll_number = 101
branch = "Computer Science"
semester = 1
print(f"My name is {name}. My roll number is {roll_number}. I am studying {branch} in semester {semester}.")

#   Question 15: Personal Information  
name = "Priya Sharma"
age = 19
gender = "Female"
city = "Jaipur"
print(f"My name is {name}. I am {age} years old. I am {gender} and I live in {city}.")

#   Question 16: Mobile Details  
brand = "Samsung"
model = "Galaxy A55"
ram = "8 GB"
storage = "256 GB"
print(f"I have a {brand} {model} with {ram} RAM and {storage} storage.")

#   Question 17: Employee Introduction  
name = "Rohit Kumar"
job_role = "Software Developer"
company = "ABC Technologies"
experience = "2 years"
print(f"My name is {name}. I work as a {job_role} at {company} and I have {experience} of experience.")

#   Question 18: College Information  
college = "XYZ Institute of Technology"
course = "B.Tech"
branch = "Information Technology"
city = "Ahmedabad"
print(f"I am studying {course} in {branch} at {college} in {city}.")

#   Question 19: Product Information  
product = "Laptop"
brand = "HP"
price = 55000
quantity = 1
print(f"I bought {quantity} {brand} {product} for {price} rupees.")

#   Question 20: Family Details  
name = "Rahul Raj"
father_name = "Rajesh Kumar"
mother_name = "Sunita Kumar"
city = "Patna"
print(f"My name is {name}. My father's name is {father_name}. My mother's name is {mother_name}. I live in {city}.")

#   Question 21: Student Result  
name = "Neha Sharma"
subject = "Python Programming"
marks = 88
grade = "A"
percentage = 88.0
print(f"{name} scored {marks} marks in {subject}. Her grade is {grade} and her percentage is {percentage}.")

#   Question 22: Laptop Information  
brand = "HP"
model = "Pavilion 15"
processor = "Intel Core i5"
ram = "16 GB"
storage = "512 GB SSD"
price = 65000
print(f"I have an {brand} {model} with {processor}, {ram} RAM, {storage}, and it costs {price} rupees.")

#   Question 23: Movie Information  
movie = "3 Idiots"
genre = "Comedy Drama"
rating = 8.4
language = "Hindi"
release_year = 2009
print(f"{movie} is a {genre} movie in {language}. It was released in {release_year} and has a rating of {rating}.")

#   Question 24: Final Mixed Practice  
name = "Arjun Patel"
age = 19
college = "ABC Institute of Technology"
branch = "Computer Science"
semester = 1
city = "Ahmedabad"
percentage = 87.5
programming_language = "Python"
print(f"My name is {name}. I am {age} years old and I am studying {branch} in semester {semester} at {college} in {city}. I scored {percentage} percent and my favorite programming language is {programming_language}.")


# 
# Topic 3: Data Types and type()
# 

#   Question 21  
# Issue: No issue; valid type checks.
name = "Riya"
age = 20
marks = 85.5
print("Name:", name)
print("Age:", age)
print("Marks:", marks)
print("Name Type:", type(name))
print("Age Type:", type(age))
print("Marks Type:", type(marks))

#   Question 22  
# Issue: 'Marks' in print() was capitalized instead of 'marks'.
name = "Riya"
age = 20
marks = 85.5
print("Name:", name)
print("Age:", age)
print("Marks:", marks)
print("Name Type:", type(name))
print("Age Type:", type(age))
print("Marks Type:", type(marks))

#   Question 23  
# Issue: No issue; string and float types correctly evaluated.
age = "18"
marks = 85.5
print("Age:", age)
print("Marks:", marks)
print("Age Type:", type(age))
print("Marks Type:", type(marks))

#   Question 24  
# Issue: No issue; integer and string types correctly evaluated.
age = 18
marks = "85.5"
print("Age:", age)
print("Marks:", marks)
print("Age Type:", type(age))
print("Marks Type:", type(marks))

#   Question 25  
# Issue: No issue; all types printed correctly.
name = "Ravi"
age = 18
marks = 90.5
passed = True
print("Name:", name)
print("Age:", age)
print("Marks:", marks)
print("Passed:", passed)
print(type(name))
print(type(age))
print(type(marks))
print(type(passed))

#   Question 26  
# Issue: 'Age' was capitalized and 'mark' was used instead of 'marks' in type().
name = "Ravi"
age = 18
marks = 90.5
passed = True
print("Name:", name)
print("Age:", age)
print("Marks:", marks)
print("Passed:", passed)
print(type(name))
print(type(age))
print(type(marks))
print(type(passed))

#   Question 27  
# Issue: No issue; correctly defined and printed.
student_name = "Karan"
student_age = 18
student_marks = 87.5
print("Student:", student_name)
print("Age:", student_age)
print("Marks:", student_marks)
print("Student Type:", type(student_name))
print("Age Type:", type(student_age))
print("Marks Type:", type(student_marks))

#   Question 28  
# Issue: 'student_Name' inside type() had a capital 'N'.
student_name = "Karan"
student_age = 18
student_marks = 87.5
print("Student:", student_name)
print("Age:", student_age)
print("Marks:", student_marks)
print("Student Type:", type(student_name))
print("Age Type:", type(student_age))
print("Marks Type:", type(student_marks))


# 
# Topic 4: Syntax Errors and Debugging
# 

#   Question 29  
# Issue: Unclosed string literal for "Riya.
name = "Riya"
age = 20
print("Name:", name)
print("Age:", age)

#   Question 30  
# Issue: Missing closing parenthesis in print("Age:", age).
name = "Aman"
age = 18
print("Name:", name)
print("Age:", age)

#   Question 31  
# Issue: 'Student_name' had capital 'S' in print().
student_name = "Rohan"
student_age = 19
student_city = "Ahmedabad"
print("Name:", student_name)
print("Age:", student_age)
print("City:", student_city)

#   Question 32  
# Issue: Variable 'studentCity' did not match snake_case 'student_city'.
student_name = "Neha"
student_age = 20
student_city = "Vadodara"
print("Name:", student_name)
print("Age:", student_age)
print("City:", student_city)
print("Name Type:", type(student_name))
print("Age Type:", type(student_age))
print("City Type:", type(student_city))

#   Question 33  
# Issue: Unclosed string "Amit, capitalized 'Student_age', and missing closing parenthesis in type(student_age).
student_name = "Amit"
student_age = 18
student_college = "XYZ College"
print("Name:", student_name)
print("Age:", student_age)
print("College:", student_college)
print("Name Type:", type(student_name))
print("Age Type:", type(student_age))

#   Question 34  
# Issue: Missing closing parenthesis on type(student_college).
student_name = "Meera"
student_age = 20
student_college = "ABC College"
print("Name:", student_name)
print("Age:", student_age)
print("College:", student_college)
print("Name Type:", type(student_name))
print("Age Type:", type(student_age))
print("College Type:", type(student_college))

#   Question 35  
# Issue: No issue; perfectly valid syntax and logic.
student_name = "Raju"
student_age = 18
student_marks = 92.5
is_passed = True
print("Name:", student_name)
print("Age:", student_age)
print("Marks:", student_marks)
print("Passed:", is_passed)
print("Name Type:", type(student_name))
print("Age Type:", type(student_age))
print("Marks Type:", type(student_marks))
print("Passed Type:", type(is_passed))

#   Question 36  
# Issue: 'student name' contained a space during declaration.
student_name = "Raju"
student_age = 18
student_marks = 92.5
is_passed = True
print("Name:", student_name)
print("Age:", student_age)
print("Marks:", student_marks)
print("Passed:", is_passed)

#   Question 37  
# Issue: 'Name' and 'Marks' capitalized in print(), missing parenthesis in print("Age:", age), and 'Age' capitalized in type().
name = "Amit"
age = 18
marks = 91.5
print("Name:", name)
print("Age:", age)
print("Marks:", marks)
print("Name Type:", type(name))
print("Age Type:", type(age))
print("Marks Type:", type(marks))

#   Question 38  
# Issue: Missing closing parenthesis on print("Age:", student_age).
college_name = "ABC College"
student_name = "Riya"
student_age = 19
print("College:", college_name)
print("Student:", student_name)
print("Age:", student_age)
print("College Type:", type(college_name))

#   Question 39  
# Issue: 'class' is a reserved Python keyword and cannot be used as a variable name. Renamed to 'student_class'.
student_class = "B.Tech"
student_name = "Ravi"
print("Class:", student_class)
print("Student:", student_name)

#   Question 40  
# Issue: Capitalized 'Student_name' in print() and missing closing parenthesis on type(student_age).
student_name = "Ravi"
student_age = 18
student_marks = 89.5
print("Name:", student_name)
print("Age:", student_age)
print("Marks:", student_marks)
print("Name Type:", type(student_name))
print("Age Type:", type(student_age))
print("Marks Type:", type(student_marks))

#   Question 41  
# Issue: Space in 'student age', variable starting with digit '2student_marks', capitalized 'Student_name', and missing parenthesis in type(student_age).
student_name = "Ravi"
student_age = 18
student_marks = 89.5
print("Name:", student_name)
print("Age:", student_age)
print("Marks:", student_marks)
print("Name Type:", type(student_name))
print("Age Type:", type(student_age))
print("Marks Type:", type(student_marks))

#   Question 42 ---
# Issue: Unclosed string "Karan, assignment syntax error 'print=', undefined 'Age' and 'Marks', typo 'printt', and missing parenthesis in print("College:", college_name).
name = "Karan"
age = "18"
marks = 87.5
college_name = "ABC College"
print("Name:", name)
print("Age:", age)
print("Marks:", marks)
print("College:", college_name)
print("Name Type:", type(name))
print("Age Type:", type(age))
print("Marks Type:", type(marks))
print("College Type:", type(college_name))
