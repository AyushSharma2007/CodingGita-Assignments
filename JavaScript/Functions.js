// Section 1: What Is a Function?

// Q1. Why do we use functions instead of writing the same code again and again? Explain with one simple example.
// Answer: Functions let us write a block of logic once and reuse it whenever needed, avoiding repetition and making updates easy.
// Example: Instead of writing a + b repeatedly to add marks for 10 students, we write one add(a, b) function and call it 10 times.

// Q2. List any four advantages of functions and write one line for each advantage.
// Answer:
// 1. Reusability: Write the code once and call it multiple times with different inputs.
// 2. Modularity: Breaks a large program into smaller, manageable pieces.
// 3. Easy Maintenance: Updating logic in one place automatically updates every function call.
// 4. Readability: Meaningful function names make code easier to read and understand.

// Q3. Imagine you have to display a welcome message at 6 different places in your program. How will a function help you here?
// Answer: You define the welcome message once inside a function and call it at all 6 places. If the message changes later, you only edit it inside the function instead of 6 separate places.

// Q4. Show the same code written twice without a function and once with a function.
// Without a function:
console.log("Welcome to JavaScript!");
console.log("Welcome to JavaScript!");

// With a function:
function showWelcomeS1() {
    console.log("Welcome to JavaScript!");
}
showWelcomeS1();
showWelcomeS1();

// Q5. Give one real-life analogy that explains the idea of a function.
// Answer: A juicer machine: you give it fruits (input/arguments), it blends them internally (function body), and gives you juice (return value).

// Q6. Why do functions make debugging easier? Answer in 1-2 lines.
// Answer: Functions isolate specific tasks into separate blocks, so you can test and fix a bug in one function without searching through the entire program.


// Section 2: Function Declaration

// Q1. Create a function declaration named displayCourse that returns "JavaScript Fundamentals". Call it and print the result.
function displayCourse() {
    return "JavaScript Fundamentals";
}
console.log(displayCourse());

// Q2. Write a function declaration getStudentStatus that returns the string "Active Learner". Store the returned value in a variable and print it.
function getStudentStatus() {
    return "Active Learner";
}
let studentStatusResult = getStudentStatus();
console.log(studentStatusResult);

// Q3. Write a function declaration and call it before its definition. What happens and why? Explain briefly.
console.log(hoistedGreeting());
function hoistedGreeting() {
    return "Called before declaration!";
}
// Answer: It runs without error and prints "Called before declaration!" because JavaScript hoists the entire function declaration (name and body) to the top of its scope before execution.


// Section 3: Function Expression

// Q1. Create a function expression named showMotto that returns "Code. Learn. Grow.". Call it and print the output.
const showMotto = function () {
    return "Code. Learn. Grow.";
};
console.log(showMotto());

// Q2. Write a function expression getSemester that returns the number 3. Print the value returned by the function.
const getSemester = function () {
    return 3;
};
console.log(getSemester());

// Q3. Create a function expression and try to call it before writing the expression. What error do you get and why?
// console.log(notHoisted()); // ReferenceError: Cannot access 'notHoisted' before initialization (with const/let)
const notHoisted = function () {
    return "Function expression";
};
// Answer: With const/let, it throws a ReferenceError because the variable is in the Temporal Dead Zone until initialized. With var, it throws a TypeError (notHoisted is not a function) because only the variable name is hoisted as undefined.


// Section 4: Function Calling (Invocation)

// Q1. Write a function declaration greetStudent that returns "All the best for your coding journey!". Call this function four times.
function greetStudent() {
    return "All the best for your coding journey!";
}
console.log(greetStudent());
console.log(greetStudent());
console.log(greetStudent());
console.log(greetStudent());

// Q2. Create a function expression todayFocus that returns "Focus on functions today". Store the result in a variable and print that variable.
const todayFocus = function () {
    return "Focus on functions today";
};
let focusMessage = todayFocus();
console.log(focusMessage);

// Q3. Write one function declaration and one function expression. Call each of them twice and print all four results.
function sayHiDeclared() {
    return "Hi from declaration";
}
const sayByeExpressed = function () {
    return "Bye from expression";
};
console.log(sayHiDeclared());
console.log(sayHiDeclared());
console.log(sayByeExpressed());
console.log(sayByeExpressed());


// Section 5: Parameters vs Arguments

// Q1. Write a function declaration subtract(a, b) that returns the difference of two numbers. Call it with 50 and 18 and print the result.
function subtract(a, b) {
    return a - b;
}
console.log(subtract(50, 18));

// Q2. Create a function expression greetUser(name) that returns "Welcome, " + name + "!". Call it with "Aarav".
const greetUser = function (name) {
    return "Welcome, " + name + "!";
};
console.log(greetUser("Aarav"));

// Q3. Write a function calculateArea(length, breadth) that returns the area of a rectangle. Call it with (12, 5) and (8, 9).
function calculateArea(length, breadth) {
    return length * breadth;
}
console.log(calculateArea(12, 5));
console.log(calculateArea(8, 9));

// Q4. What is the difference between a parameter and an argument? Explain with a short example.
// Answer: A parameter is the variable listed inside the function definition, while an argument is the actual value passed when calling the function.
// Example: In function add(x, y), x and y are parameters. In add(4, 6), 4 and 6 are arguments.

// Q5. Can a function have parameters but be called without arguments? What happens in that case? Explain briefly.
// Answer: Yes. JavaScript does not throw an error; any parameter that does not receive an argument automatically gets the value undefined.


// Section 6: Return Statement

// Q1. Write a function squareOfNumber(n) that returns the square of the given number. Call it with 9 and print the returned value.
function squareOfNumber(n) {
    return n * n;
}
console.log(squareOfNumber(9));

// Q2. Create a function isAdult(age) that returns true if age is 18 or above, otherwise false. Test it with 17 and 20.
function isAdult(age) {
    if (age >= 18) {
        return true;
    } else {
        return false;
    }
}
console.log(isAdult(17));
console.log(isAdult(20));

// Q3. Write a function getFullName(firstName, lastName) that returns the full name. Call it with "Rohit" and "Sharma" and print the result.
function getFullName(firstName, lastName) {
    return firstName + " " + lastName;
}
console.log(getFullName("Rohit", "Sharma"));

// Q4. What does a function return if there is no return statement inside it?
// Answer: It returns undefined.

// Q5. Why do we use the return statement in a function instead of just using console.log() inside the function? Explain in 2-3 lines.
// Answer: console.log() only prints output to the console and does not give the value back to the program.
// The return statement sends the calculated result back to the caller so it can be stored in a variable, reused in calculations, or passed to another function.


// Section 7: Why Use Functions? (Real-world Example)

// Q1. Write a function getTotal(m1, m2, m3) to calculate total marks of three subjects and call it four times for 4 students.
function getTotal(m1, m2, m3) {
    return m1 + m2 + m3;
}
console.log("Student 1 Total:", getTotal(78, 85, 90));
console.log("Student 2 Total:", getTotal(65, 70, 72));
console.log("Student 3 Total:", getTotal(92, 88, 95));
console.log("Student 4 Total:", getTotal(55, 60, 58));

// Q2. Create a function calculateSimpleInterest(principal, rate, time) that returns simple interest. Call it for two sets of values.
function calculateSimpleInterest(principal, rate, time) {
    return (principal * rate * time) / 100;
}
console.log("SI 1:", calculateSimpleInterest(5000, 5, 2));
console.log("SI 2:", calculateSimpleInterest(10000, 7, 3));

// Q3. Find the average of three numbers twice without a function, then rewrite using a single function findAverage(a, b, c) and call it twice.
// Without function:
let avgStudent1 = (80 + 70 + 90) / 3;
let avgStudent2 = (60 + 75 + 85) / 3;
console.log("Without function:", avgStudent1, avgStudent2);

// With function:
function findAverage(a, b, c) {
    return (a + b + c) / 3;
}
console.log("With function:", findAverage(80, 70, 90), findAverage(60, 75, 85));

// Q4. How do functions help in reducing code repetition? Explain with one real-world example.
// Answer: Functions encapsulate common logic so you call it instead of copying it everywhere.
// Example: An e-commerce site uses one calculateTax(price) function across product pages, cart, and checkout instead of repeating the tax formula on every page.

// Q5. Mention any three advantages of using functions in a program.
// Answer: 1. Code reusability  2. Easier debugging and maintenance  3. Better organization and readability


// Section 8: Function Scope

// Q1. Create showCity() declaring local city = "Ahmedabad" and printing it. Call it, then try printing city outside and note what happens.
function showCity() {
    let city = "Ahmedabad";
    console.log(city);
}
showCity();
// console.log(city); // ReferenceError: city is not defined (city is local to showCity)

// Q2. Declare global variable trainer = "CodingGita Mentor". Write displayTrainer() to print it. Call the function and print it outside too.
var trainer = "CodingGita Mentor";
function displayTrainer() {
    console.log(trainer);
}
displayTrainer();
console.log(trainer);

// Q3. Write demoScope() with local variable value = 50, print it inside, then try accessing it outside and explain.
function demoScope() {
    let value = 50;
    console.log(value);
}
demoScope();
// console.log(value); // ReferenceError: value is not defined
// Explanation: Inside demoScope() it prints 50, but outside it throws a ReferenceError because value exists only inside demoScope().

// Q4. A variable declared inside a function cannot be used outside. Why does JavaScript follow this rule? How does it help?
// Answer: Function scope prevents accidental modification of variables from other parts of the program and avoids naming conflicts, making code safer and easier to maintain.

// Q5. What will happen if a global variable and a local variable have the same name? Which one will the function use? Explain briefly.
// Answer: The local variable shadows (hides) the global variable inside the function. The function uses its own local variable, while the global variable remains unchanged outside.


// Section 9: Combining Function Concepts

// Q1. Write generateMessage(name, score) checking if passed (score >= 40) and returning a sentence like "Aarav has scored 65 and the result is Pass".
function generateMessage(name, score) {
    let result = score >= 40 ? "Pass" : "Fail";
    return name + " has scored " + score + " and the result is " + result;
}
console.log(generateMessage("Aarav", 65));
console.log(generateMessage("Riya", 32));

// Q2. Create billCalculator(item1, item2, item3) returning total amount and whether discount applies (total >= 1000 -> "Discount Applied", else "No Discount").
function billCalculator(item1, item2, item3) {
    let total = item1 + item2 + item3;
    let discountStatus = total >= 1000 ? "Discount Applied" : "No Discount";
    return "Total: " + total + " - " + discountStatus;
}
console.log(billCalculator(400, 350, 300));
console.log(billCalculator(200, 150, 300));

// Q3. Write performanceReport(student, m1, m2, m3) calculating total, average, and remark ("Excellent" if average >= 80, else "Keep Improving").
function performanceReport(student, m1, m2, m3) {
    let total = m1 + m2 + m3;
    let average = total / 3;
    let remark = average >= 80 ? "Excellent" : "Keep Improving";
    return "Student: " + student + " | Total: " + total + " | Average: " + average.toFixed(2) + " | Remark: " + remark;
}
console.log(performanceReport("Priya", 85, 90, 88));
console.log(performanceReport("Aman", 65, 70, 72));

// Q4. Why is it better to perform multiple related tasks (calculation + decision + message) inside one function instead of separate scattered code?
// Answer: Grouping related steps into one function keeps the workflow self-contained, ensures consistent results every time it is called, and prevents repeating the same multi-step logic.

// Q5. How does combining parameters, return, and conditions inside a single function improve code quality?
// Answer: Parameters make the function adaptable, conditions handle decision-making dynamically, and return passes back clean reusable results, reducing duplication and bugs.


// Section 10: Nested Functions

// Q1. Write mainTask containing inner function helperTask returning "Task completed successfully". Call helperTask from mainTask and return its result.
function mainTask() {
    function helperTask() {
        return "Task completed successfully";
    }
    return helperTask();
}
console.log(mainTask());

// Q2. Create calculateFinal(m1, m2) with inner function getTotal to add marks, returning "Final marks = " followed by the total.
function calculateFinal(m1, m2) {
    function getTotal() {
        return m1 + m2;
    }
    return "Final marks = " + getTotal();
}
console.log(calculateFinal(42, 46));

// Q3. Write studentStatus(name, marks) with inner function getGrade ("A" if >= 80, "B" if >= 60, else "C"). Return a final sentence using name and grade.
function studentStatus(name, marks) {
    function getGrade() {
        if (marks >= 80) {
            return "A";
        } else if (marks >= 60) {
            return "B";
        } else {
            return "C";
        }
    }
    return name + " secured Grade " + getGrade();
}
console.log(studentStatus("Neha", 86));
console.log(studentStatus("Rahul", 68));
console.log(studentStatus("Karan", 45));

// Q4. What is the main advantage of writing a function inside another function? When should we use nested functions?
// Answer: The main advantage is encapsulation: helper logic stays private inside the outer function and does not clutter the global scope.
// Use nested functions when a small helper task is only needed by one specific outer function.

// Q5. Can an inner function access variables of the outer function? What about the reverse (outer accessing inner variables)? Explain.
// Answer: Yes, an inner function can access variables of its outer function through the scope chain.
// No, the outer function cannot access variables declared inside the inner function because scope lookup only moves outward, not inward.
