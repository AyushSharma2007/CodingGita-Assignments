// 📝 JavaScript Assignment

// `for` Loop

// Q1.
// A teacher wants students to practice counting. Write a program to print all numbers from 1 to 15.
for (let i = 1; i <= 15; i++) {
  console.log(i);
}

// Q2.
// A school has lockers numbered with even numbers for a special activity. Write a program to print all even numbers from 2 to 40.
for (let i = 2; i <= 40; i += 2) {
  console.log(i);
}

// Q3.
// A fitness coach assigns odd numbers to participants for a special activity. Write a program to print all odd numbers from 1 to 35.
for (let i = 1; i <= 35; i += 2) {
  console.log(i);
}

// Q4. 
// You save ₹10 on Day 1, ₹20 on Day 2, ₹30 on Day 3, and continue increasing your daily savings by ₹10. Write a program to calculate your total savings after 10 days.
let totalSavings = 0;
for (let day = 1; day <= 10; day++) {
  let dailySavings = day * 10;
  totalSavings += dailySavings;
}
console.log("Total savings after 10 days: ₹" + totalSavings);

// Q5. 
// You want to practice multiplication. Write a program to print the multiplication table of 12, from 12 × 1 to 12 × 10.
let num = 12;
for (let i = 1; i <= 10; i++) {
  console.log(num + " x " + i + " = " + (num * i));
}

// Q6. 
// You drink 3 glasses of water every day. Write a program to calculate the total number of glasses you drink over 7 days. Print the cumulative total after each day.
let totalGlasses = 0;
for (let day = 1; day <= 7; day++) {
  totalGlasses += 3;
  console.log("Day " + day + ": " + totalGlasses + " glasses");
}

// Q7. 
// One chocolate costs ₹15. Write a program to print the total cost of buying 1 to 10 chocolates.
let costPerChocolate = 15;
for (let i = 1; i <= 10; i++) {
  let totalCost = i * costPerChocolate;
  let label = i === 1 ? " chocolate = ₹" : " chocolates = ₹";
  console.log(i + label + totalCost);
}

// Q8.
// You want to calculate the sum of all even numbers between 2 and 30, including both 2 and 30. Write a program to calculate and print the total.
let sumOfEvens = 0;
for (let i = 2; i <= 30; i += 2) {
  sumOfEvens += i;
}
console.log("Sum of even numbers: " + sumOfEvens);

// Q9. 
// You do 5 push-ups on Day 1, 10 on Day 2, 15 on Day 3, and continue increasing the number by 5 each day. Write a program to print the number of push-ups for each day over 7 days.
for (let day = 1; day <= 7; day++) {
let pushups = day * 5;
  console.log("Day " + day + ": " + pushups + " push-ups");
}

// Q10. 
// One movie ticket costs ₹150. Write a program to print the total ticket cost for 1 to 8 people.
let pricePerTicket = 150;
for (let person = 1; person <= 8; person++) {
  let totalCost = person * pricePerTicket;
  let personLabel = person === 1 ? " person: ₹" : " people: ₹";
  console.log(person + personLabel + totalCost);
}

// Part B

// 1. Given an array of temperatures [28, 32, 25, 40, 18, 35], use a for loop to count how many days were hotter than 30°C.
let temps = [28, 32, 25, 40, 18, 35];
let hotDaysCount = 0;
for (let i = 0; i < temps.length; i++) {
  if (temps[i] > 30) {
    hotDaysCount++;
}
}
console.log(hotDaysCount);

// 2. Write a for loop that calculates the sum of all digits of a given number (example: 4729 -> 4+7+2+9 = 22).
let numStr = String(num);
let sum = 0;
for (let i = 1; i <= numStr.length; i++) {
  let last_digit = num % 10;
  sum += last_digit;
  num = Math.floor(num / 10);
}
console.log(sum);

// 3. Create a for loop that prints only the numbers between 1 and 100 that are divisible by both 3 and 5, but not by 7.
for (let i = 1; i <= 100; i++) {
  if (i % 3 === 0 && i % 5 === 0 && i % 7 !== 0) {  
    console.log(i);
}
}

// 4. Given the string "JavaScript", use a for loop to create a new string that contains only the consonants (remove vowels).
let str = "JavaScript";
let consonantsOnly = "";
let vowels = "aeiouAEIOU";
for (let i = 0; i < str.length; i++) {
  let isVowel = false;
  for (let j = 0; j < vowels.length; j++) {
    if (str[i] === vowels[j]) {
      isVowel = true;
      break;
}
}
if (!isVowel) {
  consonantsOnly += str[i];
}
}
console.log(consonantsOnly);

// 5. Write a for loop that finds the largest number in an array of positive integers without using any sorting method.
let nums = [14, 55, 2, 99, 23];
let largest = nums[0];
for (let i = 1; i < nums.length; i++) {
  if (nums[i] > largest) {
    largest = nums[i];
}
}
console.log(largest);

// 6. Use a for loop to check whether a given number is a perfect number (a number equal to the sum of its proper divisors). Example: 28.
let testNum = 28;
let sumDivisors = 0;
for (let i = 1; i < testNum; i++) {
  if (testNum % i === 0) {
    sumDivisors += i;
}
}
if (sumDivisors === testNum) {
  console.log(testNum + " is a perfect number.");
} else {
  console.log(testNum + " is not a perfect number.");
}

// 7. Print the following series using a single for loop: 1 2 4 8 16 32 64 128
let series = "";
for (let i = 1; i <= 128; i *= 2) {
  series += i + (i === 128 ? "" : " ");
}
console.log(series);

// 8. Write a for loop that prints the first 20 Fibonacci numbers (starting with 0 and 1).
let a = 0;
let b = 1;
let bag = "0 1 ";
for (let i = 1; i <= 18; i++) {
  let c = a + b;
  bag += c + " ";
  a = b;
  b = c;
}
console.log(bag);

// 9. Given an array of student scores [45, 78, 90, 32, 56, 88], use a for loop to calculate the average and also count how many students scored above the average.
let scores = [45, 78, 90, 32, 56, 88];
let totalScore = 0;
for (let i = 0; i < scores.length; i++) {
  totalScore += scores[i];
}
let average = totalScore / scores.length;

let aboveAverageCount = 0;
for (let i = 0; i < scores.length; i++) {
  if (scores[i] > average) {
    aboveAverageCount++;
}
}
console.log("Average:", average, "| Above average:", aboveAverageCount);

// 10. Write a for loop that converts a decimal number to its binary representation.
let num = 49;
let binary = "";
for (; num != 0; ) {
  let remainder = num % 2;
  binary = remainder + binary;
  num = Math.floor(num / 2);
}
console.log(binary);

// Part C-a

// 1. Write a for loop that searches for the first occurrence of the number 7 in an array. As soon as it finds 7, print its index and stop the loop using break.
let searchArr = [2, 9, 4, 7, 5, 7];
for (let i = 0; i < searchArr.length; i++) {
  if (searchArr[i] === 7) {
    console.log("Found 7 at index:", i);
    break;
}
}

// 2. Simulate a simple password checker: keep asking the user for a password (using a for loop that runs maximum 5 times). If the correct password is entered, print “Access granted” and break. If all 5 attempts fail, print “Account locked”.
let attempts = ["pass", "123", "secret", "correct_password", "wrong"];
let correct = "correct_password";
for (let i = 0; i < 5; i++) {
  let guess = attempts[i];
  if (guess === correct) {
    console.log("Access granted");
    break;
}
if (i === 4) {
  console.log("Account locked");
}
}

// 3. Write a for loop that adds numbers from 1 onwards until the sum exceeds 100. Print the last number that was added before the sum crossed 100 and stop using break.
let currentSum = 0;
let lastAdded = 0;
for (let i = 1; ; i++) {
  currentSum += i;
  if (currentSum > 100) {
    console.log(lastAdded);
    break;
}
lastAdded = i;
}

// 4. Given an array of names, use a for loop to find the first name that starts with the letter “S”. Print that name and immediately stop the loop with break.
let nameList = ["Ayush", "Rohan", "Sam", "Siddharth", "Amit"];
for (let i = 0; i < nameList.length; i++) {
  if (nameList[i][0] === "S") {
    console.log(nameList[i]);
    break;
}
}

// 5. Create a for loop that prints numbers from 1 to 50. Stop completely (break) as soon as you encounter a number that is both a perfect square and greater than 20.
for (let i = 1; i <= 50; i++) {
  let isSquare = false;
  for (let j = 1; j * j <= i; j++) {
    if (j * j === i) {
      isSquare = true;
      break;
}
}
if (i > 20 && isSquare) {
  break;
}
console.log(i);
}

// Part C-b

// 1. Print all numbers from 1 to 30, but skip every number that is divisible by 4 using continue.
for (let i = 1; i <= 30; i++) {
  if (i % 4 === 0) {
    continue;
}
console.log(i);
}

// 2. Given an array of mixed positive and negative numbers, use a for loop with continue to calculate the sum of only the positive numbers.
let mixedNumbers = [10, -5, 20, -3, 15];
let positiveSum = 0;
for (let i = 0; i < mixedNumbers.length; i++) {
  if (mixedNumbers[i] < 0) {
    continue;
}
positiveSum += mixedNumbers[i];
}
console.log(positiveSum);

// 3. Write a for loop that prints every character of the string "Hello World", but skips all spaces using continue.
let greetStr = "Hello World";
for (let i = 0; i < greetStr.length; i++) {
  if (greetStr[i] === " ") {
    continue;
}
console.log(greetStr[i]);
}

// 4. Print the multiplication table of 6 from 1 to 12, but skip the rows where the product is divisible by 5 (use continue).
for (let i = 1; i <= 12; i++) {
  let product = 6 * i;
  if (product % 5 === 0) {
    continue;
}
console.log("6 x " + i + " = " + product);
}

// 5. Given an array of ages [12, 18, 25, 15, 30, 17, 22], use a for loop with continue to print only the ages of people who are eligible to vote (age >= 18).
let ageArr = [12, 18, 25, 15, 30, 17, 22];
for (let i = 0; i < ageArr.length; i++) {
  if (ageArr[i] < 18) {
    continue;
}
console.log(ageArr[i]);
}
