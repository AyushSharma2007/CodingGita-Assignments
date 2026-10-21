// 📝 JavaScript Assignment

// `for` Loop

// Q1. Counting Numbers 
// A teacher wants students to practice counting. Write a program to print all numbers from 1 to 15.
for (let i = 1; i <= 15; i++) {
console.log(i);
}

// Q2. Even Numbers 
// A school has lockers numbered with even numbers for a special activity. Write a program to print all even numbers from 2 to 40.
for (let i = 2; i <= 40; i += 2) {
console.log(i);
}

// Q3. Odd Numbers 
// A fitness coach assigns odd numbers to participants for a special activity. Write a program to print all odd numbers from 1 to 35.
for (let i = 1; i <= 35; i += 2) {
console.log(i);
}

// Q4. Saving Money 
// You save ₹10 on Day 1, ₹20 on Day 2, ₹30 on Day 3, and continue increasing your daily savings by ₹10. Write a program to calculate your total savings after 10 days.
let totalSavings = 0;
for (let day = 1; day <= 10; day++) {
let dailySavings = day * 10;
totalSavings += dailySavings;
}
console.log("Total savings after 10 days: ₹" + totalSavings);

// Q5. Multiplication Table 
// You want to practice multiplication. Write a program to print the multiplication table of 12, from 12 × 1 to 12 × 10.
let num = 12;
for (let i = 1; i <= 10; i++) {
console.log(num + " x " + i + " = " + (num * i));
}

// Q6. Daily Water Intake 
// You drink 3 glasses of water every day. Write a program to calculate the total number of glasses you drink over 7 days. Print the cumulative total after each day.
let totalGlasses = 0;
for (let day = 1; day <= 7; day++) {
totalGlasses += 3;
console.log("Day " + day + ": " + totalGlasses + " glasses");
}

// Q7. Shopping Calculation 
// One chocolate costs ₹15. Write a program to print the total cost of buying 1 to 10 chocolates.
let costPerChocolate = 15;
for (let i = 1; i <= 10; i++) {
let totalCost = i * costPerChocolate;
let label = i === 1 ? " chocolate = ₹" : " chocolates = ₹";
console.log(i + label + totalCost);
}

// Q8. Sum of Even Numbers 
// You want to calculate the sum of all even numbers between 2 and 30, including both 2 and 30. Write a program to calculate and print the total.
let sumOfEvens = 0;
for (let i = 2; i <= 30; i += 2) {
sumOfEvens += i;
}
console.log("Sum of even numbers: " + sumOfEvens);

// Q9. Weekly Exercise 
// You do 5 push-ups on Day 1, 10 on Day 2, 15 on Day 3, and continue increasing the number by 5 each day. Write a program to print the number of push-ups for each day over 7 days.
for (let day = 1; day <= 7; day++) {
let pushups = day * 5;
console.log("Day " + day + ": " + pushups + " push-ups");
}

// Q10. Movie Tickets 
// One movie ticket costs ₹150. Write a program to print the total ticket cost for 1 to 8 people.
let pricePerTicket = 150;
for (let person = 1; person <= 8; person++) {
let totalCost = person * pricePerTicket;
let personLabel = person === 1 ? " person: ₹" : " people: ₹";
console.log(person + personLabel + totalCost);
}
