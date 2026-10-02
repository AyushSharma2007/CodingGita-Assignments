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


// Part e — Basic Identification

// 1. Classify the Types

let wholeNum = 42;
let decimalNum = 3.14;
let text = "Vantika"; 
let isComplete = true;

console.log(wholeNum, typeof wholeNum);       // 42 'number'
console.log(decimalNum, typeof decimalNum);   // 3.14 'number'
console.log(text, typeof text);               // Vantika 'string'
console.log(isComplete, typeof isComplete);   // true 'boolean'



// 2. Undefined vs Null

let a;
let b = null;

console.log(a, typeof a); // undefined 'undefined'
console.log(b, typeof b); // null 'object'


// The Difference: `undefined` is JavaScript's default state for a variable that has been declared but hasn't been given a value yet. `null` is a value you explicitly assign to indicate an intentional absence of data (an empty state). Note that `typeof null` returning `"object"` is a notorious, legacy bug in JavaScript that was never fixed to avoid breaking old websites.

// 3. Number Special Values

let posInf = Infinity;
let negInf = -Infinity;
let notANum = NaN;
let sciNum = 2.5e3;
let readableNum = 1_000_000;

console.log(posInf, typeof posInf);       // Infinity 'number'
console.log(negInf, typeof negInf);       // -Infinity 'number'
console.log(notANum, typeof notANum);     // NaN 'number'
console.log(sciNum, typeof sciNum);       // 2500 'number'
console.log(readableNum, typeof readableNum); // 1000000 'number'


// 4. String Styles

let single = 'Single quotes';
let double = "Double quotes";
let template = `Using template literals with ${single}`;

console.log(single);
console.log(double);
console.log(template);



// Part f — Advanced Primitive Types

// 5. Symbol Uniqueness

let sym1 = Symbol('id');
let sym2 = Symbol('id');

console.log(sym1 === sym2); // false

let userObj = {
  [sym1]: "First ID Data",
  [sym2]: "Second ID Data"
};

console.log(userObj[sym1]); // "First ID Data"
console.log(userObj[sym2]); // "Second ID Data"


// Why it returns `false`: Every Symbol generated is fundamentally unique, even if they share the same description label. The string `'id'` is just a tag for your own debugging, not the underlying value. This makes them perfect for object keys that will never accidentally overwrite each other.

// 6. BigInt Precision

let max = 9007199254740991;
console.log(max + 1); // 9007199254740992
console.log(max + 2); // 9007199254740992 (Precision lost!)
console.log(max + 3); // 9007199254740994 (Precision lost!)

let bigMax = 9007199254740991n;
console.log(bigMax + 1n); // 9007199254740992n
console.log(bigMax + 2n); // 9007199254740993n
console.log(bigMax + 3n); // 9007199254740994n


// The Difference: Standard JavaScript numbers use 64-bit floating-point formatting, meaning they lose exact precision after `Number.MAX_SAFE_INTEGER`. BigInt allows you to bypass this memory limit and perform accurate math on infinitely large integers.

// 7. Choose the Correct Type

// A unique identifier...: `Symbol` (e.g., `let id = Symbol("hash");`)
// A very large integer...: `BigInt` (e.g., `let debt = 999999999999999999n;`)
// Declared but not given a value: `undefined` (e.g., `let user;`)
// An intentional empty value: `null` (e.g., `let activeSession = null;`)


// Part g — Prediction & Fixing

// 8. Predict the Output

//  `typeof a, a`: "undefined" undefined (Declared but unassigned variables default to undefined).
//  `typeof b, b`: "object" null (The historic JavaScript bug mentioned earlier where `typeof null` incorrectly reports as object).
//  `typeof c, c`: "number" 42 (Standard whole integer).
//  `typeof d, d`: "string" "Hello" (Standard text string).
//  `typeof e, e`: "boolean" true (Standard logical value).
//  `typeof f, f`: "symbol" Symbol(key) (The string 'key' is just its description).
//  `typeof g, g`: "bigint" 123n (The `n` suffix denotes a BigInt).

// 9. Fix the Code
// The original code contained unquoted strings, improper capitalization for booleans/nulls, and incorrect object casing for Symbol.

let num = 10;
let text = "Hello";         // Added quotes around the string
let flag = true;            // Lowercased 'true'
let empty;                  
let nothing = null;         // Lowercased 'null'
let unique = Symbol("id");  // Capitalized 'Symbol'
let big = 9007199254740991n; // Added 'n' to safely handle the max integer limit

console.log(num, text, flag, empty, nothing, unique, big);


// 10. Primitive vs Non-Primitive

// a) Main Difference: Primitive types are immutable (their core value cannot be altered) and are stored in memory directly by their actual value. 
//                     Non-primitives are mutable and are stored by a reference (a memory address) pointing to where the data lives.
// b) Why they are Primitive: Numbers, Strings, Booleans, etc., hold one single, simple piece of data. When you assign one primitive to another variable, it creates a completely independent copy of that value.
// c) Non-Primitive Example: An Object 
//    (e.g., `let user = { name: "Ayush", age: 20 };`).
//    It is non-primitive because it is a structural collection of multiple values, and if you assign `user` to a new variable, they both point to the exact same object in memory—changing one changes both.
