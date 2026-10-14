// A] if Statement

// 1. Write a program to check if a number is divisible by 5. If yes, print “Divisible by 5”.
let numA1 = 25;
if (numA1 % 5 === 0) {
console.log("Divisible by 5");
}

// 2. Check if a person’s age is greater than or equal to 60. If true, print “Senior Citizen”.
let ageA2 = 65;
if (ageA2 >= 60) {
console.log("Senior Citizen");
}

// 3. Write a program that checks if a given number is greater than 100. If yes, print “Big Number”.
let numA3 = 150;
if (numA3 > 100) {
console.log("Big Number");
}

// 4. Check if the temperature is less than 10. If true, print “Very Cold”.
let tempA4 = 5;
if (tempA4 < 10) {
console.log("Very Cold");
}

// 5. Write a program to check if a student scored full marks (100). If yes, print “Perfect Score”.
let marksA5 = 100;
if (marksA5 === 100) {
console.log("Perfect Score");
}

// 6. Check if a number is negative. If it is, print “Negative Number”.
let numA6 = -10;
if (numA6 < 0) {
console.log("Negative Number");
}

// 7. Write a program that checks if a user has entered an empty string. If the string is empty, print “No input provided”.
let strA7 = "";
if (strA7 === "") {
console.log("No input provided");
}

// 8. Check if a given year is divisible by 100. If yes, print “Century Year”.
let yearA8 = 2000;
if (yearA8 % 100 === 0) {
console.log("Century Year");
}

// 9. Write a program to check if a number is both positive and even using a single if condition. If true, print “Positive Even Number”.
let numA9 = 12;
if (numA9 > 0 && numA9 % 2 === 0) {
console.log("Positive Even Number");
}

// 10. Check if the value of a variable marks is greater than or equal to 35 and less than or equal to 100. If true, print “Valid Marks”.
let marksA10 = 75;
if (marksA10 >= 35 && marksA10 <= 100) {
console.log("Valid Marks");
}

// B] if...else Statement

// 1. Write a program to check whether a number is even or odd.
let numB1 = 15;
if (numB1 % 2 === 0) {
console.log("Even");
} else {
console.log("Odd");
}

// 2. Check if a person is eligible to vote (age ≥ 18). Print “Eligible” or “Not Eligible”.
let ageB2 = 20;
if (ageB2 >= 18) {
console.log("Eligible");
} else {
console.log("Not Eligible");
}

// 3. Write a program that checks whether a number is positive or negative.
let numB3 = -5;
if (numB3 >= 0) {
console.log("Positive");
} else {
console.log("Negative");
}

// 4. Check if a student has passed or failed based on marks (pass mark = 35).
let marksB4 = 30;
if (marksB4 >= 35) {
console.log("Passed");
} else {
console.log("Failed");
}

// 5. Write a program to check whether a given character is an uppercase letter or not.
let charB5 = 'G';
if (charB5 >= 'A' && charB5 <= 'Z') {
console.log("Uppercase Letter");
} else {
console.log("Not an Uppercase Letter");
}

// 6. Check if a number is divisible by 3 or not. Print appropriate messages.
let numB6 = 9;
if (numB6 % 3 === 0) {
console.log("Divisible by 3");
} else {
console.log("Not divisible by 3");
}

// 7. Write a program that takes a password as input. If the password is “admin123”, print “Login Successful”, otherwise print “Incorrect Password”.
let passB7 = "admin123";
if (passB7 === "admin123") {
console.log("Login Successful");
} else {
console.log("Incorrect Password");
}

// 8. Check whether a given year is a leap year or not using the basic rule (divisible by 4).
let yearB8 = 2024;
if (yearB8 % 4 === 0) {
console.log("Leap Year");
} else {
console.log("Not a Leap Year");
}

// 9. Write a program to find the greater of two numbers using if...else.
let num1B9 = 40;
let num2B9 = 25;
if (num1B9 > num2B9) {
console.log(num1B9 + " is greater");
} else {
console.log(num2B9 + " is greater");
}

// 10. Check if a number is positive, negative, or zero using only if...else.
let numB10 = 0;
if (numB10 > 0) {
console.log("Positive");
} else if (numB10 < 0) {
console.log("Negative");
} else {
console.log("Zero");
}
