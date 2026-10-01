// Part a


// 1. Personal Information
let Name = "Vantika";
let age = 20;
let city = "Agra";

console.log("Q1:", Name);
console.log("Q1:", age);
console.log("Q1:", city);

// 2. Change the Score
let score = 50;
score = 80;

console.log("Q2:", score);

// 3. Constant Value
const PI = 3.14;
console.log("Q3:", PI);
// PI = 3.14159; // This would cause a TypeError because const values cannot be changed.

// 4. Uninitialized Variables
var num1;
let num2;

console.log("Q4 before assignment:", num1); // Output: undefined
console.log("Q4 before assignment:", num2); // Output: undefined

num1 = 10;
num2 = 20;

console.log("Q4 after assignment:", num1); // Output: 10
console.log("Q4 after assignment:", num2); // Output: 20



// Part b


// 5. Choose the Correct Keyword
const studentName = "Ayush"; // const because the student's identity won't change
let marks = 85;              // let because test marks will change over time
const schoolName = "Swaminarayan University"; // const because the school name remains static

marks = 92;

console.log("Q5:", studentName);
console.log("Q5:", marks);
console.log("Q5:", schoolName);

// 6. Understand Scope
if (true) {
    var a = "Accessible outside";
    let b = "Hidden outside";
    const c = "Hidden outside";
}

console.log("Q6 var:", a); // Works. 'var' is not block-scoped.
// console.log(b); // ReferenceError: 'let' is block-scoped and gets destroyed outside the if-block.
// console.log(c); // ReferenceError: 'const' is block-scoped and gets destroyed outside the if-block.

// 7. Test Re-declaration
var user = "Alice";
var user = "Bob"; // 'var' allows you to re-declare the same variable name.
console.log("Q7 var re-declaration:", user); 

let user2 = "Charlie";
// let user2 = "Dave"; // SyntaxError: 'let' STRICTLY forbids re-declaring the same variable name in the same scope.

// 8. Test Re-assignment
var varTest = 10;
let letTest = 20;
const constTest = 30;

varTest = 15; // Allowed
letTest = 25; // Allowed
// constTest = 35; // TypeError: Assignment to constant variable. 'const' cannot be re-assigned.


// Part c

// 9. Predict and Explain
/*
var x = 10;
if (true) {
    var x = 20;
    let y = 30;
    const z = 40;
}
console.log(x); // Output: 20. Explanation: 'var' ignores block scope, so the inner 'x' overwrites the outer 'x'.
console.log(y); // Error: ReferenceError. Explanation: 'let' is block-scoped and doesn't exist here.
console.log(z); // Error: ReferenceError. Explanation: 'const' is block-scoped and doesn't exist here.
*/


// 10. Fix the Program
// Fix 1: 'const' must be initialized with a value at the exact time it is declared.
const fixedName = "Ayush";

// Fix 2: 'let' cannot be re-declared. The second line should just re-assign the value.
let fixedAge = 20;
fixedAge = 25;

// Fix 3: To use 'country' outside the block, declare it in the outer scope first.
let country;

if (true) {
    var fixedCity = "Delhi";
    country = "India"; // Now it modifies the variable in the outer scope
}

console.log("Q10:", country);

// Fix 4: 'score' is being re-assigned on the second line, so it must be 'let', not 'const'.
let finalScore = 50;
finalScore = 80;
